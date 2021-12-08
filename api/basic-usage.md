# ⚙ Basic Usage

The best way to use DecentHolograms API is the DHAPI class. This class was added in version 2.0.12 and is made, so that no matter what chages are made in the code or even the API, DHAPI class will stay the same changing just the implementation. Thanks to this, you can just implement a support for DecentHolograms once and will you have to change it no matter what version of DH is used. (After 2.0.12 of course.)

## Using DHAPI class

You can create or edit holograms very easily using the DHAPI class. I would actually recommend looking at the class yourself to see all the methods. You can find this class on [GitHub](https://github.com/DecentSoftware-eu/DecentHolograms/blob/main/src/main/java/eu/decentsoftware/holograms/api/DHAPI.java) with javadoc.

Anyway, here are some examples on how to use it:

### Creating a hologram

```java
Location location = null; // You will need a valid location..
List<String> lines = Arrays.asList("Line 1", "Line 2");

// Create an empty hologram
Hologram hologram = DHAPI.createHologram("name", location);

// Create a hologram with lines
Hologram hologram = DHAPI.createHologram("name", location, lines);

// Creating a hologram, that's going to be saved in a file and therefore loaded
Hologram hologram = DHAPI.createHologram("name", location, true);

// Or with lines
Hologram hologram = DHAPI.createHologram("name", location, true, lines);
```

{% hint style="success" %}
That's it! You don't even have to register the hologram or anything.
{% endhint %}

### Getting a hologram

```java
// You can simply get a hologram by name
Hologram hologram = DHAPI.getHologram("hologramName");
```

### Moving a hologram

```java
Location location = null; // You will need a valid location..
Hologram hologram = DHAPI.getHologram("hologramName");

// Move a hologram
DHAPI.moveHologram(hologram, location);

// Move a hologram by name
DHAPI.moveHologram("hologramName", location);
```

### Editting a hologram

{% hint style="info" %}
If you want to know more about line content, visit [this page](../get-started-1/format/).
{% endhint %}

```java
// Most of the methods below also work with just a name but we will use this
Hologram hologram = DHAPI.getHologram("hologramName");

int pageIndex = 0; // First page
// == Set hologram lines from list (this will affect the first page only) ==
List<String> lines = Arrays.asList("Line 1", "Line 2");
DHAPI.setHologramLines(hologram, lines);
// To set lines on a specific page, do this:
DHAPI.setHologramLines(hologram, pageIndex, lines);

// == Add a line ==
DHAPI.addHologramLine(hologram, "Line content");
// To a specific page
DHAPI.addHologramLine(hologram, pageIndex, "Line content");

int lineIndex = 0; // First line
// == Insert a line ==
DHAPI.insertHologramLine(hologram, lineIndex, "Line content");
// To a specific page
DHAPI.insertHologramLine(hologram, pageIndex, lineIndex, "Line content");

// == Set a line ==
DHAPI.setHologramLine(hologram, lineIndex, "New line content");
// On a page
DHAPI.setHologramLine(hologram, pageIndex, lineIndex, "New line content");

// == Remove a line ==
HologramLine line = DHAPI.removeHologramLine(hologram, lineIndex);
// From a page
HologramLine line = DHAPI.removeHologramLine(hologram, pageIndex, lineIndex);
```

### Pages

```java
// Most of the methods below also work with just a name but we will use this
Hologram hologram = DHAPI.getHologram("hologramName");
List<String> lines = Arrays.asList("Line 1", "Line 2");
int pageIndex = 0; // First page

// == Add a page == 
HologramPage page = DHAPI.addHologramPage(hologram);
// Or with lines
HologramPage page = DHAPI.addHologramPage(hologram, lines);

// == Insert a page ==
HologramPage page = DHAPI.insertHologramPage(hologram, pageIndex);
// Or with lines
HologramPage page = DHAPI.insertHologramPage(hologram, pageIndex, lines);

// == Remove a page ==
HologramPage page = DHAPI.removeHologramPage(hologram, pageIndex);
```

{% hint style="info" %}
There are much more methods in the DHAPI class that you can play with. If you want me to explain/add anything else, please contact us on [Discord](https://discord.decentsoftware.eu).
{% endhint %}
