---
title: '/dh hologram setupdaterange'
description: 'Sets the max distance in which holograms update'
---

The `setupdaterange` subcommand sets the max distance in which dynamic data such as Placeholders update.

{{ permissions("hologram", "setupdaterange") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to change the update range of.

### `#!command <range>`

Distance in blocks in which a hologram should update for a player.  
Can be between 1 and 64.