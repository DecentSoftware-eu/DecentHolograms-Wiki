---
title: Colors
description: Information about what types of colors are supported

icon: material/palette
---

## Basic colors and formatting

DecentHolograms supports all basic color and formatting options through the usage of the `&` color code.  
For example, `&1` would be dark blue and `&l` would be bold.

## RGB (1.16+)

DecentHolograms supports multiple formats for RGB colors, all of which are defined in hexadecimal format. The first two digit represent the red color, the middle ttwo digits represent the green color, and the last two digits represent the blue color.

- `#RRGGBB`
- `&#RRGGBB`
- `<#RRGGBB>`
- `{#RRGGBB}`

## Gradients

Gradients in DecentHolograms are defined using the following format:

/// tip
You can use formatting codes inside the gradients.
///

> ```command
> <#RRGGBB>This text is going to have a gradient.</#RRGGBB>
> ```

Example gradient:

> ```command
> <#00FFFF>&l&nDECENT HOLOGRAMS</#FF00FF>
> ```

## Rainbow Gradients

Rainbow Gradients in DecentHolograms are defined using the following formats:

/// tip
You can also put another number from 0 to 999 instead of the 1 to make the rainbow different.
///

> ```command
> <RAINBOW1>Rainbow Text</RAINBOW>
> ```

## Rainbow Color

Rainbow Color is an animated color that cycles through all colors gradually, giving the text a dynamic and visually striking effect.  
Former HolographicDisplays users may be familiar with this one, as it uses the same color code:

> ```
> &uSome color-changing text
> ```