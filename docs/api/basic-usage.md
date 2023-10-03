---
title: Basic Usage
icon: material/cog
---

The best way to use DecentHolograms API is the DHAPI class. This class was added in version 2.0.12 and is made, so that no matter what changes are made in the code or event the API, DHAPI class will stay the same changing just the implementation. Thanks to this, you can just implement a support for DecentHolograms once and will not have to change it no matter what version of DH is used. (After 2.0.12 of course)

## Using DHAPI class

You can create or edit holograms very easily using the DHAPI class. I would actually recommend looking at the class yourself to see all the method. You can find this class on [GitHub][github] with Javadoc.

Anyway, here are some examples on how to use it:

### Creating a hologram

```java
Location location = null; // Make sure this is a valid location
List<String> lines = Arrays.asList("Line1", "Line 2");

// Crate an empty hologram
Hologram hologram = DHAPI.createHologram("name", location);

// Create a hologram with lines
Hologram hologram = DHAPI.createHologram("name", location, lines);

// Create a hologram that will be saved to a file and is therefore persistent between restarts
Hologram hologram = DHAPI.createHologram("name", location, true);

// ...and the same with lines
Hologram hologram = DHAPI.createHologram("name", location, true, lines);
```

That's it! You don't even have to register the hologram or anything.

### Getting a hologram

```java
// Get a hologram by its name
Hologram hologram = DHAPI.getHologram("name");
```

### Moving a hologram
```java
Location location = null; // Make sure this is a valid location
Hologram hologram = DHAPI.getHologram("name");

// Move the hologram
DHAPI.moveHologram(hologram, location);

// Move a hologram by name
DHAPI.moveHologram("name", location);
```

### Editing a hologram

!!! info
    Hologram lines use the exact same content as YAML files have. To learn more about available content options, visit [this page](../general/format-and-colors/index.md).

```java
// Most methods below also work with a hologram name, but we will be using this
Hologram hologram = DHAPI.getHologram("name");

// Pages are zero-indexed, so this is the first page
int page = 0;

// Override existing lines with new list
List<String> lines = Arrays.asList("Line1", "Line 2");
DHAPI.setHologramLines(hologram, lines);
// To set lines of a specific page, do this:
DHAPI.setHologramLines(hologram, page, lines);

// Add a new line
DHAPI.addHologramLine(hologram, "New Line");
// For a specific page
DHAPI.addHologramLine(hologram, page, "New Line");

// First line of a page. Also zero-indexed like pages
int line = 0;

// Insert a line
DHAPI.insertHologramLine(hologram, line, "New Line");
// On a specific page
DHAPI.insertHologramLine(hologram, page, line, "New Line");

// Remove a line. Returned HologramLine is the removed one.
HologramLine line = DHAPI.removeHologramLine(hologram, line);
// On a specific page
HologramLine line = DHAPI.removeHologramLine(hologram, page, line);
```

### Pages

```java
Hologram hologram = DHAPI.getHologram("name");
List<String> lines = Arrays.asList("Line1", "Line 2");
int page = 0;

// Add a page
HologramPage page = DHAPI.addHologramPage(hologram);
// Or with lines
HologramPage page = DHAPI.addHologramPage(hologram, lines);

// Insert a page
HologramPage page = DHAPI.insertHologramPage(hologram, page);
// Or with lines
HologramPage page = DHAPI.insertHologramPage(hologram, page, lines);

// Remove a page. Returned HologramPage is the removed one
HologramPage page = DHAPI.removeHologramPage(hologram, page);
```

## More

There are a lot more methods in the DHAPI. Way too many to list here.  
If you would like to see some more examples here, contact us on [Discord][discord]

[github]: https://github.com/DecentSoftware-eu/DecentHolograms/blob/main/src/main/java/eu/decentsoftware/holograms/api/DHAPI.java
[discord]: https://discord.decentsoftware.eu/