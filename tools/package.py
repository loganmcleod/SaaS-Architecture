#!/usr/bin/env python3
"""Validate, build and install the text-only skill. Install uses only stdlib."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
NAME = "enterprise-saas-architecture"
ALLOWED_SUFFIXES = {".md", ".yaml"}


def package_files(root: Path) -> list[Path]:
    """An explicit runtime boundary; never walk private workspace artifacts."""
    skill = root / "skills" / NAME
    if skill.is_symlink() or not (skill / "SKILL.md").is_file():
        raise ValueError("Expected an ordinary skill directory with SKILL.md")
    files = []
    for path in sorted(skill.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlinks cannot be distributed: {path.relative_to(root)}")
        if path.is_dir():
            continue
        if not path.is_file() or (path.name != "LICENSE" and path.suffix not in ALLOWED_SUFFIXES):
            raise ValueError(f"Unexpected runtime file: {path.relative_to(root)}")
        if any(part.startswith(".") for part in path.relative_to(skill).parts):
            raise ValueError(f"Hidden runtime file: {path.relative_to(root)}")
        files.append(path)
    if (skill / "LICENSE").read_bytes() != (root / "LICENSE").read_bytes():
        raise ValueError("Root and bundled MIT licenses must match")
    return files


def version(root: Path) -> str:
    value = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", value):
        raise ValueError("VERSION must contain a semantic version")
    return value


def validate(root: Path) -> list[Path]:
    try:
        import yaml
    except ImportError as error:
        raise ValueError("Validation/build requires: python -m pip install -r requirements-dev.txt") from error
    files = package_files(root)
    version(root)
    skill = root / "skills" / NAME
    content = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not match:
        raise ValueError("SKILL.md needs YAML frontmatter")
    front = yaml.safe_load(match.group(1))
    if not isinstance(front, dict) or front.get("name") != NAME or front.get("license") != "MIT":
        raise ValueError("Skill name/license metadata is invalid")
    description = front.get("description")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        raise ValueError("Skill description must contain 1–1024 characters")
    for path in files + list((root / ".github").rglob("*.yml")):
        if path.suffix in {".yaml", ".yml"}:
            yaml.safe_load(path.read_text(encoding="utf-8"))
    context = yaml.safe_load((skill / "assets/company-context.yaml").read_text(encoding="utf-8"))
    if context.get("profile") != "general" or context["confirmed_profile"].get("industry") is not None:
        raise ValueError("Public context template must not contain company-specific defaults")
    docs = [root / name for name in ("README.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md")]
    docs += list((root / "docs").rglob("*.md"))
    docs += list((root / ".github").rglob("*.md"))
    for path in files + docs:
        text = path.read_text(encoding="utf-8")
        if re.search(r"/Users/[^/\s]+/|/home/[^/\s]+/|[A-Za-z]:\\Users\\", text):
            raise ValueError(f"Machine-specific user path: {path.relative_to(root)}")
        if "[TODO:" in text or "FIXME" in text:
            raise ValueError(f"Unfinished scaffold: {path.relative_to(root)}")
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            destination = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            boundary = skill if path in files else root
            if not destination.is_relative_to(boundary.resolve()) or not destination.exists():
                raise ValueError(f"Broken/nonportable link in {path.relative_to(root)}: {target}")
    catalog = (skill / "references/discipline-catalog.md").read_text(encoding="utf-8")
    if re.findall(r"^\| (D\d\d) \|", catalog, re.M) != [f"D{i:02d}" for i in range(1, 21)]:
        raise ValueError("Discipline catalog must contain D01–D20 exactly once and in order")
    return files


def build(root: Path, output: Path) -> Path:
    files = validate(root)
    skill = root / "skills" / NAME
    if output.resolve().is_relative_to(skill.resolve()):
        raise ValueError("Build output must stay outside the runtime skill directory")
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"{NAME}-{version(root)}.zip"
    entries = {f"{NAME}/{p.relative_to(skill).as_posix()}": p.read_bytes() for p in files}
    entries[f"{NAME}/VERSION"] = (version(root) + "\n").encode()
    # Fixed timestamp, permissions and order; no local paths or source mtimes.
    # Stored entries avoid checksum differences across zlib implementations.
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_STORED) as zipped:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            zipped.writestr(info, data)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    return archive


def install(root: Path, destination: Path, replace: bool = False) -> tuple[Path, Path | None]:
    files = package_files(root)
    skill = root / "skills" / NAME
    destination = destination.expanduser().resolve()
    target = destination / NAME
    if destination.is_relative_to(skill.resolve()) or target == skill.resolve():
        raise ValueError("Installation must not replace or be nested inside the source skill")
    occupied = target.exists() or target.is_symlink()
    if occupied and not replace:
        raise ValueError("Installation exists; use --replace to preserve a backup and update")
    destination.mkdir(parents=True, exist_ok=True)
    backup = None
    with tempfile.TemporaryDirectory(prefix=".saas-architecture-stage-", dir=destination.parent) as temporary:
        staged = Path(temporary) / NAME
        staged.mkdir()
        for path in files:
            relative = path.relative_to(skill)
            copied = staged / relative
            copied.parent.mkdir(parents=True, exist_ok=True)
            copied.write_bytes(path.read_bytes())
        (staged / "VERSION").write_text(version(root) + "\n", encoding="utf-8")
        if occupied:
            backups = destination.parent / f".{destination.name}-saas-architecture-backups"
            backups.mkdir(exist_ok=True)
            backup = backups / f"{NAME}-{uuid.uuid4().hex}"
            target.rename(backup)
        try:
            staged.rename(target)
        except OSError:
            if backup is not None:
                backup.rename(target)
            raise
    return target, backup


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    builder = commands.add_parser("build")
    builder.add_argument("--output", type=Path, default=ROOT / "dist")
    installer = commands.add_parser("install")
    installer.add_argument("--destination", required=True, type=Path, help="Parent skills directory")
    installer.add_argument("--replace", action="store_true", help="Back up an existing entry before updating")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            print(f"Validated {len(validate(ROOT))} runtime files and repository documentation")
        elif args.command == "build":
            print(build(ROOT, args.output))
        else:
            target, backup = install(ROOT, args.destination, args.replace)
            print(f"Installed: {target}")
            if backup:
                print(f"Previous installation preserved: {backup}")
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
