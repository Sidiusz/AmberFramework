---
title: Playing
parent: Troubleshooting
nav_order: 1
---
{% raw %}
# Playing

## Mods do not load in the game

Start the game with **Play Modded** in the mod manager. Started from Steam, the game runs without mods. With mods active, the version line in the main menu ends with "Modded: Amber Framework, N mods".

## Changes in the Mods screen do nothing

Turning mods on or off applies after restarting the game, and so do settings marked "after restart". The load order can only be changed in the mod manager. See [Mods screen in the game](play-in-game.md).

## Buildings of a removed mod are gone

Without the mod, the game drops its buildings the next time it saves. Mods with `"preserve": true` bring them back when you install the mod again. See [Removing mods](play-removing.md).

## Multiplayer problems

All players need the same mods in the same versions. After joining, a "MODS DIFFER" window shows what each side is missing. "MODS NOT CONFIRMED" means the host didn't answer: the host plays without Amber Framework or with a version older than 0.2.0. See [Multiplayer](multiplayer.md).
{% endraw %}
