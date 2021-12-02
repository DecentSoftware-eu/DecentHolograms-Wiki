---
description: General usage and editting of Holograms.
---

# 🖥 Setup

## Features

* Holograms are made 100% using packets, there are no real entites in your worlds which gives us a lot of possibilities when it comes to per-player behaviour.
* Holograms can have multiple pages.
* Holograms can be clickable with many click action options.
* Hologram lines have a system for text animations.
* Hologram lines can be offset off the parent Hologram center.
* You can setup permissions to view Holograms or Hologram lines.
* There are a few preset features like Damage & Heal displays.
* And much more...

## Permissions

DecentHolograms is a plugin made for server admins, therefore it doesn't need multiple different permission nodes for different actions. So, there is just one permission node you need to be able to do everything with DecentHolograms. And that is:

{% hint style="success" %}
dh.admin
{% endhint %}

## Editting Holograms

This is a simple tutorial to get started with editting holograms. Full list of all commands is [here](commands/).

### Create a hologram [\[more\]](commands/hologram.md)

You can simply create a hologram using the following command.

{% hint style="success" %}
/dh create \<name>
{% endhint %}

### Edit lines [\[more\]](commands/hologram-line.md)

Possible line types and content for hologram lines can be found [here](format/).

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

You can add more pages and navigate between them.

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

Here is a little example of how you could create a new hologram with some lines and pages.

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

To allow players to navigate between pages, you can simply do:

{% hint style="success" %}
/dh page addaction example 1 RIGHT NEXT\_PAGE

/dh page addaction example 2 LEFT PREV\_PAGE
{% endhint %}

Now, when a player RIGHT clicks the first page, he will be switched to the next page and when he LEFT clicks the second page, he will be switched back to the first one.&#x20;

#### You can also switch to a specific page

{% hint style="info" %}
/dh page addaction example 2 RIGHT PAGE:1
{% endhint %}

There are more actions, all of them are explained [here](../advanced/actions.md).

### Conclusion

And that's basically it. Of course, you can do much more with DecentHolograms. You can find all available commands [here](commands/). If you need any help, contact us on [Discord](https://discord.decentsoftware.eu).
