---
title: '/dh displays delete'
description: 'Deletes a Display Entity'
---

The `delete` subcommand removes a Display Entity.  
This **permanently** removes the Display Entity, including its configuration file.

To only hide a Display Entity, use [`/dh displays disable`](disable.md).

{{ permissions("displays", "delete") }}

{{ aliases(["del"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to remove.