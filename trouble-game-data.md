---
title: Game data
parent: Troubleshooting
nav_order: 3
---
{% raw %}
# Game data

## cfstatus says a row or field was not found

The name in the manifest does not exist in the installed game. Names are case-sensitive in the manifest even where the game is not. Look the row up again in the [game data export](game-data.md). After a game update a row can be renamed or removed. Export again after each update, since the export reads the installed version.

## cfstatus says waiting

A row the mod names does not exist yet. The message names the table and the row. Usually the row belongs to another mod that is missing, turned off or later in the load order. Put that mod first or add it as a dependency.

## A weapon sometimes fires the template's projectile

An attack row has three kinds of shots: normal, charged and perfectly charged. Each has its own `ProjectileClass`, `ChargedProjectileClass` and `PerfectChargedProjectileClass`, and its own damage type. A short `ChargeTime` makes most shots charged ones. Set all three when the attack should always fire the new projectile, as the Arsenal Weapons rifle does.

{% endraw %}
