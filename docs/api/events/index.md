---
title: Events
description: Custom Events offered by DecentHolograms

icon: material/text-long
---

DecentHolograms provides a collection of events that a plugin can listen to.  
These events are primarely focused around Holograms.

## Events

<div class="grid cards" markdown>

-   ### [DecentHologramsEvent](decenthologramsevent.md)
    
    ----
    
    The basic event that all others are extending from.

-   ### [DecentHologramsReloadEvent](decenthologramsreloadevent.md)
    
    ----

    Called whenever the [`/dh reload`](../../general/commands/general.md#dh-reload) is executed.

-   ### [HologramClickEvent](hologramclickevent.md)
    
    ----

    Called whenever a player interacts with (clicks) a Hologram.

-   ### [HologramDisableEvent](hologramdisableevent.md)
    
    ----

    Called whenever a Hologram is disabled via its `disable(DisableCause)` method.

-   ### [HologramEnableEvent](hologramenableevent.md)
    
    ----

    Called whenever a Hologram is enabled via its `enable()` method.

-   ### [HologramRegisterEvent](hologramregisterevent.md)
    
    ----

    Called whenever a Hologram gets registered via `HologramManager#register(Hologram)`.

-   ### [HologramUnregisterEvent](hologramunregisterevent.md)
    
    ----

    Called whenever a Hologram gets unregistered via `HologramManager#unregister(Hologram)`.

</div>