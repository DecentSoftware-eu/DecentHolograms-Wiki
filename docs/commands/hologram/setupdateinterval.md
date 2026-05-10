---
title: '/dh hologram setupdateinterval'
description: 'Sets the interval in which placeholders should update'
---

The `setupdateinterval` subcommand can be used to set the frequency at which a Hologram should update dynamic data such as Placeholders.

{{ permissions("hologram", "setupdateinterval") }}

{{ aliases(["updateinterval"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to change the update interval of.

### `#!command <interval>`

New interval in ticks with 20 ticks being 1 second.  
Can only be between 1 and 1200.