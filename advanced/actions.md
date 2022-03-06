# 🖱 Actions

### Format

General format of actions is:

{% hint style="success" %}
\<actionType>\[:args]
{% endhint %}

### Click Types

* LEFT
* RIGHT
* SHIFT\_LEFT
* SHIFT\_RIGHT

## Action Types

> <> - Required
>
> \[] - Optional

#### MESSAGE:\<message>

Sends a message to the player who clicked.

#### COMMAND:\<command>

Executes a command as the player who clicked.

#### CONSOLE:\<command>

Executes a command as console.

#### CONNECT:\<server>

Send the player who clicked to another server. (Bungee only)

#### TELEPORT:\[world]:\<x>:\<y>:\<z>

Teleport the player who clicked to the specified location.

#### SOUND:\<sound>

Plays a sound for the player who clicked.

There is a list of all sounds you can use:&#x20;

* [For 1.8](https://helpch.at/docs/1.8.8/index.html?org/bukkit/Sound.html)
* [For 1.9+](https://helpch.at/docs/1.9/index.html?org/bukkit/Sound.html)
* [For 1.13+](https://helpch.at/docs/1.13/index.html?org/bukkit/Sound.html)

You can see sounds for any specific version by editting this link (..docs/VERSION/..):&#x20;

[https://helpch.at/docs/1.13/index.html?org/bukkit/Sound.html](https://helpch.at/docs/1.13/index.html?org/bukkit/Sound.html)

#### PERMISSION:\<permission>

Checks whether the player who clicked has the specified permission and if not, all the actions after this one will not be executed.

#### NEXT\_PAGE:\[hologram]

Switches to the next page of the specified hologram for the player who clicked.&#x20;

#### PREV\_PAGE:\[hologram]

Switches to the previous page of the specified hologram for the player who clicked.

#### PAGE:\[hologram]:\<page>

Switches to a specific page of the specified hologram for the player who clicked.

