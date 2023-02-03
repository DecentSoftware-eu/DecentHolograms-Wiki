---
description: General usage of commands.
---

# ⌨ Commands

DecentHolograms offers a user-friendly command interface that allows you to edit almost everything without the need to edit config files. Additionally, all commands feature tab-completion functionality, making it even easier to use them.

**You can view all commands by using:**

* [ ] /dh help - For general help.
* [ ] /dh holograms help - For help with Holograms related commands.
* [ ] /dh lines help - For help with Hologram Lines related commands.
* [ ] /dh features help - For help with Features related commands.

### Arguments

Parenthesis only specify the type of an argument, they are not part of the final command.

| Parenthesis | Meaning                  |
| ----------- | ------------------------ |
| <>          | Required argument.       |
| \[]         | Optional argument.       |
| {}          | List of possible values. |

### Aliases

DecentHolograms utilizes a single, main command with many subcommands. To streamline the process, we have added useful aliases to make it more convenient for you. These aliases are visible in help messages and tab-completion, and some of the most important ones are listed in the table below.

| (Sub)command name               | Aliases                           |
| ------------------------------- | --------------------------------- |
| Main command - /decentholograms | /holograms, /hologram, /holo, /dh |
| Hologram  - holograms           | hologram, holo, h                 |
| Lines - lines                   | line, l                           |
| Features - features             | feature, f                        |
| Pages - pages                   | page, p                           |

{% hint style="info" %}
For example, instead of:

`/decentholograms holograms create demo`

You can just use:

`/dh h c demo`
{% endhint %}
