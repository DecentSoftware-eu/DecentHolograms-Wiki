---
title: Hologram Line
description: General usage and editing of hologram lines
---

--8<-- "arguments.md"

## Commands

**Aliases:** `line`, `l`  
**Permission:** `dh.command.lines`

/// info | Command help
For a list of all available subcommands run the following command:  
```
/dh l help
```
///

----

### `#!command /dh l add <hologram> <page> [content]` { #dh-l-add }

:   **Aliases:** `append`  
    **Permission:** `dh.command.lines.add`
    
    Add a new line into hologram.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line should be.
    - `#!command [content]` - Optional [Content](../format-and-colors/index.md) of the new line. Defaults to the [`defaults.text` config option](../configuration/config.md).

----

### `#!command /dh l addflag <hologram> <page> <line> <flag>` { #dh-l-addflag }

:   **Permission:** `dh.command.lines.addflag`
    
    Adds a [flag](../flags.md) to a hologram line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command <flag>` - Name of the [Flag](../flags.md) to add.

----

### `#!command /dh l align <hologram> <page> <line1> <line2> {X|Z|XZ|FACING}` { #dh-l-align }

  
:   **Permission:** `dh.command.lines.align`
    
    Aligns `#!command <line1>` with `#!command <line2>` on the specified axis or facing angle.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line1>` - Index of the first line.
    - `#!command <line2>` - Index of the second line.
    - `#!command {X|Z|XZ|FACING}` - Align `#!command <line1>` with `#!command <line2>` on either the X, Z, or X and Z axis, or sets its facing angle to that of `#!command <line2>`.

----

### `#!command /dh l edit <hologram> <page> <line>` { #dh-l-edit }

:   **Aliases:** `e`  
    **Permission:** `dh.command.lines.edit`
    
    Gives you a chat message to click on to get a pre-made command to edit the specified line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.

----

### `#!command /dh l height <hologram> <page> <line> <height>` { #dh-l-height }

:   **Aliases:** `setheight`  
    **Permission:** `dh.command.lines.height`
    
    Set the height of a line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command <height>` - Number between `0.0` and `2.5` to set the line height.

----

### `#!command /dh l info <hologram> <page> <line>` { #dh-l-info }

:   **Permission:** `dh.command.lines.info`
    
    Display some general info about a hologram line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.

----

### `#!command /dh l insert <hologram> <page> <line> [content]` { #dh-l-insert }

:   **Permission:** `dh.command.lines.insert`
    
    Insert a new line into hologram at the position of the given line number.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command [content]` - Optional [Content](../format-and-colors/index.md) of the new line. Defaults to the [`defaults.text` config option](../configuration/config.md).

----

### `#!command /dh l offsetx <hologram> <page> <line> <offset>` { #dh-l-offsetx }

:   **Aliases:** `offx`, `xoff`, `xoffset`  
    **Permission:** `dh.command.lines.offsetx`
    
    Set the X offset of a hologram line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command <offset>` - Number between `-2.5` and `2.5` to set the X offset of a line.

----

### `#!command /dh l offsetz <hologram> <page> <line> <offset>` { #dh-l-offsetz }

:   **Aliases:** `offz`, `zoff`, `zoffset`  
    **Permission:** `dh.command.lines.offsetz`
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command <offset>` - Number between `-2.5` and `2.5` to set the Z offset of a line.

----

### `#!command /dh l remove <hologram> <page> <line>` { #dh-l-remove }

:   **Aliases:** `del`, `delete`, `rem`  
    **Permission:** `dh.command.lines.remove`
    
    Remove a line from hologram.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.

----

### `#!command /dh l removeflag <hologram> <page> <line> <flag>` { #dh-l-removeflag }

:   **Permission:** `dh.command.lines.removeflag`
    
    Removes a [flag](../flags.md) from a hologram line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command <flag>` - Name of the [Flag](../flags.md) you want to remove.

----

### `#!command /dh l set <hologram> <page> <line> <content>` { #dh-l-set }

:   **Permission:** `dh.command.lines.set`
    
    Set a new content to hologram line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command <content>` - [Content](../format-and-colors/index.md) of a line.

----

### `#!command /dh l setfacing <hologram> <page> <line> <facing>` { #dh-l-setfacing }

:   **Aliases:** `facing`, `face`  
    **Permission:** `dh.command.lines.setfacing`
    
    Set the rotation of hologram line facing (Yaw). This only has an effect on `#HEAD:`, `#SMALLHEAD:` and `#ENTITY:` content lines.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command <facing>` - Number between `-180.0` and `180.0` for a specific angle, or a cardinal direction (`NORTH`, `EAST`, `SOUTH` or `WEST`).

----

### `#!command /dh l setpermission <hologram> <page> <line> [permission]` { #dh-l-setpermission }

:   **Aliases:** `perm`, `permission`, `setperm`  
    **Permission:** `dh.command.lines.setpermission`
    
    Set a permission required to view a hologram line.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the line is.
    - `#!command <line>` - Index of the line.
    - `#!command [permission]` - Permission required for a line to be seen. Leave empty to remove any permission.

----

### `#!command /dh l swap <hologram> <page> <line1> <line2>` { #dh-l-swap }

:   **Permission:** `dh.command.lines.swap`
    
    Swap two lines in a hologram.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Index of the page, on which the lines are.
    - `#!command <line1>` - Index of the first line.
    - `#!command <line2>` - Index of the second line.
