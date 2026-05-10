---
title: '/dh hologram center'
description: 'Centers the hologram on a Block'
---

The `center` subcommand can be used to have the Hologram be centered on a block.

When centering the Hologram does DecentHologram take the location, remove any decimals and then eithe add or subtract `0.5` to/from it based on if the truncated number is smaller or larger than the original.

{{ permissions("hologram", "center") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to center.