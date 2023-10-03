---
title: Hologram Pages
subtitle: General usage and editing of hologram pages
---

## Commands

> Aliases: `page`, `p`

You can simply view all commands for hologram pages using the following command:

> ```
> /dh pages help
> ```

### `#!html /dh p add <hologram> [content]` { #dh-p-add }

Add a new page into hologram.

- `#!html <hologram>` - Name of the hologram.
- `[content]` - [Content](../format-and-colors/index.md) of the first line.

### `#!html /dh p insert <hologram> <index>` { #dh-p-insert }

Insert a new page into hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <index>` - Index of the new page.

### `#!html /dh p remove <hologram> <page>` { #dh-p-remove }

Remove a page from hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <page>` - Index of the page to remove.

### `#!html /dh p swap <hologram> <page1> <page2>` { #dh-p-swap }

Swap two pages in a hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <page1>` - Index of the first page.
- `#!html <page2>` - Index of the second page.

### `#!html /dh p switch <hologram> <page>` { #dh-p-switch }

Switch to another page in a hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <page>` - Index of the page to view.

### `#!html /dh p addaction <hologram> <page> <clickType> <actipn>` { #dh-p-addaction }

Add [action](../actions.md) to a page of a hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <page>` - Index of the page.
- `#!html <clickType>` - [Click type](../actions.md#click-types) that triggers this action.
- `#!html <action>` - [Action](../actions.md#action-types) to trigger.

### `#!html /dh p removeaction <hologram> <page> <clickType> <index>` { #dh-p-removeaction }

Remove [action](../actions.md) from a page of a hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <page>` - Index of the page.
- `#!html <clickType>` - [Click type](../actions.md#click-types) that triggers this action.
- `#!html <index>` - Index of the action.

### `#!html /dh p clearactions <hologram> <page> <clickType>` { #dh-p-clearactions }

Clear [actions](../actions.md) on specified click type in page of a hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <page>` - Index of the page.
- `#!html <clickType>` - [Click type](../actions.md#click-types).

### `#!html /dh p actions <hologram> <page> <clickType>` { #dh-p-actions }

View actions set on the specified [Click type](../actions.md#click-types) in page of a hologram.

- `#!html <hologram>` - Name of the hologram.
- `#!html <page>` - Index of the page.
- `#!html <clickType>` - [Click type](../actions.md#click-types).