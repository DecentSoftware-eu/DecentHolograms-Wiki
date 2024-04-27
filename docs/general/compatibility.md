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

/// note | The plugin does not need to be enabled to convert. Only its hologram files are needed.
///

### CMI

:   
    ```
    /dh convert CMI
    ```
    
    **Default File Location:** `plugins/CMI/holograms.yml`
    
    **Special Actions:**
    
    - :octicons-check-16:{ .md-icon-color--success } `#!command ICON:<item>` gets converted to `#!command #ICON:<item>`
    - :octicons-check-16:{ .md-icon-color--success } `!nextpage!` creates a new Hologram Page.
    - :octicons-alert-16:{ .md-icon-color--warning } Holograms with names that start with `#<` or `#>` will be skipped

### FutureHolograms

:   
    ```
    /dh convert FutureHolograms
    ```
    
    **Default File Location:** `plugins/FutureHolograms/holograms.yml`
    
    **Special Actions:**
    
    - :octicons-alert-16:{ .md-icon-color--warning } No notable actions outside basic Hologram cinversion.

### GHolo

:   
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

:   
    ```
    /dh convert HolographicDisplays
    ```
    
    **Default File Location:** `plugins/HolographicDisplays/database.yml`
    
    **Special Actions:**
    
    - :octicons-check-16:{ .md-icon-color--success } `#!command ICON:<item>` gets converted to `#!command #ICON:<item>`
    - :octicons-check-16:{ .md-icon-color--success } `#!command {papi: <placeholder>}` gets converted to `%<placeholder>%`
    - :octicons-check-16:{ .md-icon-color--success } `#!command {empty}` creates an empty line using a color code.