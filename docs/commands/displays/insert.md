---
title: '/dh displays insertline'
description: 'Inserts a new line into a Text Display Entity'
---

The `insertline` subcommand inserts a new Text line into the Display Entity at the specified Line number.  
The current line at the specified number and any other following it are moved downwards.

/// warning | This command only works for Text Display Entities!
///

{{ permissions("displays", "text.insertline") }}

## Arguments

### `#!command <name>`

Name of the Display entity to insert a line to.

### `#!command <index>`

The Line number where to add a line into.

### `#!command <text>`

Text line to insert.