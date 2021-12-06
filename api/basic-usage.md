# ⚙ Basic Usage

## Using DHAPI class

You can create or edit holograms very easily using the DHAPI class. Here are some examples on how to use it. (You can find this class on [GitHub](https://github.com/DecentSoftware-eu/DecentHolograms/blob/main/src/main/java/eu/decentsoftware/holograms/api/DHAPI.java) with javadoc.)

```java
// Create a hologram with lines
Location location = null; // You will need a valid location..
List<String> lines1 = Arrays.asList("Line 1", "Line 2");
Hologram hologram = DHAPI.createHologram("name", location, lines1);

/* ===================================== */

// Update hologram lines
// The hologram must exist in the first place
Hologram hologram = DHAPI.getHologram("name");
List<String> lines2 = Arrays.asList("Line 1", "Line 2 (Middle)", "Line 3");
DHAPI.setHologramLines(hologram, lines2);

/* ===================================== */

// Update hologram line
// The hologram and the line we are editting must exist in the first place
Hologram hologram = DHAPI.getHologram("name");
int lineIndex = 0; // First line
DHAPI.setHologramLine(hologram, lineIndex, "New content");
```

{% hint style="info" %}
There are much more methods in the DHAPI class that you can play with. If you want me to explain/add anything else, please contact us on [Discord](https://discord.decentsoftware.eu).
{% endhint %}
