---
title: '/dh hologram downorigin'
description: 'Sets the downorigin of a Hologram'
---

The `downorigin` subcommand is used to enable/disable a Hologram's downorigin setting.  
When enabled will a Holograms anchor point be set to the bottom. This results in any text added moving the hologram up, rather than expanding it downwards.

{{ permissions("hologram", "downorigin") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to change the downorigin of.

### `#!command {true|false}`

Whether to enable or disable the Downorigin of the hologram.