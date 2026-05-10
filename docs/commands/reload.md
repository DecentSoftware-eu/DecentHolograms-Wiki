---
title: '/dh reload'
description: 'Reloads the plugin and its holograms'
---

The `reload` command performs a reload of DecentHolograms.  
This will refresh the general plugin settings, custom animations and all saved Holograms.

/// info | Note for developers
This command will trigger a [`DecentHologramsReloadEvent`](../api/events/decenthologramsreloadevent.md)
///

{{ permissions("reload") }}