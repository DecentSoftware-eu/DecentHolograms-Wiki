---
title: '/dh displays reset-attribute'
description: 'Resets the provided attribute to its default value'
---

The `reset-attribute` subcommand resets the defined attribute to its default value for the specified Display Entity.  
The value will be reset to whatever has been configured in the attributes-defaults.yml file.

{{ permissions("displays", "resetattribute") }}

{{ aliases(["resetattribute"]) }}

## Arguments

### `#!command <name>`

Name of the Display entity to reset the attribute of.

### `#!command <attribute>`

The attribute to reset.