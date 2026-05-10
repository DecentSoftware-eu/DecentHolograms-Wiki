---
title: '/dh displays update-interval'
description: 'Changes the Update Interval of a Display Entity'
---

The `update-interval` subcommand changes the frequency at which a Display Entity updates its content.

{{ permissions("displays", "updateinterval") }}

{{ aliases(["updateinterval"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to change the update interval of.

### `#!command <interval>`

Interval in ticks to set. 20 ticks is 1 second.