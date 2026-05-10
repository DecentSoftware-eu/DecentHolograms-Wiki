---
title: '/dh hologram align'
description: 'Aligns the Hologram with another one'
---

The `align` subcommand allows you to align the Hologram with another one on a specified axis or angle.

{{ permissions("hologram", "align") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to align.

### `#!command {X|Y|Z|XZ|FACING}`

Sets on what axis to align the hologram with the other.  
If `FACING` is used will the hologram instead have all its (small) heads and Entities adjusted to face the same direction as the other hologram.

### `#!command <otherHologram>`

Name of the other Hologram to align this one to.