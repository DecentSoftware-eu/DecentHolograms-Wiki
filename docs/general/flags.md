---
title: Flags
description: General usage of flags

icon: material/flag
---

In DecentHolograms, you can configure various flags on holograms and hologram lines. These flags mostly disable some functionality that you don't want or need.

/// info
A flag on a hologram affects all its Lines but different lines can have different flags without affecting each other or the parent hologram.
///

## List of Flags

These are all flags, that are currently available:

- `DISABLE_UPDATING` - Disables updating for hologram or line.
- `DISABLE_PLACEHOLDERS` - Disables placeholders for hologram or line.
- `DISABLE_ANIMATIONS` - Disables animations for hologram or line.
- `DISABLE_ACTIONS` - Disables click actions for hologram.

## Commands

The following commands can be used to add and remove flags from holograms or even hologram lines:

- [`#!command /dh h addflag <hologram> <flag>`](commands/hologram.md#dh-h-addflag)
- [`#!command /dh h removeflag <hologram> <flag>`](commands/hologram.md#dh-h-removeflag)
- [`#!command /dh l addflag <hologram> <page> <line> <flag>`](commands/hologram-line.md#dh-l-addflag)
- [`#!command /dh l removeflag <hologram> <page> <line> <flag>`](commands/hologram-line.md#dh-l-removeflag)