---
title: '/dh lines offsetx'
description: 'Sets the X offset of the line'
---

The `offsetx` subcommand allows to change the offset of the line on the X-axis.  
This is useful for situations where multiple lines are on the same height and you want to space them out vertically.

{{ permissions("lines", "offsetx") }}

{{ aliases(["offx", "xoff", "xoffset"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to change a line's X-offset in.

### `#!command <page>`

Page in the Hologram to change a line's X-offset in.

### `#!command <line>`

Line number to change the X-offset of.

### `#!command <offset>`

Offset in blocks on the X-axis of the line.  
The value can be between -2.5 and 2.5 inclusive with 0 being centered on the Hologram.