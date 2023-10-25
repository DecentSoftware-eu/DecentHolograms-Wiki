---
title: Actions
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

Sends `#!command <message>` to the player who clicked the hologram.

### `#!command COMMAND:<command>` { #command }

Executes `#!command <command>` as the player who clicked the hologram. If `#!command <command>` doesn't start with `/` will it be send as a message from the player.

### `#!command CONSOLE:<command>` { #console }

Executes `#!command <command>` as the console.

### `#!command CONNECT:<server>` { #connect }

Sends the player who clicked to `#!command <server>`. Only works on a BungeeCord/Velocity network.

### `#!command TELEPORT:<world>:<x>:<y>:<z>` / `#!command TELEPORT:<x>:<y>:<z>` { #teleport }

Teleports the player to the provided world and coordinates. If no world is provided will the world the player is in be used.

### `#!command SOUND:<sound>` { #sound }

Plays a sound for the player who clicked.

What sounds you can use depends on the server version. Here is a list of sounds:

- [For 1.8]()
- [For 1.9+]()
- [For 1.13+]()

You can see a list of sounds for a specific version by replacing `1.13` in the link below with a matching version:  
https://helpch.at/docs/1.13/index.html?org/bukkit/Sound.html

### `#!command PERMISSION:<permission>` { #permission }

Checks whether the player who clicked has the specified permission and if not, all the actions after this one will not be executed.

### `#!command NEXT_PAGE:<hologram>` / `NEXT_PAGE` { #next_page }

Switches to the next page of the specified hologram. If no hologram is provided will the one the player clicked on be used.

### `#!command PREV_PAGE:<hologram>` / `PREV_PAGE` { #prev_page }

Switches to the previous page of the specified hologram. If no hologram is provided will the one the player clicked on be used.

### `#!command PAGE:<hologram>:<page>` / `#!command PAGE:<page>` { #page }

Switches to the specified page of the specified hologram. If no hologram is provided will the one the player clicked on be used.