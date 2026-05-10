---
title: '/dh displays set-block'
description: 'Set the displayed block in a Block Display'
---

The `set-block` subcommand sets the block to display in an Display entity.

/// warning | This command only works for Block Display Entities!
///

{{ permissions("displays", "setblock") }}

{{ aliases(["setblock", "block"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to change the block of.

### `#!command <block_type>`

The Block to set. Needs to be a valid Block ID in the format `namespace:id` (i.e. `minecraft:dirt`).