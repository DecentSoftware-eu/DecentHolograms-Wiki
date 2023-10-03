---
title: Animations
icon: material/animation-play
---

DecentHolograms supports two types of animations: Premade and custom.

Custom animations can be configured in files and the process of doing so is explained in more detail on [this page](configuration/animation.md).

## Format

> ```html
> <#ANIM:<name>>Text</#ANIM>
> <#ANIM:<name>:<args>>Text</#ANIM>
> ```

!!! note
    To use placeholders inside animations you need to enable `allow-placeholders-inside-animations` in the [`config.yml`](configuration/config.md).

## Premade Animations

There are some premade animations you can use, that will work with any text.

### Colors

> ```
> <#ANIM:colors>Text</#ANIM>
> OR
> &uText
> ```

### Wave

> ```html
> <#ANIM:wave:<color1>,<color2>>Text</#ANIM>
> ```

!!! example
    > ```
    > <#ANIM:wave:&f,&b&l>Text</#ANIM>
    > ```

### Burn

> ```html
> <#ANIM:burn:<color1>,<color2>>Text</#ANIM>
> ```

!!! example
    > ```
    > <#ANIM:burn:&f,&b&l>Text</#ANIM>
    > ```

### Typewriter

> ```
> <#ANIM:typewriter>Text</#ANIM>
> ```

### Scroll

> ```
> <#ANIM:scroll>Text</#ANIM>
> ```