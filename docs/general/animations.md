---
title: Animations
description: How to use built-in animations from DecentHolograms

icon: material/animation-play
---

DecentHolograms supports two types of animations: Premade and custom.

Custom animations can be configured in files and the process of doing so is explained in more detail on [this page](configuration/animation.md).

## Format

> ```command
> <#ANIM:<name>>Text</#ANIM>
> <#ANIM:<name>:<args>>Text</#ANIM>
> ```

/// note
To use placeholders inside animations you need to enable `allow-placeholders-inside-animations` in the [`config.yml`](configuration/config.md).
///

## Premade Animations

There are some premade animations you can use, that will work with any text.

### Colors

> ```command
> <#ANIM:colors>Text</#ANIM>
> OR
> &uText
> ```

### Wave

> ```command
> <#ANIM:wave:<color1>,<color2>>Text</#ANIM>
> ```

/// example
```command
<#ANIM:wave:&f,&b&l>Text</#ANIM>
```
///

### Burn

> ```command
> <#ANIM:burn:<color1>,<color2>>Text</#ANIM>
> ```

/// example
```command
<#ANIM:burn:&f,&b&l>Text</#ANIM>
```
///

### Typewriter

> ```command
> <#ANIM:typewriter>Text</#ANIM>
> ```

### Scroll

> ```command
> <#ANIM:scroll>Text</#ANIM>
> ```