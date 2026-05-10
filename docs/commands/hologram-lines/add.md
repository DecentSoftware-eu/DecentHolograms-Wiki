---
title: '/dh lines add'
description: 'Adds a line to a Hologram page'
---

The `add` subcommand allows to add new lines to a Hologram page.

{{ permissions("lines", "add") }}

{{ aliases(["append"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to add a line to.

### `#!command <page>`

Page in the Hologram to add a line to.

### `#!command [content]`

Line content to add.  
If left empty, defaults to the `defaults.text` value in the config.yml of the plugin.