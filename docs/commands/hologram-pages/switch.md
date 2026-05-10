---
title: '/dh pages switch'
description: 'Switches to a different page (for another player)'
---

The `switch` subcommand allows to switch to a different Hologram page.  
This can be done for a specific player too.

/// warning
Can only be executed by a player, if no player argument is provided!
///

{{ permissions("pages", "switch") }}

{{ aliases(["go", "view"]) }}

## Arguments

### `#!command <hologram>`

Name of the Hologram to switch a page of.

### `#!command <page>`

Page in the Hologram to switch to.

### `#!command [player]`

The player to switch the page for.  
If not specified, uses the command executor.