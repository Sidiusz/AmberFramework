---
title: Home
nav_order: 1
---
{% raw %}

# Amber Framework

Amber Framework lets many mods change Grounded 2 at once. Mods add new rows to the game's data tables and change single values instead of replacing game files. Two mods can edit the same item as long as they change different values, and a mod keeps working after a game update unless the values it uses were removed. See [What Amber does](how-it-works.md).

| Part | What it does |
| --- | --- |
| Grounded 2 Mod Manager | Installs mods, shows problems such as missing dependencies, starts the game with the mods that are on and cleans up when the game closes. |
| Framework | A UE4SS mod inside the game that applies the mods' data, models, loot and scripts. |
| Editor plugin | An Amber Framework menu in Unreal Editor 5.7 for creating and packing mods. |

## Where to start

I want to play with mods
: Read [Playing with mods](players.md).

I want to make my first mod
: Follow [Make your first mod](tutorial-first-mod.md). In about ten minutes you change a sword's damage and go through the whole process: look up names, write the change, pack, install and test in the game.

I want to add something new
: [Explore the game files](tutorial-game-files.md), [Add an item with a recipe](tutorial-item.md), [Add a weapon with your own model](tutorial-model.md), [Make a building with a script](tutorial-building.md), [Changing other game data](tutorial-first-mod.md#6-changing-other-game-data).

I need the details of one feature
: See the [Reference](reference.md).

Something does not work
: See [Troubleshooting](troubleshooting.md) and the [FAQ](faq.md).

## Example mods

The framework comes with example mods. Each one shows a feature and is a good starting point.

| Mod | Shows |
| --- | --- |
| Steel Gear | A new resource and a helmet with recipes, a Ranger terminal entry other mods add to, an Oven recipe, an extra loot drop, a daily bounty |
| Arsenal Weapons | The AK-74, a ranged weapon with its own model, LODs, fire projectiles and settings, and the Fire Dagger with its own model, glowing blade and a fire combo |
| Game Tweaks | Changes to existing game data only: the Crimson Saber's damage, recipe and look, loot, creature health |
| Slot Machine | A building with a poseable model, a gameplay script, prizes and text on the model |
| Base Buildings | A storage chest with 60 slots, a glowing decoration, an animated windmill and pictures for sign frames, sold at the Ranger terminal |
| Energy Soda | A drink with its own status effect, texts in 11 languages |
| Giant Aphid | A new creature with its own model on the game's aphid skeleton |
| Snackbar Map | Map changes: removed pieces and foliage, a level of the mod, a moved pickup, items on the ground |
| Radio Dialog | A terminal by the Snackbar with its own speaker, screen pictures and a conversation |
| Mods Menu | The in-game Mods screen, as a separate mod |

## Requirements

- Grounded 2 on Steam. The mod manager adds the UE4SS build the framework needs on its first start ([First setup](play-setup.md)).
- For mods with models, textures or Blueprints: Unreal Engine 5.7 and an authoring project ([Authoring setup](authoring.md)). Data, text and scripts need no Unreal Engine.
{% endraw %}
