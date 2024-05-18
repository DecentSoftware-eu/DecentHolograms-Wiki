---
title: Commands
description: List of all the Commands DecentHolograms offers

icon: material/keyboard
---

DecentHolograms offers a user-friendly command interface that allows you to edit almost everything without the need to edit config files. Additionally, all commands feature tab-completion functionality, making it even easier to use them.

**You can view all commands by using:**

- `/dh help` - For general help.
- `/dh holograms help` - For help with Holograms related commands.
- `/dh lines help` - For help with Hologram Lines related commands.
- `/dh features help` - For help with Features related commands.

--8<-- "arguments.md"

## Aliases

DecentHolograms utilizes a single, main command with many subcommands. To streamline the process, we have added useful aliases to make it more convenient for you. These aliases are visible in help messages and tab-completions, and some of the most important ones are listed in the table below.

| Type                | (Sub)command name | Aliases                           |
|---------------------|-------------------|-----------------------------------|
| Main command        | /decentholograms  | /holograms, /hologram, /holo, /dh |
| Hologram subcommand | holograms         | hologram, holo, h                 |
| Lines subcommand    | lines             | line, l                           |
| Features subcommand | features          | feature, f                        |
| Pages subcommand    | pages             | page, p                           |

/// example
Instead of
```
/decentholograms holograms create demo
```
You can just use:
```
/dh h c demo
```
///

## Permissions

DecentHolograms offers specific sets of permissions for you to use.

| Permission                          | Description                                                                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dh.default`                        | Grants access to the main `/decentholograms` command (Only showing plugin info) and [`/dh version`](general.md#dh-version).                                       |
| `dh.admin`                          | Grants access to all commands and sub-commands of the plugin.                                                                                                     |
| `dh.command`                        | Same as `dh.admin`, granting access to all commands and sub-commands of the plugin.                                                                               |
| `dh.command.<command>`              | Grants access to a specific command of the plugin. I.e. `dh.command.version` allows access to [`/dh version`](general.md#dh-version).                             |
| `dh.command.<command>.<subcommand>` | Grants access to a specific sub-command of the plugin. I.e. `dh.command.holograms.create` allows access to [`/dh holograms create ...`](hologram.md#dh-h-create). |