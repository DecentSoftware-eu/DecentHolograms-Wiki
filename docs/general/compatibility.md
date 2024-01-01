---
title: Compatibility
description: List of compatible (hologram) plugins and how to migrate from them

icon: material/link-variant
---

## PlaceholderAPI

DecentHolograms fully supports PlaceholderAPI (PAPI) and its placeholders can be used in various parts of the plugin such as hologram lines, actions and animations.

/// info | Placeholders in animations
By default are placeholders inside animations not parsed to reduce possible performance issues.  
To allow placeholders to be parsed, enable `allow-placeholders-inside-animations` in the `config.yml` of DecentHolograms.
///

## Hologram conversion

DecentHolograms supports the conversion of Holograms from other hologram plugins to itself.  
Below is a list of all currently supported plugins, the command you have to use and notes on how DecentHologram will treat specific cases.

/// note
The plugins **do not** have to be enabled to allow a conversion. Only their Hologram file needs to be present in their default location.
///

### CMI

> ```
> /dh convert CMI
> ```

Special actions:

- :octicons-check-16: `#!command ICON:<item>` is converted to `#!command #ICON:<item>`
- :octicons-check-16: `!nextpage!` reates a new page
- :octicons-alert-16: Holograms with names that start with `#<` or `#>` will be skipped.

### FutureHolograms

> ```
> /dh convert FutureHolograms
> ```

Special Actions:

- :octicons-alert-16: No notable Actions outside basic Hologram conversion.

### GHolo

> ```
> /dh convert GHolo
> ```

Special Actions:

- :octicons-check-16: `#!command ICON:<item>` is converted to `#!command #ICON:<item>`
- :octicons-check-16: `#!command ENTITY:<entity>` is converted to `#!command #ENTITY:<entity>`
- :octicons-check-16: `[x]`, `[X]` and `[|]` are converted into their respective unicode characters.
- :octicons-check-16: `#!command [#rrggbb text #rrggbb]` is converted to `#!command <#rrggbb>text</#rrggbb>`

### Holograms

> ```
> /dh convert Holograms
> ```

Special Actions:

- :octicons-check-16: `#!command ITEM:<item>` is converted to `#!command #ICON:<item>`

### HolographicDisplays

> ```
> /dh convert HolographicDisplays
> ```

Special Actions:

- :octicons-check-16: `#!command ICON:<item>` is converted to `#!command #ICON:<item>`
- :octicons-check-16: `#!command {papi: <placeholder>}` is converted to `#!command %<placeholder>%`
- :octicons-check-16: `#!command {empty}` is converted into an empty Hologram line using a color code.