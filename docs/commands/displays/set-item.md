---
title: '/dh displays set-item'
description: 'Sets the item to display'
---

The `set-item` subcommand sets the Item to display for the Display Entity.

/// warning | This command only works for Item Display Entities!
///

{{ permissions("displays", "setitem") }}

{{ aliases(["setitem", "item"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to set the item of.

### `#!command <item>`

The Item to set. Needs to be a valid Item ID in the format `namespace:id` (i.e. `minecraft:dirt`).