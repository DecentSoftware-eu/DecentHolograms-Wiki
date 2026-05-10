---
title: '/dh pages remove'
description: 'Removes a page from a Hologram'
---

The `remove` subcommand removes the specified page from the Hologram.  
Any pages that were listed after it are moved one up in the list.

{{ permissions("pages", "remove") }}

{{ aliases(["del", "delete", "rem"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to remove a page from.

### `#!command <page>`

Page in the Hologram to remove.