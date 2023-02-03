---
description: Configuration of custom animations.
---

# Animation

You can use your custom animations in holograms with the following format.

> <#ANIM:name>Any text here\</#ANIM>

Example line:

> Animation: <#ANIM:example>Some Text\</#ANIM>

### Example animation (animation\_example.yml)

```yaml
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

