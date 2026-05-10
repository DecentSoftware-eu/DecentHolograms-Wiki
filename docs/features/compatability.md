---
title: 'Compatability'
description: 'Plugin support in DecentHolograms'

icon: material/connection
---

DecentHolograms provides support for specific plugins. This can be support for basic features, or the ability to convert their holograms into DecentHolograms.

## Plugin Support

The following plugins are supported in DecentHolograms.

### PlaceholderAPI

DecentHolograms supports all placeholders from [PlaceholderAPI](https://modrinth.com/plugin/placeholderapi){ target="_blank" rel="noopener" }.  
Placeholders can be used using their default `%identfier_values%` format (i.e. `%player_name%`) in Hologram Lines, actions and Animations.

Placeholders are parsed with the player viewing the Hologram.

/// info | Placeholders in animations
By default are placeholders in custom animations not parsed, to avoid performance issues.  
If you still want them to be parsed, enable `allow-placeholders-inside-animations` in the `config.yml` of DecentHolograms.
///

## Hologram Conversion

DecentHologram provides support for converting Holograms from the following Holograms.

/// warning | Support may be limited.
///

### CMI

```
/dh convert CMI
```

**Default File Location:** `plugins/CMI/holograms.yml`

**Special Actions:**

- :octicons-check-16:{ .md-icon-color--success } `#!command ICON:<item>` gets converted to `#!command #ICON:<item>`
- :octicons-check-16:{ .md-icon-color--success } `!nextpage!` creates a new Hologram Page.
- :octicons-alert-16:{ .md-icon-color--warning } Holograms with names that start with `#<` or `#>` will be skipped

### FutureHolograms

```
/dh convert FutureHolograms
```

**Default File Location:** `plugins/FutureHolograms/holograms.yml`

**Special Actions:**

- :octicons-alert-16:{ .md-icon-color--warning } No notable actions outside basic Hologram conversion.

### GHolo

```
/dh convert GHolo
```

**Default File Location:** `plugins/GHolo/data/h.data`

**Special Actions:**

- :octicons-check-16:{ .md-icon-color--success } `#!command ICON:<item>` gets converted to `#!command #ICON:<item>`
- :octicons-check-16:{ .md-icon-color--success } `#!command ENTITY:<entity>` gets converted to `#!command #ENTITY:<entity>`
- :octicons-check-16:{ .md-icon-color--success } `[x]`, `[X]` and `[|]` get converted into Unicde characters
- :octicons-check-16:{ .md-icon-color--success } <code class="highlight"><span class="p">[</span><span class="nt">#rrggbb</span> text <span class="nt">#rrggbb</span><span class="p">]</span></code>
  gets converted to
  <code class="highlight"><span class="p"><</span><span class="nt">#rrggbb</span><span class="p">></span>text<span class="p"><</span><span class="nt">/#rrggbb</span><span class="p">></span></code>

### Holograms

:   
    ```
    /dh convert Holograms
    ```
    
    **Default File Location:** `plugins/Holograms/holograms.yml`
    
    **Special Actions:**
    
    - :octicons-check-16:{ .md-icon-color--success } `#!command ITEM:<item>` gets converted to `#!command #ICON:<item>`

### HolographicDisplays

```
/dh convert HolographicDisplays
```

**Default File Location:** `plugins/HolographicDisplays/database.yml`

**Special Actions:**

- :octicons-check-16:{ .md-icon-color--success } `#!command ICON:<item>` gets converted to `#!command #ICON:<item>`
- :octicons-check-16:{ .md-icon-color--success } `#!command {papi: <placeholder>}` gets converted to `%<placeholder>%`
- :octicons-check-16:{ .md-icon-color--success } `#!command {empty}` creates an empty line using a color code.