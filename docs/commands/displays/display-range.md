---
title: '/dh displays display-range'
description: 'Sets the range a Display Entity should be visible from'
---

The `display-range` subcommand sets the max range a player can be from the Display Entity to still see it.

/// warning | The client's and server's entity render distance may influence this.
///

{{ permissions("displays", "displayrange") }}

{{ aliases(["displayrange"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to set the display range of.

### `#!command <range>`

The range in blocks to set.  
Allowed values are between 1 and 256.