---
description: General formatting of hologram line content.
---

# 💾 Format & Colors

## Hologram Line Types

DecentHolograms supports various types of content for hologram lines, including text, items, and entities. If the content is not text, the type must be defined in the line's content using the following format.

{% hint style="success" %}
\#\<type>: \<content>
{% endhint %}

<img src="../../.gitbook/assets/image.png" alt="" data-size="original">

### Text

A text line allows you to enter any text, including PAPI placeholders, colors and animations. You can use this type of line to display dynamic and personalized information to players.

#### Example text line:

{% hint style="success" %}
\&fThis is a \&btext line\&f.
{% endhint %}

### Icon

An Icon line displays a floating item, which can be any material, player head, PAPI placeholders, or modified NBT data.

#### Format:

{% hint style="success" %}
\#ICON: MATERIAL\[:DATA\_VALUE] \[(skull\_texture)] \[{NBT}]
{% endhint %}

Of course, you don't have to enter all of the parameters. Here are a few examples:

{% hint style="info" %}
_// Red Wool (<1.13):_

\#ICON: WOOL:14

_// Light Blue Leather Chestplate:_

\#ICON: LEATHER\_CHESTPLATE {display:{color:3847130\}}

_// d0by's head (1.13+, use SKULL\_ITEM in lower versions):_

\#ICON: PLAYER\_HEAD (d0by)
{% endhint %}

### Head

Head lines are displayed as a helmet of normal-size armor stand.

Format is the same as format for [Icons](./#icon) except that you start with:

{% hint style="success" %}
\#HEAD:
{% endhint %}

#### Examples:

{% hint style="info" %}
_// d0by's head (1.13+, use SKULL\_ITEM in lower versions):_

\#HEAD: PLAYER\_HEAD (d0by)

_// Grass block:_

\#HEAD: GRASS\_BLOCK
{% endhint %}

### Small Head

The same thing as [Head](./#head) but on a small armor stand.

{% hint style="success" %}
\#SMALLHEAD:
{% endhint %}

### Entity

Yes, you can even display entities. All entity types can be found [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html). Not all entity types will work on all versions, it depends on your server version.

#### Format:

{% hint style="success" %}
\#ENTITY: ENTITY\_TYPE
{% endhint %}

#### Examples:

{% hint style="info" %}
\#ENTITY: PIG

\#ENTITY: AXOLOTL
{% endhint %}

## Additional Information

It's important to note that certain materials and entity types may only be available on specific server versions. For example, using the Entity Type AXOLOTL on a 1.8 server will not work. Be sure to check the compatibility of the materials and entity types you wish to use with your server version.

### Player Heads

There are three methods to create player heads, all of which are shown in the examples below.

#### Player Name:

{% hint style="success" %}
\#ICON: PLAYER\_HEAD (d0by)
{% endhint %}

#### PAPI Placeholder:

This would display a different head to each player.

{% hint style="success" %}
\#ICON: PLAYER\_HEAD (%player\_name%)
{% endhint %}

#### Texture:

You can use a Base64 string textures.

{% hint style="success" %}
\#ICON: PLAYER\_HEAD (`eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODE2ZjAwNzNjNTg3MDNkOGQ0MWU1NWUwYTNhYmIwNDJiNzNmOGMxMDViYzQxYzJmMDJmZmUzM2YwMzgzY2YwYSJ9fX0=`)
{% endhint %}

#### Notes

{% hint style="warning" %}
For server versions below 1.13, please use the SKULL\_ITEM material instead of PLAYER\_HEAD when creating player head holograms.
{% endhint %}

{% hint style="info" %}
Please note that the examples provided below use the ICON line type, but the same methods can also be used with the HEAD and SMALLHEAD line types.
{% endhint %}
