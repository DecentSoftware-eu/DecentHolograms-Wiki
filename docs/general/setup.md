---
title: Setup
description: How to use DecentHolograms

icon: material/monitor
---

## Permissions

DecentHolograms is a plugin specifically designed for server administrators and as such, it simplifies permissions by requiring only one permission node, `dh.admin`, to access all of its features and functionality.

## Commands

With a wide range of commands, effectively utilizing this plugin may require a basic understanding of some general rules. This will be helpful to work with the commands effectively.

### Arguments

--8<-- "arguments.md:2"

### Tab Completion

The majority of commands and sub-commands feature tab-completion functionality, which can be used to quickly type commands and determine valid values for arguments.

## Editing Holograms

The below section will give you a basic example of creating and managing a hologram. For more info, visit the following pages:

<div class="grid cards" markdown>

- ### [:material-floppy: Format & Colors](format-and-colors/index.md)
- ### [:material-keyboard: Commands](commands/index.md)

</div>

## Hologram Creation Example

Here is an example of how to create a new hologram with multiple lines and pages using the available commands.

### Create the hologram

:   /// info | To execute as console, you have to add the `-l:<world>:<x>:<y>:<z>` argument.
    ///
    
    ```
    /dh create example
    ```
    
    ![creating a hologram](../assets/images/setup/hologram-create.png){ loading="lazy" }

### Edit lines

:   
    ```
    /dh line set example 1 1 &3&lDECENT HOLOGRAMS  
    /dh line add example 1 &fHolograms plugin
    ```
    
    ![editing a hologram](../assets/images/setup/hologram-edit.png){ loading="lazy" }

### Add another page

:   You can have as many pages as you'd like.
    
    ```
    /dh page add example
    /dh page switch example 2
    ```
    
    ![adding a page to a hologram](../assets/images/setup/hologram-page.png){ loading="lazy" }

### Setup actions

:   To allow players to navigate between pages, you can simply do this:
    
    ```
    /dh page addaction example 1 RIGHT NEXT_PAGE
    /dh page addaction example 2 LEFT PREV_PAGE
    ```
    
    This allows players to navigate between the pages by left/right-clicking the hologram.  
    More actions are available and can be found [here](actions.md).    

## Conclusion

That concludes the basic overview of how to use DecentHolograms. The plugin offers many more advanced features and functionality, all of which can be found in the command reference page. If you need any assistance, please don't hesitate to reach out to us on our Discord channel.