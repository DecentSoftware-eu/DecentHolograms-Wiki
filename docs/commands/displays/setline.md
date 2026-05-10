---
title: '/dh displays setline'
description: 'Sets a line in the Text Display Entity'
---

The `setline` subcommand sets the content of the specified line in a Display Entity.

/// warning | This command only works for Text Display Entities!
///

{{ permissions("displays", "text.setline") }}

## Arguments

### `#!command <name>`

Name of the Display entity to set the line of.

### `#!command <index>`

Position of the Line to edit.

### `#!command <text>`

New text for the line to have.