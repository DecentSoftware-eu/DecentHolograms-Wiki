# 🦿 Animations

DecentHolograms supports two types of animations: premade and custom. Custom animations can be configured in files and the process of doing so is explained in more detail on [this page](configuration/animation.md).

### Format

General format of animations.

{% hint style="success" %}
<#ANIM:\<name>\[:args]>Text\</#ANIM>
{% endhint %}

**NOTE!** To use placeholders inside animations, you need to enable the feature in the [config.yml](configuration/config.md) file.

## Premade Animations

There are some premade animations you can use, that will work with any text.

### Colors

`<#ANIM:colors>Text</#ANIM>`

Or:

`&uText`

### Wave

`<#ANIM:wave:<color1>,<color2>>Text</#ANIM>`

Example:

`<#ANIM:wave:&f,&b&l>Text</#ANIM>`

### Burn

`<#ANIM:burn:<color1>,<color2>>Text</#ANIM>`

Example:

`<#ANIM:burn:&f,&b&l>Text</#ANIM>`

### Typewriter

`<#ANIM:typewriter>Text</#ANIM>`

### Scroll

`<#ANIM:scroll>Text</#ANIM>`
