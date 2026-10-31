---
title: Game data
parent: Troubleshooting
nav_order: 3
---
{% raw %}
# Game data

## cfstatus says a field was not found

A field name in the manifest does not exist in the row's type. Look the field up in the [game data export](game-data.md). Export again after each game update, since the export reads the installed version.

## cfstatus says not ready

`not ready: <table>.<row>`: a row the mod names does not exist. The message names the table and the row. Usually the row belongs to another mod that is missing, turned off or later in the load order. Put that mod first or add it as a dependency. After a game update a game row can also be renamed or removed: look it up in a new export. In the main menu the mods after this one in the load order wait too. If the row is still missing when a world starts loading, `cfstatus` says `turned off, <table>.<row> is still missing when the world loads`. Only that mod is off, and the mods after it apply.

## A weapon sometimes fires the template's projectile

An attack row has three kinds of shots: normal, charged and perfectly charged. Each has its own `ProjectileClass`, `ChargedProjectileClass` and `PerfectChargedProjectileClass`, and its own damage type. A short `ChargeTime` makes most shots charged ones. Set all three when the attack should always fire the new projectile, as the Arsenal Weapons rifle does.

{% endraw %}
