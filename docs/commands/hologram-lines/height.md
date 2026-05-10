---
title: '/dh lines height'
description: 'Sets the line height'
---

The `height` subcommand is used to set the height of a Hologram line.  
The height determines the distance between the line and any previous one above it.

{{ permissions("lines", "height") }}

{{ aliases(["setheight"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to set the height of a line.

### `#!command <page>`

Page in the Hologram to set the height of a line.

### `#!command <line>`

Line number to change its height of.

### `#!command <height>`

Height in blocks to set.  
Allowed values are between 0 and 2.5 inclusive.