# ⚙ Get Started

On this page, you can find how to add DecentHolograms into your plugins and use its API. Keep in mind, that you also need to have the DecentHolograms plugin on your server, in order for the API to work.

Latest version of the plugin can be found in Releases on the GitHub page.

**Gradle:**

```groovy
repositories {
    maven { url 'https://jitpack.io' }
}

dependencies {
    compileOnly 'com.github.decentsoftware-eu:decentholograms:TAG'
}
```

{% hint style="warning" %}
Replace TAG with the current version of DecentHolograms. (Latest release on [GitHub](https://github.com/DecentSoftware-eu/DecentHolograms/releases))
{% endhint %}

**Maven:**

```xml
<repositories>
    <repository>
        <id>jitpack.io</id>
        <url>https://jitpack.io</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>com.github.decentsoftware-eu</groupId>
        <artifactId>decentholograms</artifactId>
        <version>TAG</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

{% hint style="warning" %}
Replace TAG with the current version of DecentHolograms. (Latest release on [GitHub](https://github.com/DecentSoftware-eu/DecentHolograms/releases))
{% endhint %}
