---
title: '/dh lines setpermission'
description: 'Sets a permission for a Line'
---

The `setpermission` subcommand sets a permission for a Hologram line.  
When a permission is set can only players with said permission see the line.

{{ permissions("lines", "setpermission") }}

{{ aliases(["perm", "permission", "setperm"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to set a line's permission.

### `#!command <page>`

Page in the Hologram to set a line's permission.

### `#!command <line>`

Line number to set its permission.

### `#!command [permission]`

Optional permission to set.  
If left empty, removes any set permission.