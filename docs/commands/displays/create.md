---
title: '/dh displays create'
description: 'Creates a new Display Entity'
---

The `create` subcommand creates a new Text, item or Block entity.

{{ permissions("displays", "create") }}

{{ aliases(["new", "c"]) }}

## Arguments

### `#!command <type>`

The type for the display entity to have.  
Supported types are `TEXT`, `ITEM` and `BLOCK`.

Based on the provided type can the content only accept specific values.

### `#!command <name>`

Name of the Display entity to have.

### `#!command [content]`

Optional content for the Display Entity to start with.  
Depending on the type defined will this option accept either any text, or specific item/block values.