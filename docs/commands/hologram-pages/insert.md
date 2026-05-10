---
title: '/dh pages insert'
description: 'Insert a Page into a Hologram'
---

The `insert` subcommand allows to insert a page into a Hologram at the position of the specified page.  
The specified page and any after it are moved back in the list.

{{ permissions("pages", "insert") }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to insert a new page into.

### `#!command <page>`

Page in the Hologram to insert a new page at.

### `#!command [content]`

Optional content to have for the page's first line.  
If left empty uses the `defaults.text` value from the config.yml.