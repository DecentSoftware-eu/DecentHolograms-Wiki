---
title: Hologram
description: General usage and editing of Holograms
---

--8<-- "arguments.md"

## Commands

**Aliases:** `hologram`, `holo`, `h`  
**Permission:** `dh.command.holograms`

/// info | Command help
For a list of all available subcommands run the following command:  
```
/dh h help
```
///

----

### `#!command /dh h addflag <hologram> <flag>` { #dh-h-addflag }

:   **Permission:** `dh.command.holograms.addflag`
    
    Adds a [flag](../flags.md) to a hologram.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <flag>` - Name of the [Flag](../flags.md) to add.

----

### `#!command /dh h align <hologram> {X|Y|Z|XZ|FACING} <otherHologram>` { #dh-h-align }

:   **Permission:** `dh.command.holograms.align`
    
    Moves a hologram to the location of the other hologram on a specified axis.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command {X|Y|Z|XZ|FACING}` - Aligns the hologram on either the X, Y, Z, or X and Z axis of the `#!command <otherHologram>`, or sets the same facing angle as the `#!command <otherHologram>`.
    - `#!command <otherHologram>` - Name of the other Hologram.

----

### `#!command /dh h center <hologram>` { #dh-h-center }

:   **Permission:** `dh.command.holograms.center`
    
    Moves a hologram into the center of the block on its current X and Z location.
    
    - `#!command <hologram>` - Name of the Hologram.

----

### `#!command /dh h clone <hologram> <name> [temp] [-l:<world>:<x>:<y>:<z>]` { #dh-h-clone }

:   **Aliases:** `copy`  
    **Permission:** `dh.command.holograms.clone`
    
    Clone an existing hologram.
    
    - `#!command <hologram>` - Name of the Hologram to clone.
    - `#!command <name>` - Name of the new, clones Hologram.
    - `#!command [temp]` - Optional boolean to set, whether the cloned hologram should be temporary (not save to file) or not. Default is `false`
    - `#!command [-l:<world>:<x>:<y>:<z>]` - Optional location argument, which allows you to specify the location where the cloned hologram should be placed. This argument can also be used by console users to execute the command.
    
    /// example | Examples
    ```
    /dh h clone test test_clone
    /dh h clone test test_clone true
    /dh h clone test test_clone -l:world:0:100:0
    /dh h clone test test_clone true -l:world:0:100:0
    ```
    ///

----

### `#!command /dh h create <name> [-l:<world>:<x>:<y>:<z>] [content]` { #dh-h-create }

:   **Aliases:** `create`, `c`  
    **Permission:** `dh.command.holograms.create`
    
    Create a new hologram.
    
    - `#!command <name>` - Name of the created Hologram.
    - `#!command [-l:<world>:<x>:<y>:<z>]` - Optional location argument, which allows you to specify the location where the hologram should be placed. This argument can also be used by console users to execute the command.
    - `#!command [content]` - Content of the first line. (Optional)
   
    /// example | Examples
    ```
    /dh h create test
    /dh h create test -l:world:0:100:0
    /dh h create test First Line
    /dh h create test -l:world:0:100:0 First Line
    ```
    ///

----

### `#!command /dh h delete <hologram>` { #dh-h-delete }

:   **Aliases:** `del`, `remove`, `rem`  
    **Permission:** `dh.command.holograms.delete`
    
    Delete an existing hologram.
    
    - `#!command <hologram>` - Name of the Hologram.

----

### `#!command /dh h disable <hologram>` { #dh-h-disable }

:   **Aliases:** `off`  
    **Permission:** `dh.command.holograms.disable`
    
    Disable a hologram. While disabled, it won't be displayed to anyone.
    
    - `#!command <hologram>` - Name of the Hologram.

----

### `#!command /dh h downorigin <hologram> {true|false}` { #dh-h-downorigin }

:   **Permission:** `dh.command.holograms.downorigin`
    
    Sets the value of down origin. If true, hologram's location will be relative to its bottom.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command {true|false}` - Whether the hologram's location should be relative to its bottom line or not.

----

### `#!command /dh h enable <hologram>` { #dh-h-enable }

:   **Aliases:** `on`  
    **Permission:** `dh.command.holograms.enable`
    
    Enable a hologram.
    
    - `#!command <hologram>` - Name of the Hologram.

----

### `#!command /dh h info <hologram>` { #dh-h-info }

