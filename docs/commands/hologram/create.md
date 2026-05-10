---
title: '/dh hologram create'
description: 'Creates a new Hologram'
---

The `create` subcommand allows you to create a new Hologram.

{{ permissions("hologram", "create") }}

{{ aliases(["c"]) }}

## Arguments

### `#!command <name>`

Name of the Hologram to have.

### `#!command [-l:<world>:<x>:<y>:<z>]`

Optional Location argument to specify a world and the X, Y and Z location of the Hologram.

/// warning
This argument is required when the subcommand is executed from the server console.
///

### `#!command [--center]`

Optional argument to have the Hologram centered on the Block

### `#!command [content]`

Optional argument to set the text that is displayed when creating the hologram.  
Defaults to the `defaults.text` config value when not specified.

/// note
Any content that does not match `#!command -l:<world>:<x>:<y>:<z>` or `--center` will be seen as Line content.
///

## Examples

```
/dh h create test
/dh h create test -l:world:0:100:0
/dh h create test First Line
/dh h create test -l:world:0:100:0 First Line
/dh h create test --center
```