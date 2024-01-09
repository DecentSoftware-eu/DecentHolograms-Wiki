---
title: Get Started
description: How to get started with DecentHolograms' API

icon: material/cog
---

On this page, you can find how to add DecentHolograms into your plugins and use its API. Keep in mind, that you also need to have the DecentHolograms plugin on your server, in order for the API to work.

Latest version of the plugin can be found in Releases on the GitHub page.

## Add the API

Add the following to your build file to add the DecentHolograms API to your project.

/// tab | :simple-gradle: Gradle
```{ .groovy title="build.gradle" data-md-component="api-version" }
repositories {
    maven { 
      id = "jitpack"
      url = "https://jitpack.io/"
    }
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

/// question | Receiving errors about NBT-API not being found?
Try adding the CodeMC repository to your build file to fix this:

//// tab | :simple-gradle: Gradle
```groovy title="build.gradle"
repositories {
  // Other repositories, including jitpack
  maven {
    id = "codemc"
    url = "https://repo.codemc.io/repository/maven-public/"
  }
}
```
////

//// tab | :simple-apachemaven: Maven
```xml
<repositories>
  <!-- Other repositories, including jitpack -->
  <repository>
    <id>codemc</id>
    <url>https://repo.codemc.io/repositories/maven-public/</url>
  </repository>
</repositories>
```
////
///

## Add plugin as a (soft) dependency

DecentHolograms needs to be on your server for your plugin to be able to use the API.  
To make sure that DecentHolograms is loaded before your plugin, add it as a (soft) dependency to your `plugin.yml` or `paper-plugin.yml` file:

/// tab | :simple-spigotmc: / :fontawesome-solid-paper-plane: plugin.yml
//// tab | Soft dependency
```yaml
name: 'MyPlugin'
author: 'Me'
version: '1.0.0'

main: 'com.example.plugin.MyPlugin'

softdepend:
  - DecentHolograms
```
////

//// tab | Dependency
```yaml
name: 'MyPlugin'
author: 'Me'
version: '1.0.0'

main: 'com.example.plugin.MyPlugin'

depend:
  - DecentHolograms
```
////
///

/// tab | :fontawesome-solid-paper-plane: paper-plugin.yml
//// tab | Soft dependency
```yaml
name: 'MyPlugin'
author: 'Me'
version: '1.0.0'

main: 'com.example.plugin.MyPlugin'

dependencies:
  server:
    DecentHolograms:
      load: BEFORE
      required: false # This is the default when not present
```
////

//// tab | Dependency
```yaml
name: 'MyPlugin'
author: 'Me'
version: '1.0.0'

main: 'com.example.plugin.MyPlugin'

dependencies:
  server:
    DecentHolograms:
      load: BEFORE
      required: true
```
////
///
