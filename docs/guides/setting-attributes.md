---
title: Setting Attributes for Display Holograms
description: A small guide explaining how you can set attributes for a Display Hologram.
---

Display Entity based Holograms in DecentHolograms utilize a concept called attributes, using a YAML file to store them.  
This system allows a signifcantly more powere way of customization for your Hologram, that wouldn't be possible otherwise with the old system used in Armor Stand based Holograms. It also allows to extend it further in the future, adding new features without having to rewrite the entire system each time.

However, the attribute system may not be the most straight forward to understand, which is why this guide will try and explain it, to hopefully ease you into it and make you feel more familiar with it in the end.

## The attribute-defaults.yml file

DecentHolograms provides a file called [`attribute-defaults.yml`](../configuration/attribute-defaults.md). This file is used as the default for any newly created Display Hologram, copying its values. It is also used when resetting certain attributes of a Hologram using [`/dh displays reset-attibute <name> <attribute>`](../commands/displays/reset-attribute.md).

It contains all the currently supported attributes for Display Holograms, split up into the different Display Entity types supported. This also means that certain attributes are only available for specific Display Types (i.e. `background-color` is only available for `TEXT` Display Holograms).  
It can be a decent guide on what values may be expected and accepted. But with that said can a specific attribute accept one or multiple different formats, which is why using the [`/dh displays attribute <name> <attribute> [value]`](../commands/displays/attribute.md) command is the prefered and recommended aproach.

## The attribute command

The attribute command allows you to change the individual attributes of a Display Hologram. It is extremely powerful to use, providing various tab completions based on the provided attribute and what formats and values it may support.

As an example, using `/dh displays attribute example background-color` may provide you with options such as `rgba` followed by 4 additional arguments to set an RGBA color value, specific color names (i.e. `red`), `DEFAULT` to set it to the default, which is equivalent to using `rgba 0 0 0 64`, `TRANSPARENT` to set it to be transparent, which is equivalent to `rgba 0 0 0 0` and many more.

The command also allows shorthand formats where supported, to reduce the amount of typing required. As an example, using `/dh displays attribute scale 2` is equal to using `/dh displays attribute scale 2 2 2`, meaning it applies the same value to the X, Y and Z scaling.

Some attributes may not be that complex and only accept and require a single value. Such attributes are often times ones that toggle a specific state and therefor only require a boolean to be set. Examples of such attributes are `yaw` and `pitch` (Only requires a number), or `see-through` (Only requires a boolean).