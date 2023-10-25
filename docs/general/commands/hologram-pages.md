---
title: Hologram Pages
subtitle: General usage and editing of hologram pages
---

## Commands

> Aliases: `page`, `p`

/// info | Command help
For a list of all available subcommands run the following command:  
```
/dh p help
```
///

### `#!command /dh p add <hologram> [content]` { #dh-p-add }

> Add a new page into hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command [content]` - [Content](../format-and-colors/index.md) of the first line.

### `#!command /dh p insert <hologram> <index>` { #dh-p-insert }

> Insert a new page into hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <index>` - Index of the new page.

### `#!command /dh p remove <hologram> <page>` { #dh-p-remove }

> Remove a page from hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <page>` - Index of the page to remove.

### `#!command /dh p swap <hologram> <page1> <page2>` { #dh-p-swap }

> Swap two pages in a hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <page1>` - Index of the first page.
> - `#!command <page2>` - Index of the second page.

### `#!command /dh p switch <hologram> <page>` { #dh-p-switch }

> Switch to another page in a hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <page>` - Index of the page to view.

### `#!command /dh p addaction <hologram> <page> <clickType> <actipn>` { #dh-p-addaction }

> Add [action](../actions.md) to a page of a hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <page>` - Index of the page.
> - `#!command <clickType>` - [Click type](../actions.md#click-types) that triggers this action.
> - `#!command <action>` - [Action](../actions.md#action-types) to trigger.

### `#!command /dh p removeaction <hologram> <page> <clickType> <index>` { #dh-p-removeaction }

> Remove [action](../actions.md) from a page of a hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <page>` - Index of the page.
> - `#!command <clickType>` - [Click type](../actions.md#click-types) that triggers this action.
> - `#!command <index>` - Index of the action.

### `#!command /dh p clearactions <hologram> <page> <clickType>` { #dh-p-clearactions }

> Clear [actions](../actions.md) on specified click type in page of a hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <page>` - Index of the page.
> - `#!command <clickType>` - [Click type](../actions.md#click-types).

### `#!command /dh p actions <hologram> <page> <clickType>` { #dh-p-actions }

> View actions set on the specified [Click type](../actions.md#click-types) in page of a hologram.
> 
> - `#!command <hologram>` - Name of the hologram.
> - `#!command <page>` - Index of the page.
> - `#!command <clickType>` - [Click type](../actions.md#click-types).