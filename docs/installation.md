# Installation and updates

The runtime deliverable is `skills/enterprise-saas-architecture/`. It contains Markdown instructions, YAML metadata/templates, references, profiles, synthetic evaluation inputs and an MIT license. It needs an agent capable of reading skills; it does not run a service or require cloud credentials. Generic Markdown-capable agents can read `SKILL.md` directly, though automatic discovery is host-specific.

## From a repository checkout

Repository access is required while the GitHub repository is private.

```sh
git clone https://github.com/loganmcleod/SaaS-Architecture.git
cd SaaS-Architecture
python3 tools/package.py install --destination "$HOME/.codex/skills"
```

Python 3.11 or newer is supported for the repository tools. Installation uses only its standard library. The destination is the parent skills directory; the installer creates `enterprise-saas-architecture` underneath it. It refuses to overwrite an existing installation by default. To target another compatible host, pass that host's skills directory, for example `$HOME/.agents/skills` if the host discovers skills there. Do not install duplicate copies in multiple directories scanned by the same host.

For a deliberate update:

```sh
git pull --ff-only
python3 tools/package.py install --destination "$HOME/.codex/skills" --replace
```

The installer prepares a complete replacement first, preserves the previous entry in a hidden sibling backup directory outside the active skills directory, then swaps in the new copy. For a destination named `skills`, backups are in `.skills-saas-architecture-backups` beside it, so recursive skill discovery does not load old versions. It preserves a previous symlink as a symlink; it does not alter the linked source. Keep any backup needed for recovery. Company context is stored separately and is not replaced.

To remove an installation, remove only its `enterprise-saas-architecture` entry from the host's skills directory. Other skills and personal context are independent. A manually maintained development symlink is also valid; updating such a symlink with `--replace` intentionally replaces it with a copy.

## From a release archive

When a release is available, download its versioned ZIP and SHA-256 file from [GitHub Releases](https://github.com/loganmcleod/SaaS-Architecture/releases). No release is implied merely by the existence of these instructions. Check the checksum, inspect the archive, and extract its single `enterprise-saas-architecture/` directory into the host's skills directory. Preserve an existing installation before replacing it.

The same archive is produced locally by the build command in [development](development.md). Generated archives belong in `dist/`, not in Git history. Use tags or a reviewed commit when you need repeatable installations; the default branch can change.

## Invocation and context

Ask: `Use $enterprise-saas-architecture to assess this platform and propose a prioritized improvement plan.` If the host has not refreshed its catalog, start a new chat or give the path to the installed `SKILL.md`.

By default the skill uses a general GCP-first perspective. For automotive/public-company work, request `Use the automotive-us-public profile` or set `profile: automotive-us-public` in a copy of [the context template](../skills/enterprise-saas-architecture/assets/company-context.yaml).

Store project context at `.saas-architecture/context.yaml` in the assessed project, and ensure that project's ignore rules exclude it. Optional personal defaults live at `~/.config/saas-architecture/context.yaml`. Explicit engagement facts override project context; project context overrides personal defaults; the selected profile supplies remaining assumptions. See [context selection](../skills/enterprise-saas-architecture/references/company-profile.md).

Never put private client records inside the installed skill or a release archive. Selecting a profile does not establish legal applicability or production effectiveness.
