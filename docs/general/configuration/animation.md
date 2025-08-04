---
title: Animation
description: Configuration of custom animations
---

The `animations` folder contains all the custom animations you want to use with each custom animation being its own YAML file.

## Usage

To use a custom animation, use the `#!command <#ANIM:<name>>[text]</#ANIM>` format you use for [built-in animation](../animations.md), replacing `#!command <name>` with the file-name (without the `.yml` file extension) and `#!command [text]` with optional text that should be used in the animation through the `#!command {text}` placeholder.

/// note
Filenames starting with `animation_` will have this part removed when creating an animation.  
This exists as a backwards-compatability due to how DecentHolograms expected specific filenames in the past.
///

/// example
This example would display the animation from the example file shown below.

```command
<#AMIM:example>Hello World!</#ANIM>
```
///

## Example Animation file

```yaml title="animation_example.yml"
#
# Speed of the animation in ticks.
# Represents the delay between animation steps.
#
# For speed of 2, the animation will wait
# two ticks between each step.
speed: 2

#
# Pause of the animation in ticks.
# Represents the delay between animation runs.
#
# For speed of 20, the animation will wait
# 20 ticks between each run.
pause: 20

#
# Steps of the animation
#
# List of strings that's going to be cycled
# over during the animation.
#
# You can use '{text}' placeholder, to display
# the text, that is inside this animation
# in the hologram:
# - <#ANIM:example>This text</ANIM>
#
steps:
- 'Example 1 {text}'
- 'Example 2'
- 'Example 3'
- 'Example 4'
- 'Example 5'
```
