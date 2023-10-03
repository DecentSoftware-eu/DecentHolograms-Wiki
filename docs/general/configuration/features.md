---
title: Features
subtitle: Default features
---

## Commands

You can simply view all commands for features using the following command:

> ```
> /dh features help
> ```

## Damage Display

When damage is dealt, display a temporary holographic text showing the amount of damage.

### Configuration { #configuration-damage }

!!! info "This feature can be configured in the main `config.yml` file."

```yaml
damage-display:
  # Do you want this feature enabled? [true/false]
  enabled: false
  # Do you want to display damage for players? [true/false]
  players: true
  # Do you want to display damage for mobs? [true/false]
  mobs: true
  # Do you want to display 0 (or less) damage? [true/false]
  zero-damage: false
  # How long will the hologram stay in ticks
  duration: 40
  # Damage placeholder: {damage}
  # Animations and Placeholders DO work here
  appearance: '&c{damage}'
  # Appearance of the damage, if the damage is critical
  critical-appearance: '&4&lCrit!&4 {damage}'
  # Height offset
  height: 0
```

## Heal Display

When entity heals, display a temporary holographic text showing the amount of health recovered.

### Configuration { #configuration-heal }

!!! info "This feature can be configured in the main `config.yml` file."

```yaml
healing-display:
  # Do you want this feature enabled? [true/false]
  enabled: false
  # Do you want to display healing for players? [true/false]
  players: true
  # Do you want to display healing for mobs? [true/false]
  mobs: true
  # How long will the hologram stay in ticks
  duration: 40
  # Heal placeholder: {heal}
  # Animations and Placeholders DO work here
  appearance: '&a+ {heal}'
  # Height offset
  height: 0
```