---
description: >-
  This page covers general usage and editing of holograms, including
  instructions on how to create, modify and manage them.
---

# 🖥 Setup

## Permissions

DecentHolograms is a plugin specifically designed for server administrators and as such, it simplifies permissions by requiring only one permission node, 'dh.admin', to access all of its features and functionality.

{% hint style="success" %}
dh.admin
{% endhint %}

## Commands

With a wide range of commands, effectively utilizing this plugin may require a basic understanding of some general rules. This will be helpful to work with the commands effectively.

### Arguments

Parenthesis only specify the type of an argument, they are not part of the final command.

| Parenthesis | Meaning                  |
| ----------- | ------------------------ |
| <>          | Required argument.       |
| \[]         | Optional argument.       |
| {}          | List of possible values. |

### Tab Completion

The majority of commands and sub-commands feature tab-completion functionality, which can be used to quickly type commands and determine valid values for arguments.

## Editing Holograms

This tutorial provides a basic guide for editing holograms, including instructions for creating and modifying them. For a complete list of commands, please refer to [this page](commands/).

### Create a hologram [\[more\]](commands/hologram.md)

Creating a hologram is easy, simply use the command specified below to get started.

{% hint style="success" %}
/dh create \<name> \[initial content]
{% endhint %}

**TIP!** By default, the hologram will spawn with a single line that reads "Blank Line." You can change the default line content in the [config.yml](configuration/config.md) file or specify the content in the command as shown in the example provided.

### Edit lines [\[more\]](commands/hologram-line.md)

A full list of possible line types and content for hologram lines can be found on [this page](format/).

#### Add a line

{% hint style="success" %}
/dh line add \<hologram> \<page> \<content>
{% endhint %}

#### Set a line

{% hint style="success" %}
/dh line set \<hologram> \<page> \<line> \<content>
{% endhint %}

#### Remove a line

{% hint style="success" %}
/dh line remove \<hologram> \<page> \<line>
{% endhint %}

### Edit pages [\[more\]](commands/hologram-pages.md)

Our holograms support multiple pages, allowing you to add additional content and navigate between them easily.

#### Add a page

{% hint style="success" %}
/dh page add \<hologram>
{% endhint %}

#### Remove a page

{% hint style="success" %}
/dh page remove \<hologram> \<page>
{% endhint %}

#### View a page

{% hint style="success" %}
/dh page switch \<hologram> \<page>
{% endhint %}



## Hologram Creation Example

Here is an example of how to create a new hologram with multiple lines and pages using the available commands.

### Create the hologram

{% hint style="success" %}
/dh create example
{% endhint %}

![](../.gitbook/assets/2021-11-30\_19.25.58.png)

### Edit lines

{% hint style="success" %}
/dh line set example 1 1 &3\&lDECENT HOLOGRAMS

/dh line add example 1 \&fHologram plugin
{% endhint %}

![](../.gitbook/assets/2021-11-30\_19.30.18.png)

### Add another page

You can have as many pages as you'd like.

{% hint style="success" %}
/dh page add example

/dh page switch example 2
{% endhint %}

![](../.gitbook/assets/2021-11-30\_19.34.46.png)

### Setup actions

To allow players to navigate between pages, you can simply do this:

{% hint style="success" %}
/dh page addaction example 1 RIGHT NEXT\_PAGE

/dh page addaction example 2 LEFT PREV\_PAGE
{% endhint %}

By setting up appropriate click actions, players can navigate between the pages by right-clicking the first page to switch to the next page, and left-clicking the second page to switch back to the first one.

#### You can also switch to a specific page

{% hint style="info" %}
/dh page addaction example 2 RIGHT PAGE:1
{% endhint %}

We offer a variety of click actions, all of which are explained in detail on [this page](actions.md).

### Conclusion

That concludes the basic overview of how to use DecentHolograms. The plugin offers many more advanced features and functionality, all of which can be found in the command reference page. If you need any assistance, please don't hesitate to reach out to us on our Discord channel.
