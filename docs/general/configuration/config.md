---
title: Config
description: Main configuration file
---

/// note
Main `config.yml` also contains configuration for [Features](features.md)
///

```yaml title="config.yml"
defaults:
  text: Blank Line
  display-range: 48
  update-range: 48
  update-interval: 20
  lru-cache-size: 500
  height:
    text: 0.3
    icon: 0.6
    head: 0.75
    smallhead: 0.6
  down-origin: false

update-checker: true
click-cooldown: 5
allow-placeholders-inside-animations: false
update-visibility-on-teleport: false
holograms-eye-level-positioning: false

damage-display:
  enabled: false
  players: true
  mobs: true
  zero-damage: false
  duration: 40
  appearance: '&c{damage}'
  critical-appearance: '&4&lCrit!&4 {damage}'
  height: 0

healing-display:
  enabled: false
  players: true
  mobs: true
  duration: 40
  appearance: '&a+ {heal}'
  height: 0

custom-replacements:
  '[x]': '█'
  '[X]': '█'
  '[/]': '▌'
  '[,]': '░'
  '[,,]': '▒'
  '[,,,]': '▓'
  '[p]': '•'
  '[P]': '•'
  '[|]': '⎹'
```

## Options

### `defaults`

These options mostly affect newly created holograms by defining their default values.  
Already existing Holograms do not get affected by any changes made in these options.

#### `defaults.text`

:   **Type:** String

    Sets the default text that should be displayed when creating a new hologram.

#### `defaults.display-range`

:   **Type:** Integer

    Sets the default distance in which the Hologram should be shown.  
    Note that the display may be influenced by the player's and server's view distance.

#### `defaults.update-range`

:   **Type:** Integer

    Sets the default distance in which the Hologram should update animations and placeholders.

#### `defaults.update-interval`

:   **Type:** Integer
    
    Sets the default interval in ticks for the Hologram to update.  
    20 ticks = 1 second.

#### `defaults.lru-cache-size`

:   **Type:** Integer (5-10,000)

    Sets the maximum amount of cached pattern processing results.  
    Usually you don't need to change the default value.

    Note that increasing the number can result in a higher Memory usage.

#### `defaults.height`

##### `defaults.height.text`

:   **Type:** Float

    Sets the default line height/distance in blocks for a Text line.

##### `defaults.height.icon`

:   **Type:** Float

    Sets the default line height/distance in blocks for a `#ICON` (floating item) line.

##### `defaults.height.head`

:   **Type:** Float

    Sets the default line height/distance in blocks for a `#HEAD` (armor stand head) line.

##### `defaults.height.smallhead`

:   **Type:** Float

    Sets the default line height/distance in blocks for a `#SMALLHEAD` (small armor stand head) line.

#### `defaults.down-origin`

:   **Type:** Boolean

    Sets whether the Hologram's location should be based on its bottom or top part.

### `update-checker`

:   **Type:** Boolean
    
    Enables/Disables the Update checker of DecentHolograms.

### `click-cooldown`

:   **Type:** Integer

    Defines the Cooldown in ticks to apply between clicks.  
    20 ticks = 1 second.

### `allow-placeholders-inside-animations`

:   **Type:** Boolean

    Sets whether placeholders inside animations should be replaced.

    /// note
    Enabling this can have a negative impact on your server's CPU usage, so if you don't need to have placeholders parsed inside animations, keep this option disabled.
    ///

### `update-visibility-on-teleport`

:   **Type:** Boolean

    Whether Hologram visibility should be updated whenever a player is being teleported.  
    This causes a visual glitch where even teleportations of only a few blocks cause the hologram to disappear and reappear, but is the only reliable "fix" for older MC versions containing a bug with entities disappearing on Player teleportation.

### `holograms-eye-level-positioning`

:   **Type:** Boolean

    Sets whether holograms should be positioned at the player's eye-level instead of their feet position when being created or moved to the player.

### `damage-display`

:   This section is explained in the [Features](features.md#damage-display) page.

### `heal-display`

:   This section is explained in the [Features](features.md#heal-display) page.

### `custom-replacements`

:   **Type:** Map of String and String

    Allows you to define a collection of patterns that should be replaced with another symbol or text.  
    The default is similar to HolographicDisplay's pattern feature, replacing patterns such as `[x]` with their respective Unicode equivalent.
