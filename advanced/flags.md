---
description: General usage of flags.
---

# 🚩 Flags

In DecentHolograms, you can configure various flags on holograms and hologram lines. These flags mostly disable some functionality that you don't want or need.

{% hint style="info" %}
A flag in Hologram affects all its Lines but different Lines can have different flags without affecting each other or the parent Hologram.&#x20;
{% endhint %}

### List of Flags

These are the flags, that are currently available.

* DISABLE\_UPDATING - Disables updating for hologram or line.
* DISABLE\_PLACEHOLDERS - Disables placeholders for hologram or line.
* DISABLE\_ANIMATIONS - Disables animations for hologram or line.
* DISABLE\_ACTIONS - Disables click actions for hologram.

### Commands

You can configure flags using the following commands. All these commands have Tab-Complete so you don't need to type everything manually.&#x20;

For holograms:

{% hint style="success" %}
/dh h addflag \<hologram> \<flag>

/dh h removeflag \<hologram> \<flag>
{% endhint %}

* [ ] \<hologram> - Name of the hologram.
* [ ] \<flag> - Name of the flag.

For hologram lines:

{% hint style="success" %}
/dh l addflag \<hologram> \<page> \<line> \<flag>

/dh l removeflag \<hologram> \<page> \<line> \<flag>
{% endhint %}

* [ ] \<hologram> - Name of the hologram.
* [ ] \<page> - Index of the hologram page, this line is located on.
* [ ] \<line> - Number of line in the hologram.
* [ ] \<flag> - Name of the flag.
