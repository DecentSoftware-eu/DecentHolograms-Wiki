---
title: General
description: General commands of DecentHolograms
---

## Commands

/// info | Command help
For a list of available subcommands run the following command:
```
/dh help
```
///

----

### `#!command /dh convert <plugin> [file]` { #dh-convert }

> Converts holograms from another hologram plugin.  
> The hologram plugin does not have to be on the server. Only its files!
> 
> - `#!command <plugin>` - The Hologram plugin to convert holograms from. See [this page](../compatibility.md) for a list.
> - `#!command [file]` - Location of the file to convert. Only required if the file is not in the default location of the other plugin.

----

### `#!command /dh list [page]` { #dh-list }

> Lists all holograms loaded from a hologram file.
>
> - `#!command [page]` - Page in the list to move to.

----

### `#!command /dh reload` { #dh-reload }

> Reloads the plugin.

----

### `#!command /dh version` { #dh-version }

> Aliases: `about`, `ver`
> 
> Shows some info about your current DecentHolograms version.