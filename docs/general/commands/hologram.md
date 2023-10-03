---
title: Hologram
subtitle: General usage and editing of Holograms
---

## Commands

> Aliases: `hologram`, `holo`, `h`

Due to the large number of commands for editing holograms, we have grouped them into their own category. You can access all of these commands by using the command provided below.

> ```html
> /dh holograms <subcommand>
> ```

### `/dh h help`

This command displays a comprehensive list of all hologram-related commands.

### `#!html /dh h create <name> [-l:world:x:y:z] [content]` { #dh-h-create }

> Aliases: `create`, `c`

Create a new hologram.

- `#!html <name>` - Name of the created Hologram.
- `[-l:world:x:y:z]` - Optional location argument, which allows you to specify the location where the hologram should be placed. This argument can also be used by console users to execute the command.
- `[content]` - Content of the first line. (Optional)

### `#!html /dh h clone <hologram> <name> [temp] [-l:world:x:y:z]` { #dh-h-clone }

> Aliases: `copy`

Clone an existing hologram.

- `#!html <hologram>` - Name of the Hologram to clone.
- `#!html <name>` - Name of the new, clones Hologram.
- `[temp]` - `true`, if you DON'T want the hologram to save, otherwise `false` (default). (Optional)
- `[-l:world:x:y:z]` - Optional location argument, which allows you to specify the location where the cloned hologram should be placed. This argument can also be used by console users to execute the command.

!!! example "Examples"
    - `/dh h clone test test_clone -l:world:0:100:0`
    - `/dh h clone test test_clone true`
    - `/dh h clone test test_clone`
    - `/dh h clone test test_clone -l:world:0:100:0 false`

### `#!html /dh h delete <hologram>` { #dh-h-delete }

> Aliases: `del`, `remove`, `rem`

Delete an existing hologram.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h rename <hologram> <new_name>` { #dh-h-rename }

Rename an existing hologram.

- `#!html <hologram>` - Name of the Hologram, you want to rename.
- `#!html <new_name>` - The Hologram's new name.

### `#!html /dh h setpermission <hologram> [permission]` { #dh-h-setpermission }

> Aliases: `permission`, `setperm`, `perm`

Set the current permission required to view the hologram.

- `#!html <hologram>` - Name of the Hologram.
- `[permission]` - New permissio. (Leave empty to remove)

### `#!html /dh h info <hologram>` { #dh-h-info }

Prints some general info about a hologram.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h lines <hologram> [page]` { #dh-h-lines }

Lists all the holograms lines.

- `#!html <hologram>` - Name of the Hologram.
- `[page]` - Page of the list. (Optional)

### `#!html /dh h teleport <hologram>` { #dh-h-teleport }

> Aliases: `tele`, `tp`

Teleports you to the given hologram.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h move <hologram> <x> <y> <z>` { #dh-h-move }

> Aliases: `mv`

Teleports the given hologram to the given coordinates.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <x>` - New X location of the Hologram.
- `#!html <y>` - New Y location of the Hologram.
- `#!html <z>` - New Z location of the Hologram.

### `#!html /dh h movehere <hologram>` { #dh-h-movehere }

> Aliases: `mvhr`

Teleports the given hologram to your location.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h update <hologram>` { #dh-h-update }

Hode the hologram and then Show it again.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h disable <hologram>` { #dh-h-disable }

> Aliases: `off`

Disable a hologram. While disabled, it won't be displayed to anyone.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h enable <hologram>` { #dh-h-enable }

> Aliases: `on`

Enable a hologram.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h center <hologram>` { #dh-h-center }

Moves a hologram into the center of the block on its current X and Z location.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h align <hologram> {X|Y|Z|XZ} <otherHologram>` { #dh-h-align }

Moves a hologram to the location of the other hologram on a specified axis.

- `#!html <hologram>` - Name of the Hologram.
- `{X|Y|Z|XZ}` - Aligns the hologram on the X, Y, Z or X and Z axis of the `<otherHologram>`.
- `#!html <otherHologram>` - Name of the other Hologram.

### `#!html /dh h setfacing <hologram> <facing>` { #dh-h-setfacing }

> Aliases: `facing`, `face`

Set the rotation of hologram facing (yaw). Only affects `#HEAD:`, `#SMALLHEAD:` and `#ENTITY:` content lines.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <facing>` - Angle of rotation in degrees, or a cardinal direction (`NORTH`, `EAST`, `SOUTH` or `WEST`).

### `#!html /dh h downorigin <hologram> {true|false}` { #dh-h-downorigin }

Sets the value of down origin. If true, hologram's location will be relative to its bottom.

- `#!html <hologram>` - Name of the Hologram.

### `#!html /dh h near <distance>` { #dh-h-near }

Lists of holograms in the specified distance from you.

- `#!html <distance>` - Distance to check in blocks.

### `#!html /dh h setdisplayrange <hologram> <range>` { #dh-h-setdisplayrange }

Set maximum distance a player can be from a hologram to see it.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <range>` - Range in blocks.

### `#!html /dh h setupdaterange <hologram> <range>`

Set maximum distance a player can be from a hologram to see it's updates.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <range>` - Range in blocks.

### `#!html /dh h setupdateinterval <hologram> <interval>`

Set update interval.

- `#!html <hologram>` - Name of the Hologram.
- `#!html <interval>` - Interval in ticks (20 ticks = 1 sec.).