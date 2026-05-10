---
title: 'Flags'
description: 'Allows the disabling of specific features'

icon: material/flag
---

DecentHolograms provides a feature called flags.  
Flags allow you to disable specific features either on the entire hologram, or per line.

Flags are added using either [`/dh h addflag`](../commands/hologram/addflag.md) or [`/dh l addflag`](../commands/hologram-lines/addflag.md), and are removed using either [`/dh h removeflag`](../commands/hologram/removeflag.md) or [`/dh l removeflag`](../commands/hologram-lines/removeflag.md) respectively.

## Available Flags

### `DISABLE_UPDATING`

Disables the updating of a Hologram or specific Hologram line.  
This flag can be seen as a combination of `DISABLE_PLACEHOLDERS` and `DISABLE_ANIMATIONS`.

### `DISABLE_PLACEHOLDERS`

Disables the parsing of Placeholders.

### `DISABLE_ANIMATIONS`

Disables the updating of animations.

### `DISABLE_ACTIONS`

Disables the handling of actions.  
This does **not** disable the HologramClickEvent!