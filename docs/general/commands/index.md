---
title: Commands
icon: material/keyboard
---

DecentHolograms offers a user-friendly command interface that allows you to edit almost everything without the need to edit config files. Additionally, all commands feature tab-completion functionality, making it even easier to use them.

**You can view all commands by using:**

- `/dh help` - For general help.
- `/dh holograms help` - For help with Holograms related commands.
- `/dh lines help` - For help with Hologram Lines related commands.
- `/dh features help` - For help with Features related commands.

## Arguments

Parenthesis only specifiy the type of an argument, they are **not** part of the final command.

| Parenthesis | Meaning                  |
|-------------|--------------------------|
| `<>`        | Required argument.       |
| `[]`        | Optional argument.       |
| `{}`        | List of possible values. |

## Aliases

DecentHolograms utilizes a single, main command with many subcommands. To streamline the process, we have added useful aliases to make it more convenient for you. These aliases are visible in help messages and tab-completions, and some of the most important ones are listed in the table below.

| Type                | (Sub)command name | Aliases                           |
|---------------------|-------------------|-----------------------------------|
| Main command        | /decenholograms   | /holograms, /hologram, /holo, /dh |
| Hologram subcommand | holograms         | hologram, holo, h                 |
| Lines subcommand    | lines             | line, l                           |
| Features subcommand | features          | feature, f                        |
| Pages subcommand    | pages             | page, p                           |

!!! example
    Instead of
    ```
    /decentholograms holograms create demo
    ```
    You can just use:
    ```
    /dh h c demo
    ```