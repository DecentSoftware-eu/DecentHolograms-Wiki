---
title: '/dh lines align'
description: 'Aligns a Hologram line with another'
---

The `align` subcommand allows to align a hologram line with another on the X and/or Z axis, or change the facing angle.

{{ permissions("lines", "align") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to align lines in.

### `#!command <page>`

Page in the Hologram to align lines in.

### `#!command <line1>`

Number of the line to align with the second.

### `#!command <line2>`

Number of the second line to align the first one with.

### `#!command {X|Z|XZ|FACING}`

Whether to align line 1 with line 2 on the X and/or the Z axis, or to instead match the facing angle.