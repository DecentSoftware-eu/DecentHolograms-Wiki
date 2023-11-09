---
title: Hologram
description: General usage and editing of Holograms
---

## Commands

> Aliases: `hologram`, `holo`, `h`

/// info | Command help
For a list of all available subcommands run the following command:  
```
/dh h help
```
///

### `#!command /dh h create <name> [-l:world:x:y:z] [content]` { #dh-h-create }

> Aliases: `create`, `c`
> 
> Create a new hologram.
> 
> - `#!command <name>` - Name of the created Hologram.
> - `#!command [-l:world:x:y:z]` - Optional location argument, which allows you to specify the location where the hologram should be placed. This argument can also be used by console users to execute the command.
> - `#!command [content]` - Content of the first line. (Optional)

### `#!command /dh h clone <hologram> <name> [temp] [-l:world:x:y:z]` { #dh-h-clone }

> Aliases: `copy`
> 
> Clone an existing hologram.
> 
> - `#!command <hologram>` - Name of the Hologram to clone.
> - `#!command <name>` - Name of the new, clones Hologram.
> - `#!command [temp]` - `true`, if you DON'T want the hologram to save, otherwise `false` (default). (Optional)
> - `#!command [-l:world:x:y:z]` - Optional location argument, which allows you to specify the location where the cloned hologram should be placed. This argument can also be used by console users to execute the command.
> 
> /// example | Examples
> ```
> /dh h clone test test_clone -l:world:0:100:0
> /dh h clone test test_clone true
> /dh h clone test test_clone
> /dh h clone test test_clone -l:world:0:100:0 false
> ```
> ///

### `#!command /dh h delete <hologram>` { #dh-h-delete }

> Aliases: `del`, `remove`, `rem`
> 
> Delete an existing hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h rename <hologram> <new_name>` { #dh-h-rename }

> Rename an existing hologram.
> 
> - `#!command <hologram>` - Name of the Hologram, you want to rename.
> - `#!command <new_name>` - The Hologram's new name.

### `#!command /dh h setpermission <hologram> [permission]` { #dh-h-setpermission }

> Aliases: `permission`, `setperm`, `perm`
> 
> Set the current permission required to view the hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command [permission]` - New permissio. (Leave empty to remove)

### `#!command /dh h info <hologram>` { #dh-h-info }

> Prints some general info about a hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h lines <hologram> [page]` { #dh-h-lines }

> Lists all the holograms lines.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command [page]` - Page of the list. (Optional)

### `#!command /dh h teleport <hologram>` { #dh-h-teleport }

> Aliases: `tele`, `tp`
> 
> Teleports you to the given hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h move <hologram> <x> <y> <z>` { #dh-h-move }

> Aliases: `mv`
> 
> Teleports the given hologram to the given coordinates.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <x>` - New X location of the Hologram.
> - `#!command <y>` - New Y location of the Hologram.
> - `#!command <z>` - New Z location of the Hologram.

### `#!command /dh h movehere <hologram>` { #dh-h-movehere }

> Aliases: `mvhr`
> 
> Teleports the given hologram to your location.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h update <hologram>` { #dh-h-update }

> Hode the hologram and then Show it again.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h disable <hologram>` { #dh-h-disable }

> Aliases: `off`
> 
> Disable a hologram. While disabled, it won't be displayed to anyone.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h enable <hologram>` { #dh-h-enable }

> Aliases: `on`
> 
> Enable a hologram.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h center <hologram>` { #dh-h-center }

> Moves a hologram into the center of the block on its current X and Z location.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h align <hologram> {X|Y|Z|XZ} <otherHologram>` { #dh-h-align }

> Moves a hologram to the location of the other hologram on a specified axis.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command {X|Y|Z|XZ}` - Aligns the hologram on the X, Y, Z or X and Z axis of the `#!command <otherHologram>`.
> - `#!command <otherHologram>` - Name of the other Hologram.

### `#!command /dh h setfacing <hologram> <facing>` { #dh-h-setfacing }

> Aliases: `facing`, `face`
> 
> Set the rotation of hologram facing (yaw). Only affects `#HEAD:`, `#SMALLHEAD:` and `#ENTITY:` content lines.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <facing>` - Angle of rotation in degrees, or a cardinal direction (`NORTH`, `EAST`, `SOUTH` or `WEST`).

### `#!command /dh h downorigin <hologram> {true|false}` { #dh-h-downorigin }

> Sets the value of down origin. If true, hologram's location will be relative to its bottom.
> 
> - `#!command <hologram>` - Name of the Hologram.

### `#!command /dh h near <distance>` { #dh-h-near }

> Lists of holograms in the specified distance from you.
> 
> - `#!command <distance>` - Distance to check in blocks.

### `#!command /dh h setdisplayrange <hologram> <range>` { #dh-h-setdisplayrange }

> Set maximum distance a player can be from a hologram to see it.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <range>` - Range in blocks.

### `#!command /dh h setupdaterange <hologram> <range>`

> Set maximum distance a player can be from a hologram to see it's updates.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <range>` - Range in blocks.

### `#!command /dh h setupdateinterval <hologram> <interval>`

> Set update interval.
> 
> - `#!command <hologram>` - Name of the Hologram.
> - `#!command <interval>` - Interval in ticks (20 ticks = 1 sec.).