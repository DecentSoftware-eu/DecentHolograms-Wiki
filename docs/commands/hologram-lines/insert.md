---
title: '/dh lines insert'
description: 'Inserts a line before others.'
---

The `insert` subcommand inserts a new line at the location of the provided line index.  
The provided line and any line after are moved downwards.

{{ permissions("lines", "insert") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to insert a line into.

### `#!command <page>`

Page in the Hologram to insert a line into.

### `#!command <line>`

Line number to insert the new line into.

### `#!command [content]`

Optional Line content to use.  
If not set uses the `defaults.text` value from the config.yml.