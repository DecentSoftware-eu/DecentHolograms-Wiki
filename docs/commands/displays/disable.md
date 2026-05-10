---
title: '/dh displays disable'
description: 'Disables a Display Entity'
---

The `disable` subcommand disables a Display Entity.  
A disabled Display Entity won't be visible for any player, but still exists as a file in the server to [re-enable](enable.md).

To fully remove a Display Entity, use [`/dh displays delete`](delete.md).

{{ permissions("displays", "disable") }}

## Arguments

### `#!command <name>`

Name of the Display entity to disable.