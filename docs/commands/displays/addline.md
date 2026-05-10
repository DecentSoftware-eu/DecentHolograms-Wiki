---
title: '/dh displays addline'
description: 'Adds a Line to a Text Display Entity'
---

The `addline` subcommand adds a new Line to a Display Entity.

/// warning | This command only works for Text Display Entities!
///

{{ permissions("displays", "text.addline") }}

{{ aliases(["appendline"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to add a new line to.

### `#!command <text>`

New Text line to add.