---
title: Hologram Line
subtitle: General usage and editing of hologram lines
---

## Commands

> Aliases: `line`, `l`

You can simply view all commands for hologram lines using the following command:

> ```
> /dh lines help
> ```

### `#!html /dh l add <hologram> <page> <content>` { #dh-l-add }

> Aliases: `append`

Add a new line into hologram.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line should be.
- `#!html <conten>` - [Content](../format-and-colors/index.md) of the new line.

### `#!html /dh l set <hologram> <page> <line> <content>` { #dh-l-set }

Set a new content to hologram line.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.
- `#!html <conten>` - [Content](../format-and-colors/index.md) of the new line.

### `#!html /dh l insert <hologram> <page> <line> <content>` { #dh-l-insert }

Insert a new line into hologram at the position of the given line number.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.
- `#!html <conten>` - [Content](../format-and-colors/index.md) of the new line.

### `#!html /dh l remove <hologram> <page> <line>` { #dh-l-remove }

> Aliases: `rem`, `delete`, `del`

Remove a line from hologram.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.

### `#!html /dh l swap <hologram> <page> <line1> <line2>` { #dh-l-swap }

Swap two lines in a hologram.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the lines are.
- `#!html <line1>` - Index of the first line.
- `#!html <line2>` - Index of the second line.

### `#!html /dh l info <hologram> <page> <line>` { #dh-l-info }

Display some general info about a hologram line.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.

### `#!html /dh l edit <hologram> <page> <line>` { #dh-l-edit }

Edit line in a hologram. Sends you a clickable message that puts a command to edit the line into your chat field.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.

### `#!html /dh l height <hologram> <page> <line> <newHeight>` { #dh-l-height }

Set a new height to hologram line.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.
- `#!html <newHeight>` - New X offset. (0.0 - 2.5)

### `#!html /dh l offsetx <hologram> <page> <line> <offset>` { #dh-l-offsetx }

Set a new X offset to hologram line.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.
- `#!html <offset>` - New X offset. (0.0 - 2.5)

### `#!html /dh l offsetz <hologram> <page> <line> <offset>` { #dh-l-offsetz }

Set a new Z offset to hologram line.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.
- `#!html <offset>` - New Z offset. (0.0 - 2.5)

### `#!html /dh l setfacing <hologram> <page> <line> <facing>` { #dh-l-setfacing }

> Aliases: `facing`, `face`

Set the rotation of hologram line facing (Yaw).

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.
- `#!html <facing>` - Angle of rotation in degrees, or a cardinal direction (`NORTH`, `EAST`, `SOUTH` or `WEST`).

### `#!html /dh l setpermission <hologram> <page> <line> [permission]` { #dh-l-setpermission }

> Aliases: `permission`, `setperm`, `perm`

Set the current permission required to view the hologram line.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line>` - Index of the line.
- `[permission]` - New permission. (Leave empty to remove)

### `#!html /dh l align <hologram> <page> <line1> <line2> {X|Z|XZ}` { #dh-l-align }

Align two lines in a hologram on the specified axis.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <page>` - Index of the page, on which the line is.
- `#!html <line1>` - Index of the first line.
- `#!html <line2>` - Index of the second line.
- `{X|Z|XZ}` - Align `<line1>` with `<line2>` on either the X, Z or both axis.