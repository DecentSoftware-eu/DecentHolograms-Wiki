---
title: '/dh displays set-facing'
description: 'Sets the facing angle of the Display Entity'
---

The `set-facing` subcommand sets the facing angle of the Display entity.

{{ permissions("displays", "facing") }}

{{ aliases(["setfacing", "facing", "face"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to change the facing angle of.

### `#!command <yaw>`

The Yaw (rotation on the vertical axis) the entity should have.  
Allowed values are between -180 and 180 inclusive, with (-)180 being facing towards north.

### `#!command [pitch]`

Optional Pitch (rotation on the horizontal axis) the entity should have.  
Allowed values are between -90 and 90 inclusive with 0 being facing straight forward.

If not set, defaults to the Entity's current Pitch.s