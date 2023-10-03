---
title: Actions
icon: material/mouse
---

DecentHolograms allows you to add click-actions to individual hologram pages that get executed when the player either left or right-clicks the hologram.

## Format

Actions themself are in the following formats:

> ```html
> <action_type>
> <action_type>:<args>
> ```

## Click Types

These click types are used in the [`addaction` page command](commands/hologram-pages.md#dh-p-addaction) to add the action for a specific click type.

- `LEFT`
- `RIGHT`
- `SHIFT_LEFT`
- `SHIFT_RIGHT`

## Action Types

> `<>` = Required
> `[]` = Optional
>
> The brackets themself are not needed.

### `#!html MESSAGE:<message>` { #message }

Sends `#!html <message>` to the player who clicked the hologram.

### `#!html COMMAND:<command>` { #command }

Executes `#!html <command>` as the player who clicked the hologram. If `#!html <command>` doesn't start with `/` will it be send as a message from the player.

### `#!html CONSOLE:<command>` { #console }

Executes `#!html <command>` as the console.

### `#!html CONNECT:<server>` { #connect }

Sends the player who clicked to `#!html <server>`. Only works on a BungeeCord/Velocity network.

### `#!html TELEPORT:<world>:<x>:<y>:<z>` / `#!html TELEPORT:<x>:<y>:<z>` { #teleport }

Teleports the player to the provided world and coordinates. If no world is provided will the world the player is in be used.

### `#!html SOUND:<sound>` { #sound }

Plays a sound for the player who clicked.

What sounds you can use depends on the server version. Here is a list of sounds:

- [For 1.8]()
- [For 1.9+]()
- [For 1.13+]()

You can see a list of sounds for a specific version by replacing `1.13` in the link below with a matching version:  
https://helpch.at/docs/1.13/index.html?org/bukkit/Sound.html

### `#!html PERMISSION:<permission>` { #permission }

Checks whether the player who clicked has the specified permission and if not, all the actions after this one will not be executed.

### `#!html NEXT_PAGE:<hologram>` / `NEXT_PAGE` { #next_page }

Switches to the next page of the specified hologram. If no hologram is provided will the one the player clicked on be used.

### `#!html PREV_PAGE:<hologram>` / `PREV_PAGE` { #prev_page }

Switches to the previous page of the specified hologram. If no hologram is provided will the one the player clicked on be used.

### `#!html PAGE:<hologram>:<page>` / `#!html PAGE:<page>` { #page }

Switches to the specified page of the specified hologram. If no hologram is provided will the one the player clicked on be used.