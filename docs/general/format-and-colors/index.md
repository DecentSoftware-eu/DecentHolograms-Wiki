---
title: Format & Colors
description: Information about what formats DecentHologram offers

icon: material/floppy
---

DecentHologram allows to display more than just text. Using a specific pattern, one can display a floating item, item as a head of a (small) armor stand or even entities.

![example](../../assets/images/format/line-types.png){ loading="lazy" }

/// note | Placeholders
Internal placeholders and placeholders from PlaceholderAPI can be used in text lines but also the other line types.  
As an example: Instead of a player name can you use `{player}` to display the head of who is looking at the hologram.
///

## Text Line

This is the default line type used by DecentHolograms. Only when the Line follows a specific pattern (Shown below) will the displayed content not be a floating text.

/// tab | Format
```command
<text>
```
///

/// tab | Example
```command
&aThis is a normal &f&lText Line&a!
```
///

----

## `#!command #ICON: <item>` { #icon }

Displays a floating item in the Hologram.  
Do keep in mind that the item will spin around, which can't be disabled by the plugin. If you want non-moving items, use the [`#HEAD`](#head) or [`#SMALLHEAD`](#smallhead) Line Type.

/// tab | Format
```command
#ICON: <item>[:<data>] [options]
```

--8<-- "format-options.md"
///

/// tab | Examples
```
/// Red Wool (Only works on versions before 1.13)
#ICON: WOOL:14

/// Light Blue Leather Chestplate
#ICON: LEATHER_CHESTPLATE {display:{color:3847130}}

/// Player Head of d0by (Use SKULL_ITEM on versions before 1.13)
#ICON: PLAYER_HEAD (d0by)
```
///

----

## `#!command #HEAD: <item>` { #head }

Displays the item/block as an armor stand's Head gear.  
Items displayed this way won't rotate, but may have a visible offset to the Hologram's center.

/// tab | Format
```command
#HEAD: <item>[:<data>] [options]
```

--8<-- "format-options.md"
///

/// tab | Examples
```
/// Player Head of d0by (Use SKULL_ITEM on versions before 1.13)
#HEAD: PLAYER_HEAD (d0by)

/// Grass Block
#HEAD: GRASS_BLOCK
```
///

----

## `#!command #SMALLHEAD: <item>` { #smallhead }

Displays the item/block as a small armor stand's Head gear.  
Items displayed this way won't rotate, but may have a visible offset to the Hologram's center.

/// tab | Format
```command
#SMALLHEAD: <item>[:<data>] [options]
```

--8<-- "format-options.md"
///

/// tab | Examples
```
/// Player Head of d0by (Use SKULL_ITEM on versions before 1.13)
#SMALLHEAD: PLAYER_HEAD (d0by)

/// Grass Block
#SMALLHEAD: GRASS_BLOCK
```
///

----

## `#!command #ENTITY: <entity>` { #entity }

Displays an entity. A list of all available entities can be found [here][entities]{ target="_blank" rel="nofollow" }.

/// note | Notes
- The entity will be displayed in a sitting position, if it has one. This can't be changed.
- Certain Entity types can not be used in the Hologram. A list can be seen [here][blacklist]{ target="_blank" rel="nofollow" } (Last updated: April 27th, 2024).

[entities]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html
[blacklist]: https://github.com/DecentSoftware-eu/DecentHolograms/blob/f28df4373f4d56e17eb33005885222f726ac1350/src/main/java/eu/decentsoftware/holograms/api/utils/entity/DecentEntityType.java#L21-L51
///

/// tab | Format
```command
#ENTITY: <entity>
```
///

/// tab | Examples
```
#ENTITY: PIG
#ENTITY: AXOLOTL
```
///

----

## Additional Information

### Version-specific items/entities

You can only use items and entities that actually exist for the Server's Minecraft Version. In addition can the names be different for the same item/entity, if Mojang changed them in-between versions.  
As an example, the `GRASS` item was renamed to `SHORT_GRASS` in 1.20.4, meaning that on any version before it, you use `GRASS` while on 1.20.4 and newer you use `SHORT_GRASS`.

### Player Head Textures

The following options can be set for the `<value>` in `(<value>)`:

- Player name (i.e. `d0by`).
- Placeholder resolving to a Player name such as `{player}`. This will result in the player seeing their own head in the hologram.
- A Base64-encoded Texture String. You can find those on sites such as https://minecraft-heads.com{ target="_blank" rel="nofollow" } and are usually refered to as "value".
- `HEADDATABASE_<id>` where `<id>` is a number from https://minecraft-heads.com{ target="_blank" rel="nofollow" } (Requires the plugin [HeadDatabase](https://www.spigotmc.org/resources/14280/){ target="_blank" rel="nofollow" }).