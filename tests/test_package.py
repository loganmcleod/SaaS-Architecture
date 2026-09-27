"""Behavioral checks for distribution boundaries and non-destructive installs."""

from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from tools import package


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / "repo"
        self.root.mkdir()
        shutil.copytree(package.ROOT / "skills", self.root / "skills")
        shutil.copytree(package.ROOT / "docs", self.root / "docs")
        shutil.copytree(package.ROOT / ".github", self.root / ".github")
        for name in ["LICENSE", "VERSION", "README.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md"]:
            shutil.copy2(package.ROOT / name, self.root / name)
        self.destination = self.base / "installed"

    def test_install_refuses_overwrite_and_keeps_other_skills(self):
        target, backup = package.install(self.root, self.destination)
        self.assertIsNone(backup)
        (target / "local-note.md").write_text("preserve")
        sibling = self.destination / "other-skill"
        sibling.mkdir()
        with self.assertRaises(ValueError):
            package.install(self.root, self.destination)
        self.assertEqual((target / "local-note.md").read_text(), "preserve")
        self.assertTrue(sibling.is_dir())

    def test_replace_preserves_backup_and_removes_stale_files(self):
        target, _ = package.install(self.root, self.destination)
        (target / "stale.md").write_text("prior version")
        updated, backup = package.install(self.root, self.destination, replace=True)
        self.assertEqual((backup / "stale.md").read_text(), "prior version")
        self.assertFalse(backup.is_relative_to(self.destination))
        self.assertFalse((updated / "stale.md").exists())
        self.assertTrue((updated / "LICENSE").is_file())

    def test_replace_rolls_back_if_swap_fails(self):
        target, _ = package.install(self.root, self.destination)
        (target / "local.md").write_text("original")
        real_rename = Path.rename

        def fail_stage(path, destination):
            if path.parent.name.startswith(".saas-architecture-stage-"):
                raise OSError("simulated swap failure")
            return real_rename(path, destination)

        with patch.object(Path, "rename", fail_stage):
            with self.assertRaises(OSError):
                package.install(self.root, self.destination, replace=True)
        self.assertEqual((target / "local.md").read_text(), "original")

    def test_symlink_update_does_not_modify_source(self):
        self.destination.mkdir()
        external = self.base / "external"
        external.mkdir()
        (external / "note.md").write_text("leave intact")
        target = self.destination / package.NAME
        target.symlink_to(external, target_is_directory=True)
        _, backup = package.install(self.root, self.destination, replace=True)
        self.assertTrue(backup.is_symlink())
        self.assertEqual((external / "note.md").read_text(), "leave intact")
        self.assertFalse(target.is_symlink())

    def test_dangling_symlink_is_an_existing_installation(self):
        self.destination.mkdir()
        (self.destination / package.NAME).symlink_to(self.base / "missing")
        with self.assertRaises(ValueError):
            package.install(self.root, self.destination)

    def test_cannot_install_over_or_inside_source(self):
        for destination in [self.root / "skills", self.root / "skills" / package.NAME / "nested"]:
            with self.assertRaises(ValueError):
                package.install(self.root, destination, replace=True)

    def test_build_is_reproducible_and_excludes_private_files(self):
        private = self.root / ".local"
        private.mkdir()
        (private / "private.md").write_text("private-value")
        first = package.build(self.root, self.base / "first")
        second = package.build(self.root, self.base / "second")
        self.assertEqual(first.read_bytes(), second.read_bytes())
        with zipfile.ZipFile(first) as archive:
            self.assertTrue(all(name.startswith(package.NAME + "/") for name in archive.namelist()))
            self.assertIn(package.NAME + "/LICENSE", archive.namelist())
            self.assertIn(package.NAME + "/VERSION", archive.namelist())
            self.assertFalse(any(b"private-value" in archive.read(n) for n in archive.namelist()))
            self.assertIsNone(archive.testzip())

    def test_runtime_symlinks_and_unexpected_files_are_rejected(self):
        skill = self.root / "skills" / package.NAME
        linked = skill / "linked.md"
        linked.symlink_to(self.root / "LICENSE")
        with self.assertRaises(ValueError):
            package.package_files(self.root)
        linked.unlink()
        (skill / "credentials.json").write_text("{}")
        with self.assertRaises(ValueError):
            package.package_files(self.root)

    def test_validation_detects_broken_links(self):
        path = self.root / "skills" / package.NAME / "SKILL.md"
        with path.open("a") as stream:
            stream.write("\n[Missing reference](references/missing.md)\n")
        with self.assertRaisesRegex(ValueError, "Broken/nonportable"):
            package.validate(self.root)

    def test_runtime_links_cannot_depend_on_repository_docs(self):
        path = self.root / "skills" / package.NAME / "SKILL.md"
        with path.open("a") as stream:
            stream.write("\n[Repository README](../../README.md)\n")
        with self.assertRaisesRegex(ValueError, "Broken/nonportable"):
            package.validate(self.root)

    def test_build_cannot_pollute_runtime_source(self):
        with self.assertRaisesRegex(ValueError, "outside the runtime"):
            package.build(self.root, self.root / "skills" / package.NAME / "output")


if __name__ == "__main__":
    unittest.main()
