---
description: General formatting of hologram line content.
---

# 📃 Format

## Hologram Line Types

There are multiple different types of Hologram Line content. If other than text, the type must be defined in the lines content. (#\<type>: ...)

<img src="../../.gitbook/assets/image.png" alt="" data-size="original">

### Text

Just a text line, you can enter any text, use PAPI placeholders, [colors](colors.md) and [animations](../animations.md).&#x20;

#### Example text line:

{% hint style="success" %}
\&fThis is a \&btext line\&f.
{% endhint %}

### Icon

Icon line is just a floating item. You can use any material, create player heads, use PAPI placeholders or modify NBT data.

#### Format:

{% hint style="success" %}
\#ICON: MATERIAL:DATA\_VALUE (skull\_texture) {NBT}
{% endhint %}

Of course, you don't have to enter all of the parameters. Here are a few examples:

{% hint style="info" %}
_// Red Wool (<1.13):_

\#ICON: WOOL:14

_// Light Blue Leather Chestplate:_

\#ICON: LEATHER\_CHESTPLATE {display:{color:3847130\}}
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

Some Materials and Entity Types will only work on certain versions. For example, you can't use Entity Type AXOLOTL on 1.8 server.

### Player Heads

There are three ways you can create player heads.

{% hint style="warning" %}
For versions below 1.13, use SKULL\_ITEM instead of PLAYER\_HEAD material.
{% endhint %}

{% hint style="info" %}
We used ICON as the line type but these will also work with HEAD and SMALLHEAD.
{% endhint %}

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
