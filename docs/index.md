---
title: Welcome
subtitle: Welcome to the DecentHolograms Wiki!

icon: material/home
hide_icon: true
---

## What's DecentHolograms?

DecentHolograms is a very versatile hologram plugin that offers a wide range of features and customization options, making it easy to create unique and personalized holograms.

With a user-friendly command interface, you can easily create and customize holograms without the need to edit any configuration files.

## Features

<div class="grid cards" markdown>

-   ### Packet-based
    
    ----
    
    All Holograms are packet-based, meaning they only exist for the client, but not for the server, eliminating the need for physical entities on the Server that eats up resources.  
    It also opens the door for various per-player features such as parsing placeholders for the player looking on the Hologram

-   ### Multiple Pages
    
    ----
    
    A hologram can have multiple pages to display to players, allowing you to split large amounts of information up into smaller parts that a player can go through, while keeping everything in a single Hologram.

-   ### Interactions
    
    ----
    
    Holograms can be interacted with by the player.  
    Using [click actions](features/actions.md), you can send messages, execute commands, switch servers, switch pages and more for when a player left- or right-clicks a Hologram.

-   ### Animations
    
    ----
    
    Holograms offer the option of text-based animations to be displayed. This includes [built-in animations](features/animations/index.md) and [custom animations](features/animations/custom-animations.md) to show.

-   ### Line-offsets
    
    ----
    
    Want to have the text all be aligned to the left? Using [x-offset](commands/hologram-lines/offsetx.md) and [z-offset](commands/hologram-lines/offsetz.md) commands, one can align individual lines on the X and Z axis respectively. This however does not make them always align properly from all angles.

-   ### Permissions
    
    ----
    
    You can asign a permission that a player needs to see a specific [hologram](commands/hologram/setpermission.md) or even [hologram line](commands/hologram-lines/setpermission.md).  
    This allows you to display content based on certain conditions.

-   ### Multiple Line Types
    
    ----
    
    DecentHolograms allows you to display more than just basic text. It allows you to display [floating items](features/line-content.md#icon), Blocks/Items as a [(small) Armor Stand head](features/line-content.md#head-smallhead) or even [Entities](features/line-content.md#entity).

-   ### API
    
    ----
    
    An [extensive API](api/get-started.md) is offered, allowing other plugins to hook easily into DecentHolograms and make and manage their own Holograms with all the features offered by DecentHolograms itself.

</div>

## Useful link

### Official Downloads

DecentHolograms can be downloaded from the below listed pages.  
**Any other page offering DecentHolograms for download is doing so without our permission and may even share malware!**

/// html | div.grid.cards
- [:simple-modrinth: Modrinth](https://modrinth.com/plugin/decentholograms){ target="_blank" rel="noopener" }
- [:simple-spigotmc: SpigotMC](https://www.spigotmc.org/resources/96927/){ target="_blank" rel="noopener" }
- [:simple-github: GitHub](https://github.com/DecentSoftware-eu/DecentHolograms){ target="_blank" rel="noopener" }
///

### Other Links

/// html | div.grid.cards
- [:simple-discord: Discord Server](https://discord.decentsoftware.eu){ target="_blank" rel="noopener" }
- [:octicons-graph-24: bStats (Plugin Statistics)](https://bstats.org/plugin/bukkit/DecentHolograms/12797){ target="_blank" rel="noopener" }
- [:octicons-bug-24: Issue Tracker](https://github.com/DecentSoftware-eu/DecentHolograms/issues){ target="_blank" rel="noopener" }
///