:   **Permission:** `dh.command.holograms.info`
    
    Prints some general info about a hologram.
    
    - `#!command <hologram>` - Name of the Hologram.

----

### `#!command /dh h lines <hologram> <page> [listPage]` { #dh-h-lines }

:   **Permission:** `dh.command.holograms.lines`
    
    Lists all the holograms lines.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <page>` - Page to list the lines of.
    - `#!command [listPage]` - Optional page in the list to move to.

----

### `#!command /dh h move <hologram> <x> <y> <z>` { #dh-h-move }

:   **Aliases:** `mv`  
    **Permission:** `dh.command.holograms.move`
    
    Teleports the given hologram to the given coordinates.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <x>` - New X location of the Hologram.
    - `#!command <y>` - New Y location of the Hologram.
    - `#!command <z>` - New Z location of the Hologram.

----

### `#!command /dh h movehere <hologram>` { #dh-h-movehere }

:   **Aliases:** `mvhr`  
    **Permission:** `dh.command.holograms.movehere`
    
    Teleports the given hologram to your location.
    
    - `#!command <hologram>` - Name of the Hologram.

----

### `#!command /dh h near <distance>` { #dh-h-near }

:   **Permission:** `dh.command.holograms.near`
    
    Lists of holograms in the specified distance from you.
    
    - `#!command <distance>` - Distance to check in blocks.

----

### `#!command /dh h removeflag <hologram> <flag>` { #dh-h-removeflag }

:   **Permission:** `dh.command.holograms.removeflag`
    
    Removes a [flag](../flags.md) from the hologram.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <flag>` - Name of the [Flag](../flags.md) you want to remove.

----

### `#!command /dh h rename <hologram> <new_name>` { #dh-h-rename }

:   **Permission:** `dh.command.holograms.rename`
    
    Rename an existing hologram.
    
    - `#!command <hologram>` - Name of the Hologram, you want to rename.
    - `#!command <new_name>` - The Hologram's new name.

----

### `#!command /dh h setdisplayrange <hologram> <range>` { #dh-h-setdisplayrange }

:   **Permission:** `dh.command.holograms.setdisplayrange`
    
    Set maximum distance a player can be from a hologram to see it.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <range>` - Number between `1` and `64` to set the display range in blocks.

----

### `#!command /dh h setfacing <hologram> <facing>` { #dh-h-setfacing }

:   **Aliases:** `facing`, `face`, `setface`  
    **Permission:** `dh.command.holograms.setfacing`
    
    Set the rotation of hologram facing (yaw). Only affects `#HEAD:`, `#SMALLHEAD:` and `#ENTITY:` content lines.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <facing>` - Number between `-180.0` and `180.0` for a specific angle, or a cardinal direction (`NORTH`, `EAST`, `SOUTH` or `WEST`).

----

### `#!command /dh h setpermission <hologram> [permission]` { #dh-h-setpermission }

:   **Aliases:** `permission`, `setperm`, `perm`  
    **Permission:** `dh.command.holograms.setpermission`
    
    Set the current permission required to view the hologram.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command [permission]` - Permission required for a hologram to be seen. Leave empty to remove any permission.

----

### `#!command /dh h setupdateinterval <hologram> <interval>`

:   **Aliases:** `updateinterval`  
    **Permission:** `dh.command.holograms.setupdateinterval`
    
    Set update interval.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <interval>` - Number between `1` and `1200` to set the interval in ticks (20 ticks = 1 sec.).

----

### `#!command /dh h setupdaterange <hologram> <range>`
  
:   **Permission:** `dh.command.holograms.setupdaterange`
    
    Set maximum distance a player can be from a hologram to see it's updates.
    
    - `#!command <hologram>` - Name of the Hologram.
    - `#!command <range>` - Number between `1` and `64` to set the update range in blocks.

----

### `#!command /dh h teleport <hologram>` { #dh-h-teleport }

:   **Aliases:** `tele`, `tp`  
    **Permission:** `dh.command.holograms.teleport`
    
    Teleports you to the given hologram.
    
    - `#!command <hologram>` - Name of the Hologram.

----

### `#!command /dh h update <hologram>` { #dh-h-update }
  
:   **Permission:** `dh.command.holograms.update`
    
    Hide the hologram and then Show it again.
    
    - `#!command <hologram>` - Name of the Hologram.
