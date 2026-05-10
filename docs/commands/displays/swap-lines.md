---
title: '/dh displays swap-lines'
description: 'Swaps two lines in a Text Display Entity'
---

The `swap-lines` subcommand switches the position of the first specified line with the second one.

/// warning | This command only works for Text Display Entities!
///

{{ permissions("displays", "text.swaplines") }}

{{ aliases(["swaplines"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to swap lines in.

### `#!command <line1>`

The first line to swap.

### `#!command <line2>`

The second line to swap.