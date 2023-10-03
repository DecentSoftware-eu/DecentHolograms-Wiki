---
title: Get Started
icon: material/cog
---

On this page, you can find how to add DecentHolograms into your plugins and use its API. Keep in mind, that you aslo need to have the DecentHolograms plugin on your server, in order for the API to work.

Latest version of the plugin can be found in Releases on the GitHub page.

=== ":simple-gradle: Gradle"
    ```groovy
    repositories {
        maven { url = "https://jitpack.io" }
    }
    
    depencencies {
        compileOnly 'com.github.decentsoftware-eu:decentholograms:{version}'
    }
    ```
=== ":simple-maven: Maven"
    ```xml
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