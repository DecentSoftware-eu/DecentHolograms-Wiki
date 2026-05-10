---
title: '/dh displays removeline'
description: 'Removes a Line from a Text Display Entity'
---

The `removeline` subcommand removes a line from a Display Entity.  
Any lines after the specified one are moved up by one.

/// warning | This command only works for Text Display Entities!
///

{{ permissions("displays", "text.removeline") }}

{{ aliases(["remline"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to remove a line from.

### `#!command <index>`

Position of the line to remove.