# Hologram Pages

## Commands

You can simply view all commands for hologram pages using the following command.

{% hint style="success" %}
/dh pages help
{% endhint %}

### <mark style="color:blue;">/dh p add \<hologram> \[content]</mark>

Add a new page to a hologram.

* \<hologram> - Name of the hologram.
* \[content] - [Content](../format/) of the first line.

### <mark style="color:blue;">/dh p insert \<hologram> \<index></mark>

Insert a new page into a hologram.

* \<hologram> - Name of the hologram.
* \<index> - Index of the new page.

### <mark style="color:blue;">/dh p remove \<hologram> \<page></mark>

Remove a page from a hologram.

* \<hologram> - Name of the hologram.
* \<page> - Index of the page to remove.

### <mark style="color:blue;">/dh p swap \<hologram> \<page1> \<page2></mark>

Swap two pages in a hologram.

* \<hologram> - Name of the hologram.
* \<page1> - Index of the first page.
* \<page2> - Index of the second page.

### <mark style="color:blue;">/dh p switch \<hologram> \<page></mark>

Switch to another page in a hologram.

* \<hologram> - Name of the hologram.
* \<page> - Index of the page to view.

### <mark style="color:blue;">/dh p addaction \<hologram> \<page> \<clickType> \<action></mark>

Add an action to a hologram page.

* \<hologram> - Name of the hologram.
* \<page> - Index of the page.
* \<clickType> - ClickType that triggers this action. [\[Available ClickTypes\]](/advanced/actions.md#click-types)
* \<action> - The action. [\[Available Actions\]](/advanced/actions.md)

### <mark style="color:blue;">/dh p removeaction \<hologram> \<page> \<clickType> \<index></mark>

Remove action from page.

* \<hologram> - Name of the hologram.
* \<page> - Index of the page to view.
* \<clickType> - ClickType that triggers this action. [\[Available ClickTypes\]](/advanced/actions.md#click-types)
* \<index> - Index of the action.

### <mark style="color:blue;">/dh p clearactions \<hologram> \<page> \<clickType></mark>

Clear actions on specified click type in page.

* \<hologram> - Name of the hologram.
* \<page> - Index of the page to view.
* \<clickType> - The ClickType. [\[Available ClickTypes\]](/advanced/actions.md#click-types)

### <mark style="color:blue;">/dh p actions \<hologram> \<page> \<clickType></mark>

View actions set on specified click type in page.

* \<hologram> - Name of the hologram.
* \<page> - Index of the page to view.
* \<clickType> - The ClickType. [\[Available ClickTypes\]](/advanced/actions.md#click-types)

### <mark style="color:blue;">/dh h alwaysfaceplayer \<hologram> \<page> \<true|false></mark>

Set the value of always-face-player. If true, hologram line offsets will be relative to players location, meaning that the player will see the lines aligned the same from any angle.

* \<hologram> -  Name of the Hologram.
* \<page> -  Index of the hologram page.
