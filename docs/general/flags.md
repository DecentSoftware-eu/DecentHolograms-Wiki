---
title: Flags
subtitle: General usage of flags

icon: material/flag
---

In DecentHolograms, you can configure various flags on holograms and hologram lines. These flags mostly disable some functionality that you don't want or need.

!!! info
    A flag on a hologram affects all its Lines but different lines can have different flags without affecting each other or the parent hologram.

## List of Flags

These are all flags, that are currently available:

- `DISABLE_UPDATING` - Disables updating for hologram or line.
- `DISABLE_PLACEHOLDERS` - Disables placeholders for hologram or line.
- `DISABLE_ANIMATIONS` - Disables animations for hologram or line.
- `DISABLE_ACTIONS` - Disables click actions for hologram.

## Commands

You can configure flags using the following commands. All these commands have Tab-completion so you don't need to type everything manually.

For Holograms:

> ```html
> /dh h addflag <hologram> <flag>
> /dh h removeflag <hologram> <flag>
> ```
>
> - `#!html <hologram>` - Name of the Hologram.
> - `#!html <flag>` - Name of the Flag.

For Hologram Lines:

> ```html
> /dh l addflag <hologram> <page> <line> <flag>
> /dh l removeflag <hologram> <page> <line> <flag>
> ```
>
> - `#!html <hologram>` - Name of the Hologram.
> - `#!html <page>` - Index of the page.
> - `#!html <line>` - Index of the line.
> - `#!html <flag>` - Name of the Flag.