---
title: Hologram Pages
description: General usage and editing of hologram pages
---

--8<-- "arguments.md"

## Commands

**Aliases:** `page`, `p`  
**Permission:** `dh.command.pages`

/// info | Command help
For a list of all available subcommands run the following command:  
```
/dh p help
```
///

----

### `#!command /dh p actions <hologram> <page> <clickType> [listPage]` { #dh-p-actions }

:   **Permission:** `dh.command.pages.actions`
    
    View actions set on the specified [Click type](../actions.md#click-types) in page of a hologram.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page>` - Index of the page.
    - `#!command <clickType>` - [Click type](../actions.md#click-types).
    - `#!command [listPage]` - Optional page in the list to move to.
   
----

### `#!command /dh p add <hologram> [content]` { #dh-p-add }

:   **Aliases:** `append`  
    **Permission:** `dh.command.pages.add`
    
    Add a new page into hologram.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command [content]` - Optional [Content](../format-and-colors/index.md) of the first line in the new page. Defaults to the [`defaults.text` config option](../configuration/config.md).

----

### `#!command /dh p addaction <hologram> <page> <clickType> <action>` { #dh-p-addaction }

:   **Permission:** `dh.command.pages.addaction`
    
    Adds the specified [`<action>`](../actions.md) for the specified `#!command <clickType>` to a hologram page.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page>` - Index of the page.
    - `#!command <clickType>` - [Click type](../actions.md#click-types) that triggers this action.
    - `#!command <action>` - [Action](../actions.md#action-types) to trigger.

----

### `#!command /dh p clearactions <hologram> <page> <clickType>` { #dh-p-clearactions }

:   **Permission:** `dh.command.pages.clearactions`
    
    Clears `#!command <page>` of all [Actions](../actions.md) specified for `#!command <clickType>`.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page>` - Index of the page.
    - `#!command <clickType>` - [Click type](../actions.md#click-types).

----

### `#!command /dh p insert <hologram> <page> [content]` { #dh-p-insert }

:   **Permission:** `dh.command.pages.insert`
    
    Insert a new page into hologram.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page>` - Position of the page to insert the new one before.
    - `#!command [content]` - Optional [Content](../format-and-colors/index.md) of the first line in the new page. Defaults to the [`defaults.text` config option](../configuration/config.md).

----

### `#!command /dh p remove <hologram> <page>` { #dh-p-remove }

:   **Aliases:** `del`, `delete`, `rem`  
    **Permission:** `dh.command.pages.remove`
    
    Remove a page from hologram.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page>` - Index of the page to remove.

----

### `#!command /dh p removeaction <hologram> <page> <clickType> <index>` { #dh-p-removeaction }

:   **Aliases:** `remaction`  
    **Permission:** `dh.command.pages.removeaction`
    
    Removes an [Action](../actions.md) for `#!command <clickType>` from `#!command <page>`.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page>` - Index of the page.
    - `#!command <clickType>` - [Click type](../actions.md#click-types) that triggers this action.
    - `#!command <index>` - Index of the action in the list.

----

### `#!command /dh p swap <hologram> <page1> <page2>` { #dh-p-swap }

:   **Permission:** `dh.command.pages.swap`
    
    Swaps `#!command <page1>` with `#!command <page2>`.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page1>` - Index of the first page.
    - `#!command <page2>` - Index of the second page.

----

### `#!command /dh p switch <hologram> <page> [player]` { #dh-p-switch }

:   **Aliases:** `go`, `view`  
    **Permission:** `dh.command.pages.switch`
    
    Switch to another page in a hologram.
    
    - `#!command <hologram>` - Name of the hologram.
    - `#!command <page>` - Index of the page to view.
    - `#!command [player]` - Optional player to switch the page for. Defaults to command executor if not set.