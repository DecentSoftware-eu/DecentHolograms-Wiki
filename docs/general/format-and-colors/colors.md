---
title: Colors
icon: material/palette
---

## RGB (1.16+)

DecentHolograms supports multiple formats for RGB colors, all of which are defined in hexadecimal format. The first two digit represent the red color, the middle ttwo digits represent the green color, and the last two digits represent the blue color.

- `#RRGGBB`
- `&#RRGGBB`
- `<#RRGGBB>`
- `{#RRGGBB}`

## Gradients

Gradients in DecentHolograms are defined using the following format:

!!! tip
    You can use special color codes inside the gradients.

> ```
> <#RRGGBB>This text is going to have a gradient.</#RRGGBB>
> ```

Example gradient:

> ```
> <#00FFFF>&l&nDECENT HOLOGRAMS</#FF00FF>
> ```

## Rainbow Gradients

Rainbow Gradients in DecentHolograms are defined using the following formats:

!!! tip
    You can also put another number from 0 to 999 instead of the 1 to make the rainbow different.

> ```
> <RAINBOW1>Rainbow Text</RAINBOW>
> ```

## Rainbow Color

Rainbow Color is an animated color that cycles through all colors gradually, giving the text a dynamic and visually striking effect.  
Former HolographicDisplays users may be familiar with this one, as it uses the same color code:

> ```
> &uSome color-changing text
> ```