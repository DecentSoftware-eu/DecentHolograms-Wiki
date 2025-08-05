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
speed: 2
pause: 20
steps:
- 'Example 1 {text}'
- 'Example 2'
- 'Example 3'
- 'Example 4'
- 'Example 5'
```

## Options

### `speed`

:   **Type:** Integer

    Defines the delay in ticks between each [`steps`](#steps) to wait.  
    20 ticks = 1 second.

### `pause`

:   **Type:** Integer

    Defines the delay in tick for the Animation to wait once it completed the [`steps`](#steps) list before starting again.  
    20 ticks = 1 second.

### `steps`

:   **Type:** List of Strings

    Sets the individual frames the animation should go through.  
    Supports PlaceholderAPI placeholders, if `allow-placeholders-inside-animations` is enabled in the [config.yml](config.yml).

    `{text}` can be used to display the text that can be put in-between the `<#ANIM></#ANIM>` tags when using the custom animation.
