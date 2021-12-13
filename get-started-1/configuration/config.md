---
description: Main configuration file
---

# Config

## Default config.yml

```yaml
defaults:
  # Default line
  text: Blank Line
  # Default Hologram display range in blocks.
  display-range: 48
  # Default Hologram update range in blocks.
  update-range: 48
  # Default Hologram update interval in ticks.
  update-interval: 20
  # Default heigths of different hologram line types.
  height:
    text: 0.3
    icon: 0.6
    head: 0.75
    smallhead: 0.6
  # Default value of Down Origin
  down-origin: false
  # Default value of Always Face Player
  always-face-player: true

# Check for updates on plugin startup? [true/false]
update-checker: true
```

Main 'config.yml' file also contains configuration for [Features](features.md).
