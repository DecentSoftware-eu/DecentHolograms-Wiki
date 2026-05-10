---
title: Actions
description: Adding and using Click-Actions on Hologram Pages

icon: material/mouse
---

DecentHolograms provides the ability set Actions that should be executed when left- or right-clicking specific Hologram pages.  
Actions are added using the [`/dh p addaction`](../commands/hologram-pages/addaction.md) command.

## Click Types

Actions are set per click-type, which can be one of the following options:

- `LEFT` - Left-clicking
- `RIGHT` - Right-clicking
- `SHIFT_LEFT` - Left-clicking while sneaking
- `SHIFT_RIGHT` - Right-clicking while sneaking

## Action Types

The following types are available to use.

### `#!command MESSAGE:<message>`

Sends a message to the player who clicked the Hologram.

- `#!command <message>` - The message to send. Supports placeholders and color and formatting codes.

/// details | Example
    type: example

```
MESSAGE:Hello {player}!
```
///

### `#!command COMMAND:<command>`

Execizes a command as the player who clicked the Hologram.  
The `#!command <command>` value needs to start with a `/` to run as a command. If not, will the text be send as a message by the player.

- `#!command <command>` - The command to execute as the player.

/// details | Example
    type: example

```
COMMAND:/help
COMMAND:My name is {player}!
```
///

### `#!command CONSOLE:<command>`

/// warning | Proxy commands cannot be executed with this!
///

Executes a command as the console whenever the player clicks the Hologram.

- `#!command <command>` - The command to execute as the console.

/// details | Example
    type: example

```
CONSOLE:say {player} clicked on a Hologram!
```
///

### `#!command CONNECT:<server>`

Sends the player who clicked the Hologram to the specified Server.  
This only works for servers connected to a Proxy and uses the name configured in the proxy.

- `#!command <server>` - Name of the server to connect to.

/// details | Example
    type: example

```
CONNECT:lobby
```
///

### `#!command TELEPORT:[<world>:]<x>:<y>:<z>[:<yaw>:<pitch>]`

Teleports the player who clicked the Hologram to the specified coordinates and world.

- `#!command [<world>:]` - Name of the world to teleport to. If not set, uses the world the player is in.
- `#!command <x>` - The X coordinates to teleport the player to.
- `#!command <y>` - The Y coordinates to teleport the player to.
- `#!command <z>` - The Z coordinates to teleport the player to.
- `#!command [:<yaw>:<pitch>]` - The Yaw and Pitch the player should have. If not set, uses the player's current yaw and pitch.

/// details | Examples
    type: example

```
TELEPORT:0:100:0
TELEPORT:world:0:100:0
TELEPORT:0:100:0:-180:0
TELEPORT:world:0:100:0:-180:0
```
///

### `#!command SOUND:<sound>[:<volume>:<pitch>]`

Plays the specified sound for the player who clicked the Hologram, optionally with the specified volume and pitch.

- `#!command <sound>` Name of the sound to play. Available sound names can be found [here](https://docs.andre601.ch/Spigot-Sounds/){ target="_blank" rel="noopener" }
- `#!command [:<volume>:<pitch>]` - Optional volume and pitch. Defaults to 1.0 if not set.

/// details | Examples
    type: example

```
SOUND:ENTITY_CREEPER_PRIMED
SOUND:ENTITY_CREEPER_PRIMED:0.5:0.5
```
///

### `#!command PERMISSION:<permission>`

Checks if the player who clicked the Hologram has the specified permission.  
If the player does not have the permission, are any follow-up actions not executed.

- `#!command <permission>` - The permission to check.

/// details | Example
    type: example

```
PERMISSION:some.permission
```
///

### `#!command NEXT_PAGE[:<hologram>]`

Switches the page of a Hologram to the next one, if available.  
The page is only switched for the player who clicked the Hologram.

- `#!command [:<hologram>]` - Optional Hologram name to change a specific Hologram's page. Defaults to the Hologram the player clicked, if not specified.

/// details | Examples
    type: example

```
NEXT_PAGE
NEXT_PAGE:some_hologram
```
///

### `#!command PREV_PAGE[:<hologram>]`

Switches the page of a Hologram to the previous one, if available.  
The page is only switched for the player who clicked the Hologram.

- `#!command [:<hologram>]` - Optional Hologram name to change a specific Hologram's page. Defaults to the Hologram the player clicked, if not specified.

/// details | Examples
    type: example

```
PREV_PAGE
PREV_PAGE:some_hologram
```
///

### `#!command PAGE:[<hologram>:]<page>`

Switches the page of a Hologram to the specified one, if available.  
The page is only switched for the player who clicked the Hologram.

- `#!command [<hologram>:]` - Optional Hologram name to change a specific Hologram's page. Defaults to the Hologram the player clicked, if not specified.
- `#!command <page>` - Number of the Page to switch to in the Hologram.

/// details | Examples
    type: example

```
PAGE:1
PAGE:some_hologram:1
```
///