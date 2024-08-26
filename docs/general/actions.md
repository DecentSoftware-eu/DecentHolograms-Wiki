---
title: Actions
description: Adding and using Click-Actions in your Holograms

icon: material/mouse
---

DecentHolograms allows you to add click-actions to individual hologram pages that get executed when the player either left or right-clicks the hologram.

## Click Types

These click types are used in the [`addaction` page command](commands/hologram-pages.md#dh-p-addaction) to add the action for a specific click type.

- `LEFT`
- `RIGHT`
- `SHIFT_LEFT`
- `SHIFT_RIGHT`

## Action Types

The following action types are available to use.

### `#!command MESSAGE:<message>` { #message }

Sends a message to the player who clicked the hologram.

- `#!command <message>` - The message to send. Supports Placeholders, including PlaceholderAPI.

/// details | Example
    type: example

```
MESSAGE:You clicked this Hologram! # Sends "You clicked this Hologram!" to the player.
```
///

----

### `#!command COMMAND:<command>` { #command }

Executes a command as the player who clicked the hologram. Should the specified command not start with a `/` will it instead be send as a message by the player.

- `#!command <command>` - The command to execute as the player. Supports Placeholders, including PlaceholderAPI.

/// details | Examples
    type: example

```
COMMAND:/help               # Executes /help as the player.
COMMAND:My name is {player} # Sends "My name is {player}" as the player.
```
///

----

### `#!command CONSOLE:<command>` { #console }

/// warning | Proxy commands cannot be executed by this action!
///

Executes the specified command through the console.

- `#!command <command>` - The command to execute as the console. Supports Placeholders, including PlaceholderAPI.

/// details | Example
    type: example

```
CONSOLE:say {player} clicked on a Hologram! # Executes "/say {player} clicked on a Hologram!" as the console.
```
///

----

### `#!command CONNECT:<server>` { #connect }

Sends the player who clicked the hologram to the specified Server. This action only works with Servers connected to a BungeeCord/Velocity proxy.

- `#!command <server>` - Name of the server the player should be connected to.

/// details | Example
    type: example

```
CONNECT:lobby # Connects the player to the server named "lobby".
```
///

----

### `#!command TELEPORT:[<world>:]<x>:<y>:<z>[:<yaw>:<pitch>]` { #teleport }

Teleports the player who clicked the hologram to the specified coordinates, and optionally world.

- `#!command [<world>:]` - Optional `#!command <world>` to teleport the player to. Defaults to the World the player is in, if not specified.
- `#!command <x>` - X coordinate to teleport the player to.
- `#!command <y>` - Y coordinate to teleport the player to.
- `#!command <z>` - Z coordinate to teleport the player to.
- `#!command [:<yaw>:<pitch>]` - Optional `#!command <yaw>` and `#!command <pitch>` to set for the teleportation. Defaults to the current Yaw and Pitch of the player if not set.

/// details | Example
    type: example

```
TELEPORT:0:100:0              # Teleports player to 0,100,0 in the World they are.
TELEPORT:world:0:100:0        # Teleports player to 0,100,0 in World "world".
TELEPORT:0:100:0:-180:0       # Teleports player to 0,100,0 in the World they are, facing North.
TELEPORT:world:0:100:0:-180:0 # Teleports player to 0,100,0 in World "world", facing North.
```
///

----

### `#!command SOUND:<sound>[:<volume>:<pitch>]` { #sound }

Plays the specified sound, optionally with a set volume and pitch, to the player who clicked the Hologram.

- `#!command <sound>` - Name of the sound to play. A list of available sounds is found [here](https://docs.andre601.ch/Spigot-Sounds){ target="_blank" rel="nofollow" }
- `#!command [:<volume>:<pitch>]` - Optional `#!command <volume>` and `#!command <pitch>` with both defaulting to 1.0 if not set.

/// details | Examples
    type: example

```
SOUND:ENTITY_CREEPER_PRIMED # "Creeper Primed" sound at normal volume and pitch.
SOUND:ENTITY_CREEPER_PRIMED:0.5:0.5 # "Creeper Primed" sound at half the volume and pitch.
```
///

----

### `#!command PERMISSION:<permission>` { #permission }

Checks whether the player who clicked the Hologram has the specified permission. Unlike other actions does this one act differently by stopping any actions after it from executing, should the player not have the permission.

- `#!command <permission>` - The permission to check.

/// details | Examples
    type: example

```
PERMISSION:some.permission.here # Checks for permission some.permission.here
```
///

----

### `#!command NEXT_PAGE[:<hologram>]` { #next_page }

Changes the page of the (optionally specified) Hologram to the next one, if one is available.

- `#!command [:<hologram>]` - Optional Hologram `#!command <hologram>` to change the page of. Defaults to the Hologram the player clicked on, if not set.

/// details | Examples
    type: example

```
NEXT_PAGE               # Moves to the next page of the Hologram the player clicks.
NEXT_PAGE:some_hologram # Moves to the next page of the Hologram "some_hologram".
```
///

----

### `#!command PREV_PAGE[:<hologram>]` { #prev_page }

Changes the page of the (optionally specified) Hologram to the previous page, if one is available.

- `#!command [:<hologram>]` - Optional Hologram `#!command <hologram>` to change the page of. Defaults to the Hologram the player clicked on, if not set.

/// details | Examples
    type: example

```
PREV_PAGE               # Moves to the previous page of the Hologram the player clicks.
PREV_PAGE:some_hologram # Moves to the previous page of the Hologram "some_hologram".
```
///

----

### `#!command PAGE:[<hologram>:]<page>` { #page }

Changes to the specified page on the (optionally specified) Hologram, if one is available.

- `#!command [<hologram>:]` - Optional Hologram `#!command <hologram>` to change the page of. Defaults to the Hologram the player clicked on, if not set.
- `#!command <page>` - Page to switch to on the Hologram.

/// details | Examples
    type: example

```
PAGE:2               # Switches to page 2 of the Hologram the player clicked.
PAGE:some_hologram:1 # Switches to page 2 of the Hologram "some_hologram".
```
///
