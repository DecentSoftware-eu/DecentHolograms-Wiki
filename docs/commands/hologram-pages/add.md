---
title: '/dh pages add'
description: 'Adds a new Hologram Page'
---

The `add` subcommand adds a new Hologram page to the Hologram.

{{ permissions("pages", "add") }}

{{ aliases(["append"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to add a new page to.

### `#!command [content]`

Optional content to use for the Hologram Page's first line.  
If left empty uses the `defaults.text` value from the config.yml.