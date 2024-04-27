---
title: Animations
description: How to use built-in animations from DecentHolograms

icon: material/animation-play
---

DecentHolograms supports two types of animations: Premade and custom.

Custom animations can be configured in files and the process of doing so is explained in more detail on [this page](configuration/animation.md).

## Format

:   
    ```command
    <#ANIM:<name>>Text</#ANIM>  
    <#ANIM:<name>:<args>>Text</#ANIM>  
    ```

/// note
To use placeholders inside animations you need to enable `allow-placeholders-inside-animations` in the [`config.yml`](configuration/config.md).
///

## Premade Animations

There are some premade animations you can use, that will work with any text.

### Colors

:   Switches through all available color codes. This is the same as in HolographicDisplays and also offers the `&u` as an alternative color code to use.
    ```command
    <#ANIM:colors>Text</#ANIM>
    ```

### Wave

:   Colors the text in `#!command <color1>` and makes `#!command <color2>` move through the text.
    ```command
    <#ANIM:wave:<color1>,<color2>>Text</#ANIM>
    ```
    
    /// example
    ```command
    <#ANIM:wave:&f,&b&l>Text</#ANIM>
    ```
    ///

### Burn

:   Colors the text in `#!command <color1>` and changes it to `#!command <color2>` from left to right.
    ```command
    <#ANIM:burn:<color1>,<color2>>Text</#ANIM>
    ```
    
    /// example
    ```command
    <#ANIM:burn:&f,&b&l>Text</#ANIM>
    ```
    ///

### Typewriter

:   Writes the provided text one character at a time.
    ```command
    <#ANIM:typewriter>Text</#ANIM>
    ```

### Scroll

:   Scrolls through the provided text. The length is set to `<text length> / 3 * 2`.
    ```command
    <#ANIM:scroll>Text</#ANIM>
    ```