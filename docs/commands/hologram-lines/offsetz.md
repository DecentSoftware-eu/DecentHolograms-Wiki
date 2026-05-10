---
title: '/dh lines offsetz'
description: 'Sets the Z offset of the line'
---

The `offsetz` subcommand allows to change the offset of the line on the Z-axis.  
This is useful for situations where multiple lines are on the same height and you want to space them out vertically.

{{ permissions("lines", "offsetz") }}

{{ aliases(["offz", "zoff", "zoffset"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to change a line's Z-offset in.

### `#!command <page>`

Page in the Hologram to change a line's Z-offset in.

### `#!command <line>`

Line number to change the Z-offset of.

### `#!command <offset>`

Offset in blocks on the Z-axis of the line.  
The value can be between -2.5 and 2.5 inclusive with 0 being centered on the Hologram.