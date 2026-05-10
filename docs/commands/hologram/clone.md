---
title: '/dh hologram clone'
description: 'Clones a Hologram'
---

The `clone` subcommand allows to (temporarely) clone a Hologram, including all its lines, actions, etc.

{{ permissions("hologram", "clone") }}

{{ aliases(["copy"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to copy.

### `#!command <name>`

Name of the copy to have.

### `#!command [temp]`

Optional boolean to mark the clone as temporary.  
A Temporary Hologram will not be saved to file and won't exist anymore after a server reload.

### `#!command [-l:<world>:<x>:<y>:<z>]`

Optional Location argument to set the Holograms world, X, Y and Z position.

/// warning
This argument is required when executing this subcommand from the console.
///

## Examples

```
/dh h clone test test_clone true
/dh h clone test test_clone -l:world:0:100:0
/dh h clone test test_clone true -l:world:0:100:0
```