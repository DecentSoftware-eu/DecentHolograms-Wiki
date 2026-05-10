---
title: Create your first Hologram
description: This guide explains how to create your first Hologram.
---

This page aims to explain how to create your first hologram with DecentHolograms.  
It expects you to have the proper permissions for using the `/dh` commands shown. Refer to the command pages for their respective permissions or use `decentholograms.admin` to have all permissions.

## Choosing Hologram Types

Since `2.10.0` does DecentHolograms provide two types of Holograms: Armor Stand based and Display Entity based.  
Most people may be familiar with the Armor Stand ones, while others may be more familiar with the Display Entity ones.

It's important to note that not only are Display Entity based ones using  a separate storage folder and sub-command ([`/dh displays ...`](../commands/displays/index.md)) but it also has some features not available through the Armor Stand one. Where necessary will these differences be pointed out.

## 1. Create your Hologram

To create your first hologram, simply execute [`/dh h create <name>`](../commands/hologram/create.md) or [`/dh displays create <type> <name>`](../commands/displays/create.md).  
This will create a Hologram that is positioned at your current location.

Both commands support an additional argument at the end, which sets the text that should be displayed at first. If not present will it default to the default text set in the config.yml.

The `/dh h create` command provides two additional arguments named `-l:<world>:<x>:<y>:<z>` and `--center`.  
The first one is for spawning the Hologram at specific coordinates while the second one is used to center the hologram to the block.

## 2. Change Lines

Hologram lines can be edited in various ways. The main commands you probably will use are [`/dh l set ...`](../commands/hologram-lines/set.md) and [`/dh l add ...`](../commands/hologram-lines/add.md), or [`/dh displays setline ...`](../commands/displays/setline.md) and [`/dh displays addline ...`](../commands/displays/addline.md) respectively.

The set(line) command replaces a specific line with whatever content you provide, while the add(line) command adds a new line to the already existing one at the bottom.

Note that Armor Stand based Holograms can utilize [line types](../features/line-content.md) while Display Entities are limited to the Type you specified when creating the Hologram.

## 3. Add pages

/// info | This feature is not available for Display Entity Holograms.
///

DecentHolograms offers pages, allowing you to split content up into different parts that you can switch in between.  
To add a page, simply run [`/dh p add <name>`](../commands/hologram-pages/add.md). Just like when creating the Hologram does this command offer an optional argument to set the initial line content of the new page.

To switch to the new page, either execute [`/dh p switch <name> <page>`](../commands/hologram-pages/switch.md) or setup Page Actions (Explained below).

## 4. Add Page Actions

/// info | This feature is not available for Display Entity Holograms.
///

DecentHolograms provides a [collection of actions](../features/actions.md) that you can set per hologram-page to perform certain actions on left or right clicking the Hologram.  
As an example, to allow a player to switch to our previously created page, we can execute [`/dh p addaction <name> <page> <type> <action>`](../commands/hologram-pages/addaction.md) where `<type>` is the click type (i.e. `RIGHT`) and `<action>` the Click Action, which in our case would be `NEXT_PAGE`.

This would now make the Hologram switch to the next page when the player right-clicks it while displaying the 1st page.