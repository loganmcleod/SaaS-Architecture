# Development and releases

The supported tooling baseline is Python 3.11+. The skill itself is agent-readable text and has no Python runtime dependency.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/package.py validate
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/package.py build
```

On Windows use `.venv\Scripts\python.exe` for the environment's interpreter. Tests use temporary directories, not the user's installed skills or cloud systems.

The validator checks skill metadata, YAML, relative links, complete discipline IDs, synchronized MIT licenses, allowed package files, symlink exclusion, scaffold markers and accidental local paths. This is a structural check, not a secret scanner or a guarantee of legal accuracy. Tests exercise install/update safety and reproducible archive boundaries. The build produces a versioned ZIP and SHA-256 companion in `dist/`. It includes only the runtime skill directory, plus the root version as `VERSION` inside the archive. It excludes personal context, reports, repository tools and Git metadata. Builds with identical inputs produce identical bytes.

## Changes and behavioral evaluation

Keep `SKILL.md` compact and route substantial guidance into references. Preserve explicit user context, distinguish unknowns from failures, and keep optional profiles conditional. Update relative links when moving files. Add focused tests for executable behavior and meaningful invariants; changes to prose do not need tests that merely match wording.

For substantial behavioral changes, independently execute relevant [synthetic cases](../skills/enterprise-saas-architecture/evals/cases.md). Give the evaluating agent the skill and input, withholding expected conclusions. Keep generated reports out of the package. Record which cases actually ran, their results and limits. Structural CI does not run an AI model or use API credentials.

The initial [validation history](validation.md) distinguishes prior synthetic checks from the new packaging checks. Fresh legal, vendor and model facts must be verified from the [source register](../skills/enterprise-saas-architecture/references/sources.md) when used.

## Version and release policy

`VERSION` is the package version. While pre-1.0, patch releases correct compatible content/tool defects; minor releases may change workflow or context contracts. Document user-visible changes in [CHANGELOG.md](../CHANGELOG.md). Preserve the context `schema_version` unless its structure changes; document migration when it does.

After review and successful CI, a maintainer may merge, tag the intended commit (`v` plus `VERSION`), build from that exact commit, and attach the ZIP/checksum to a GitHub release. Check a clean checkout and inspect archive contents before publishing. Tagging, merging, publishing a release and changing visibility are explicit maintainer actions; the build tool and CI do none of them. Keep the release notes clear about substantive changes, compatibility and checks actually run.
