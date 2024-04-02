---
title: Actions
description: Adding and using Click-Actions in your Holograms

icon: material/mouse
---

DecentHolograms allows you to add click-actions to individual hologram pages that get executed when the player either left or right-clicks the hologram.

## Format

Actions themself are in the following formats:

> ```command
> <action_type>
> <action_type>:<args>
> ```

Note that you don't have to include the `<>` brackets!

## Click Types

These click types are used in the [`addaction` page command](commands/hologram-pages.md#dh-p-addaction) to add the action for a specific click type.

- `LEFT`
- `RIGHT`
- `SHIFT_LEFT`
- `SHIFT_RIGHT`

## Action Types

### `#!command MESSAGE:<message>` { #message }

> Sends a message to the player who clicked the hologram.
> 
> - `#!command <message>` - The message to send. Supports Placeholders, including PlaceholderAPI.

### `#!command COMMAND:<command>` { #command }

> Executes a command as the player who clicked the hologram. Should the specified command not start with a `/` will it instead be send as a message by the player.
>
> - `#!command <command>` - The command to execute as the player. Supports Placeholders, including PlaceholderAPI.

### `#!command CONSOLE:<command>` { #console }

> /// warning | Important
> Commands only available through a proxy cannot be executed by this Action.
> ///
>
> Executes the specified command through the console.
>
> - `#!command <command>` - The command to execute as the console. Supports Placeholders, including PlaceholderAPI.

### `#!command CONNECT:<server>` { #connect }

> Sends the player who clicked the hologram to the specified Server. This action only works with Servers connected to a BungeeCord/Velocity proxy.
>
> - `#!command <server>` - Name of the server the player should be connected to.

### `#!command TELEPORT:<world>:<x>:<y>:<z>` / `#!command TELEPORT:<x>:<y>:<z>` { #teleport }

> Teleports the player who clicked the hologram to the specified coordinates, and optionally world.
>
> - `#!command <world>` - Optional world to teleport the player to. Defaults to the World the player is in, if not specified.
> - `#!command <x>` - X coordinate to teleport the player to.
> - `#!command <y>` - Y coordinate to teleport the player to.
> - `#!command <z>` - Z coordinate to teleport the player to.

### `#!command SOUND:<sound>:<volume>:<pitch>` / `#!command SOUND:<sound>` { #sound }

> Plays the specified sound, optionally with a set volume and pitch, to the player who clicked the Hologram.
> 
> - `#!command <sound>` - Name of the sound to play. A list of available sounds is found [here](https://docs.andre601.ch/Spigot-Sounds){ target="_blank" rel="nofollow" }
> - `#!command <volume>` - Optional volume to set. Default if not set is `1.0`.
> - `#!command <pitch>` - Optional pitch to set. Default if not set is `1.0`.

### `#!command PERMISSION:<permission>` { #permission }

> Checks whether the player who clicked the Hologram has the specified permission. Unlike other actions does this one act differently by stopping any actions after it from executing, should the player not have the permission.
> 
> - `#!command <permission>` - The permission to check.

### `#!command NEXT_PAGE:<hologram>` / `NEXT_PAGE` { #next_page }

> Changes the page of the (optionally specified) Hologram to the next one, if one is available.
> 
> - `#!command <hologram>` - Optional Hologram to change the page of. Defaults to the Hologram the player clicked on, if not set.

### `#!command PREV_PAGE:<hologram>` / `PREV_PAGE` { #prev_page }

> Changes the page of the (optionally specified) Hologram to the previous page, if one is available.
> 
> - `#!command <hologram>` - Optional Hologram to change the page of. Defaults to the Hologram the player clicked on, if not set.

### `#!command PAGE:<hologram>:<page>` / `#!command PAGE:<page>` { #page }

> Changes to the specified page on the (optionally specified) Hologram, if one is available.
> 
> - `#!command <hologram>` - Optional Hologram to change the page of. Defaults to the Hologram the player clicked on, if not set.
> - `#!command <page>` - Page to switch to on the Hologram.
