---
title: Features
description: General usage of special features for a hologram
---

--8<-- "arguments.md"

## Commands

**Aliases:** `feature`, `f`  
**Permission:** `dh.command.features`

/// info | Command help
For a list of all available subcommands run the following command:  
```
/dh f help
```
///

----

### `#!command /dh f disable <feature>` { #dh-f-disable }

:   **Aliases:** `off`  
    **Permission:** `dh.command.features.disable`
    
    Disables a Feature.
    
    - `#!command <feature>` - The feature to disable.

----

### `#!command /dh f enable <feature>` { #dh-f-enable }

:   **Aliases:** `on`  
    **Permission:** `dh.command.features.enable`
    
    Enables a Feature.
    
    - `#!command <feature>` - The feature to enable.

----

### `#!command /dh f info <feature>` { #dh-f-info }

:   **Permission:** `dh.command.features.info`
    
    Gives information about a specific feature.
    
    - `#!command <feature>` - The feature to retrieve infos about.

----

### `#!command /dh f list` { #dh-f-list }

:   **Permission:** `dh.command.features.list`
    
    Lists all available features.

----

### `#!command /dh f reload <feature>` { #dh-f-reload }

:   **Permission:** `dh.command.features.reload`
    
    Reloads a specific feature.
    
    - `#!command <feature>` - The feature to reload.