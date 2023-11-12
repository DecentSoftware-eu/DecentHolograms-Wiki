---
title: Get Started
description: How to get started with DecentHolograms' API

icon: material/cog
---

On this page, you can find how to add DecentHolograms into your plugins and use its API. Keep in mind, that you aslo need to have the DecentHolograms plugin on your server, in order for the API to work.

Latest version of the plugin can be found in Releases on the GitHub page.

/// tab | :simple-gradle: Gradle
```{ .groovy title="build.gradle" data-md-component="api-version" }
repositories {
    maven { url = "https://jitpack.io" }
}

depencencies {
    compileOnly 'com.github.decentsoftware-eu:decentholograms:{version}'
}
```
///

/// tab | :simple-apachemaven: Maven
```{ .xml title="pom.xml" data-md-component="api-version" }
<repositories>
  <repository>
    <id>jitpack</id>
    <url>https://jitpack.io/</url>
  </repository>
</repositories>

<dependencies>
  <dependency>
    <groupId>com.github.decentsoftware-eu</groupId>
    <artifactId>decentholograms</artifactId>
    <version>{version}</version>
    <scope>provided</scope>
  </dependency>
</dependencies>
```
///