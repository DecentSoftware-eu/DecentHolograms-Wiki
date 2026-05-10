---
title: '/dh displays attribute'
description: 'Sets or gets attributes'
---

The `attribute` subcommand is used to get or set different Attributes for the Display Entity.

{{ permissions("displays", "attribute") }}

## Arguments

### `#!command <name>`

Name of the Display entity to get or set attributes of.

### `#!command <attribute>`

Name of the attribute to get or set.

### `#!command [value]`

Optional values to set for the attribute.  
If left empty, returns the currently set attribute values, if any.