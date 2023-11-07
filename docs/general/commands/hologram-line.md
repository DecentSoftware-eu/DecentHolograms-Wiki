---
title: Hologram Line
subtitle: General usage and editing of hologram lines
---

## Commands

> Aliases: `line`, `l`

/// info | Command help
For a list of all available subcommands run the following command:  
```
/dh l help
```
///

### `#!command /dh l add <hologram> <page> <content>` { #dh-l-add }

> Aliases: `append`
> 
> Add a new line into hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line should be.
> - `#!command <conten>` - [Content](../format-and-colors/index.md) of the new line.

### `#!command /dh l set <hologram> <page> <line> <content>` { #dh-l-set }

> Set a new content to hologram line.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.
> - `#!command <conten>` - [Content](../format-and-colors/index.md) of the new line.

### `#!command /dh l insert <hologram> <page> <line> <content>` { #dh-l-insert }

> Insert a new line into hologram at the position of the given line number.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.
> - `#!command <conten>` - [Content](../format-and-colors/index.md) of the new line.

### `#!command /dh l remove <hologram> <page> <line>` { #dh-l-remove }

> Aliases: `rem`, `delete`, `del`
> 
> Remove a line from hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.

### `#!command /dh l swap <hologram> <page> <line1> <line2>` { #dh-l-swap }

> Swap two lines in a hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the lines are.
> - `#!command <line1>` - Index of the first line.
> - `#!command <line2>` - Index of the second line.

### `#!command /dh l info <hologram> <page> <line>` { #dh-l-info }

> Display some general info about a hologram line.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.

### `#!command /dh l edit <hologram> <page> <line>` { #dh-l-edit }

> Edit line in a hologram. Sends you a clickable message that puts a command to edit the line into your chat field.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.

### `#!command /dh l height <hologram> <page> <line> <newHeight>` { #dh-l-height }

> Set a new height to hologram line.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.
> - `#!command <newHeight>` - New X offset. (0.0 - 2.5)

### `#!command /dh l offsetx <hologram> <page> <line> <offset>` { #dh-l-offsetx }

> Set a new X offset to hologram line.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.
> - `#!command <offset>` - New X offset. (0.0 - 2.5)

### `#!command /dh l offsetz <hologram> <page> <line> <offset>` { #dh-l-offsetz }

> Set a new Z offset to hologram line.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.
> - `#!command <offset>` - New Z offset. (0.0 - 2.5)

### `#!command /dh l setfacing <hologram> <page> <line> <facing>` { #dh-l-setfacing }

> Aliases: `facing`, `face`
> 
> Set the rotation of hologram line facing (Yaw).
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.
> - `#!command <facing>` - Angle of rotation in degrees, or a cardinal direction (`NORTH`, `EAST`, `SOUTH` or `WEST`).

### `#!command /dh l setpermission <hologram> <page> <line> [permission]` { #dh-l-setpermission }

> Aliases: `permission`, `setperm`, `perm`
> 
> Set the current permission required to view the hologram line.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line>` - Index of the line.
> - `#!command [permission]` - New permission. (Leave empty to remove)

### `#!command /dh l align <hologram> <page> <line1> <line2> {X|Z|XZ}` { #dh-l-align }

> Align two lines in a hologram on the specified axis.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <page>` - Index of the page, on which the line is.
> - `#!command <line1>` - Index of the first line.
> - `#!command <line2>` - Index of the second line.
> - `#!command {X|Z|XZ}` - Align `#!command <line1>` with `#!command <line2>` on either the X, Z or both axis.