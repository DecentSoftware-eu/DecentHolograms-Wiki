---
title: '/dh lines setfacing'
description: 'Sets the facing angle of a Line'
---

The `setfacing` subcommand allows to change the facing angle of a line.

/// note
This command has no influence on text-lines!
///

{{ permissions("lines", "setfacing") }}

{{ aliases(["facing", "face"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to change the line's facing angle of.

### `#!command <page>`

Page in the Hologram to change the line's facing angle of.

### `#!command <line>`

Line number to change the facing angle.

### `#!command <facing>`

The facing angle of the line. Can be a number between -180 and 180, or `NORTH`, `EAST`, `SOUTH` or `WEST`.