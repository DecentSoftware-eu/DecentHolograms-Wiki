---
title: '/dh convert'
description: 'Converts Holograms from one plugin to DecentHolograms'
---

The `convert` command allows to convert existing Holograms from other plugins to DecentHolograms.  
For a List of convertable Plugin Holograms, see the Compatability page.

{{ permissions("convert") }}

## Arguments

### `#!command <plugin>`

The Plugin to convert its holograms from.  
Note that the plugin itself does not need to be on the Server. Only their Hologram file(s) needs to be present.

### `#!command [file]`

Optional path of the file that stores the hologram(s).  
This is only required when the actual file is stored on a different location than usual.

If not specified will DecentHolograms use specific default values.  
See the Compatability page for the default locations per plugin.