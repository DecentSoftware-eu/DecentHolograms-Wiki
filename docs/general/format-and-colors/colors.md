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

:   /// tip | Formatting codes can be used in-between the gradients.
    ///
    
    Gradients can be defined using `#!command <#rrggbb>text</#rrggbb>` where `#!command <#rrggbb>` is the starting color and `#!command </#rrggbb>` the ending color.
    
    /// example
    ```command
    <#FF0000>Gradient!</#00FF00>
    ```
    ///

## Rainbow Gradients

:   A rainbow gradient can be created using `<RAINBOW0>text</RAINBOW>`. The `1` can be replaced with any number from 0 to 999 to change the rainbow.
    
    /// example
    ```command
    <RAINBOW1>Rainbow Gradient!</RAINBOW>
    ```
    ///

## Rainbow Color (Animated) { #rainbow-color }

:   Using `<#ANIM:colors>`, you can make your Text cycle through all available color codes.  
    This is similar to what you may know from HolographicDisplays and does in fact also provide a `&u` color code for your convenience.
    
    /// example
    ```command
    &uAnimated rainbow text!
    ```
    ///