---
title: 'Line Content'
description: 'The different Line Content Types'

icon: material/text
---

DecentHolograms supports different Types of Hologram Lines to display.  
Depending on the Line Type are there different options available for you to use.

## Text Line

This is the default type that is used when no other specific type, or an unknown one, is used.  
This line type supports Placeholders (both own and [PlaceholderAPI ones](compatability.md#placeholderapi)) and color and formatting codes.

### Colors and Formatting

The following options can be used for colors and formatting of text lines.

/// html | div.grid.cards
-   **Legacy Color Codes**
    
    ----  
    Basic color and formatting codes such as `&a` and `&l` can be used.

-   **RGB Colors**
    
    ----  
    RGB colors can be used using one of the following formats:
    
    - `#rrggbb`
    - `&#rrggbb`
    - `<#rrggbb>`
    - {% raw %}`{#rrggbb}`{% endraw %}

-   **Gradients**
    
    ----  
    Gradients can be created using `#!command <#rrggbb>text</#rrggbb>` where `<#rrggbb>` is the start and `</#rrggbb>` then end color.

-   **Rainbow Gradient**
    
    ----
    `#!command <RAINBOW:<int>></RAINBOW>` can be used to create a rainbow gradient for the text in-between the tags.  
    `#!command <int>` can be replaced with a number between 0 and 999 to create an offset for the rainbow.

-   **Rainbow (animated)**
    
    ----  
    An animated rainbow color similar to that of HolographicDisplays can be used by either using `<#ANIM:colors>Text</#ANIM>`, or by using `&u`.
///

/// example
```
Hello World!
```
///

## `#!command #ICON: <item>` { #icon }

Displays a floating item.  
The Item will spin around like any other dropped item. To avoid this, use a `#SMALLHEAD` or `#HEAD` Line Type.

The full format is `#!command #ICON: <item>[:<data>] [options]`:

--8<-- "format-options.md"

/// example | Examples
```
// Red wool (Only workds on 1.12 and older)
#ICON: WOOL:14

// Light Blue Leather Chestplate
#ICON: LEATHER_CHESTPLATE {display:{color:3847138}}

// Player Head of d0by
// Use SKULL_ITEM on versions before 1.13!
#ICON: PLAYER_HEAD (d0by)
```
///

## `#!command #HEAD: <item>` / `#!command #SMALLHEAD: <item>` { #head-smallhead }

The `#HEAD` and `#SMALLHEAD` Line types display a floating item or Block.  
Unlike the `#ICON` line type do the displayed items not spin or float up and down.

The line types use the head slot of an armor stand or small armor stand respectively to display the item/block.  
It is therefore possible that the item/block displays differently than with `#ICON` line types.

The full format is `#!command #HEAD: <item>[:<data>] [options]`:

--8<-- "format-options.md"

/// example | Examples
```
// These examples also apply to SMALLHEAD!

// Player Head of d0by (Use SKULL_ITEM on versions before 1.13)
#HEAD: PLAYER_HEAD (d0by)

// Grass Block
#HEAD: GRASS_BLOCK
```
///

## `#!command #ENTITY: <entity>` { #entity }

Displays an entity.  
For a list of available entity names, see [this page](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html){ target="_blank" rel="noopener" }.

/// note | Notes
- The linked page is for 26.1 (last checked: 07th of April, 2026) and may contain names of entities not available in your game version, or with a different name.
- Entities will be displayed in a sitting position, if one is available for them. This is a vanilla limitation and not fixable.
- Certain entities are blacklisted from being used in DecentHolograms. For a list of those, see [this page](https://github.com/DecentSoftware-eu/DecentHolograms/blob/e39d1abb3ddebbc93137f8006a563865639a51f8/plugin/src/main/java/eu/decentsoftware/holograms/api/utils/entity/DecentEntityType.java#L30-L80){ target="_blank" rel="noopener" } (Last updated: 07th of April, 2026).
///

/// example | Examples
```
#ENTITY: PIG
#ENTITY: AXOLOTL
```
///

## Additional Info

### Version Specific Items/Entities

Only items and entities available in your server's version can be used. It's not possible to display items and entities from newer MC versions (i.e. for newer clients) while not using that specific version for your server.

### Player Head Textures

Multiple types of values can be used for the `(<value>)` option in a `PLAYER_HEAD`/`SKULL_ITEM` item:

/// tab | Player Name
The name of a player can be used.

//// example
```
#ICON: PLAYER_HEAD (d0by)
```
////
///

/// tab | Placeholders
Placeholders - both from DH and PlaceholderAPI - that resolve into a player name or Texture value can be used.

//// example
```
#ICON: PLAYER_HEAD ({player})
```
////
///

/// tab | Base64-encoded Texture Value
A Base64-encoded texture value can be used. Such a value can be obtained from sites such as [minecraft-heads](https://minecraft-heads.com){ target="_blank" rel="noopener" }.  
They are often refered to as `value`.

//// example
The following example uses the Texture value from https://minecraft-heads.com/custom-heads/head/1

```
#ICON: PLAYER_HEAD (eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTYzNmRlZTgwNmJhNDdhMmM0MGU5NWI1N2ExMmYzN2RlNmMyZTY3N2YyMTYwMTMyYTA3ZTI0ZWVmZmE2In19fQ==)
```
////
///

/// tab | HeadDatabase Head
When HeadDatabase is installed and running can `HEADDATABASE_<id>` be used where `<id>` is the ID of a head on the [minecraft-heads](https://minecraft-heads.com){ target="_blank" rel="noopener" } website.  
The ID can usually be found within the URL.

//// example
The following example uses the ID 1 from https://minecraft-heads.com/custom-heads/head/1 using the HeadDatabase plugin.

```
#ICON: PLAYER_HEAD (HEADDATABASE_1)
```
////
///