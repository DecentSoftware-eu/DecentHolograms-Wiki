---
title: Events
description: Custom Events offered by DecentHolograms

icon: material/text-long
---


DecentHolograms offers a collection of Events, all being triggered during specific situations.  
To use these events, add them to your plugin like you would with any other event provided by the Server.

## DecentHologramsEvent

This is the most basic event. All other events extend from it and it can be used as a catch-all for any DecentHolograms-based events.  
It's recommended to use the more specific events, but if you want to use this one, it is recommended to do `instanceof` checks and casting to more specific Event instances to use possible getters.

This event does not offer any methods outside the default ones from the Server.

## DecentHologramsReloadEvent

This event is called whenever DecentHolograms is being reloaded through its [`/dh reload`](../general/commands/general.md#dh-reload) command.  
This is useful for when your plugin needs to be aware of any reloads by DecentHolograms (i.e. to refresh own holograms added or other special cases).

This event does not offer any methods outside the default ones from the Server.

## HologramClickEvent

This event is called whenever a player is interacting with a hologram by left or right clicking it.  
The event is cancellable, allowing you to stop any further handling of it.

The event offers the following methods:

- `getPlayer()` - Gets the Player that clicked the hologram.
- `getHologram()` - Gets the hologram that has been clicked.
- `getHologramPage()` - Gets the HologramPage that has been clicked.
- `getClickType()` - Gets the click type (Whether it was left or right click and whether the player sneaked while clicking).
- `getEntityId()` - Gets the ID of the clicked entity.

## HologramDisableEvent

This event is called whenever a Hologram gets disabled through `Hologram.disable(DisableCause)`.

The event offers the following methods:

- `getHologram()` - Gets the Hologram that got disabled.

## HologramEnableEvent

This event is called whenever a Hologram gets enabled through `Hologram.enable()`.

The event offers the following methods:

- `getHologram()` - Gets the Hologram that got enabled.

## HologramRegisterEvent

This event is called whenever a Hologram is registered through `HologramManager.registerHologram(Hologram)`.

The event offers the following methods:

- `getHologram()` - Gets the Hologram that got registered.

## HologramUnregisterEvent

This event is called whenever a Hologram is unregistered through `HologramManager.destroy()`.

The event offers the following methods:

- `getHologram()` - The Hologram that got unregistered.
