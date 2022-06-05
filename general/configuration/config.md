---
description: Main configuration file
---

# Config

## Default config.yml

```yaml
# # # # # # # # # # # # # # # # #
#
# Welcome to DecentHolograms config.yml.
#
# - We recommend you to visit our wiki for
# detailed explanation of all features and
# configuration options as this plugin has
# a ton of them.
#
# - You should also join our discord server for
# more information, support and updates. Our
# discord server is the main way of reporting
# bugs or ideas for possible improvements.
#
# - Web: www.decentholograms.eu
# - Wiki: wiki.decentholograms.eu
# - Discord: discord.decentsoftware.eu
# - GitHub: github.decentsoftware.eu
#
# # # # # # # # # #

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



# # # # # # # # # # # # # # # # #
#
# Custom text replacements
#
# Replace specific patterns in Holograms with custom replacements, similar to HolographicDisplays
#
# # # # # # # # # #

custom-replacements:
  '[x]': '\u2588'    #The symbol looks like this: █
  '[X]': '\u2588'    #The symbol looks like this: █
  '[/]': '\u258C'    #The symbol looks like this: ▌
  '[.]': '\u2591'    #The symbol looks like this: ░
  '[..]': '\u2592'   #The symbol looks like this: ▒
  '[...]': '\u2593'  #The symbol looks like this: ▓
  '[p]': '\u2022'    #The symbol looks like this: •
  '[P]': '\u2022'    #The symbol looks like this: •
  '[|]': '\u23B9'    #The symbol looks like this: ⎹
```

Main 'config.yml' file also contains configuration for [Features](features.md).
