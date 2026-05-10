---
title: '/dh hologram setfacing'
description: 'Sets the direction in which heads and entities should look'
---

The `setfacing` subcommand sets the direction in which (small) heads and entities should be facing.

/// note
This command has no influence on text-lines!
///

{{ permissions("hologram", "setfacing") }}

{{ aliases(["facing", "face", "setface"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to change the facing angle of.

### `#!command <facing>`

The direction the (small) head or entity should face.  
Supported values are numbers between -180 and 180 or `NORTH`, `EAST`, `SOUTH` or `WEST`.