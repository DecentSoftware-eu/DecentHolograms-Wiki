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

The format used for this option depends on the provided `#!command <attribute>`  
Example, using the `billboard` attribute will accept you providing a single String defining the billboard setting, where using `background-color` will require you to provide the color type followed by its values (i.e. `rgba 0 0 0 0` to make it transparent) or named colors including `TRANSPARENT` or `DEFAULT`.

The command suggestions should generally provide you with an idea on what values and options you can provide and use for what attribute.