---
title: '/dh hologram setdisplayrange'
description: 'Sets the max range a hologram should be visible from'
---

The `setdisplayrange` subcommand allows to set the max distance from which a hologram should be visible.

/// note
The Hologram display itself is still influenced by the client's and server's entity render distance.
///

{{ permissions("hologram", "setdisplayrange") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to set the display range of.

### `#!command <range>`

The display range (in blocks) to set.