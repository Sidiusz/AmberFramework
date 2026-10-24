---
title: What Amber does
nav_order: 2
---
{% raw %}

# What Amber does

Amber is a mod loader and adds no game features by itself. It handles the work every mod would otherwise repeat, so mods are quicker to make, work together and survive game updates.

## What Amber does for you

| Area | What Amber does | Where to read |
| --- | --- | --- |
| Installing and order | Installs mods, checks dependencies and versions, keeps the load order, starts the game with the mods that are on and cleans up afterwards. | [Playing with mods](players.md) |
| Game data | Adds rows to the game's tables and changes single fields, copies rows from templates, keeps the combined tables (`AllAttacks`, `Table_AllItems`) in step, writes gameplay tags. Two mods can change the same item. | [Manifest reference](manifest.md) |
| Text and languages | Builds the game's text tables from plain language files and registers them. No Unreal Engine needed. | [Add text and translations](tutorial-localization.md) |
| Your own assets | Mounts the mod's cooked models, textures, sounds and Blueprints. Cooks them without opening the editor and applies the fixes this game needs (PadSM2, the exact bone pose of game skeletons). | [Models](models.md) |
| Game systems | Puts new things where the game looks for them: crafting menus, stations, the build menu, the Ranger terminal, chests, sign pictures, bounties, creatures, conversations and world variables. | [Manifest reference](manifest.md) |
| Saves | Records the buildings of mods that ask for it per world and brings them back when a removed mod returns. Places a mod's items once per saved world. | [Removing mods](play-removing.md) |
| Settings | Stores each mod's settings. Live settings reach the mod's scripts right away. The in-game Mods screen is a separate mod, Mods Menu. | [Mod folder and mod.json](create-a-mod.md) |
| Scripts | Runs each mod's Lua scripts with the full UE4SS API, plus helpers for buildings, keys, settings, timers, conversations and world variables. A failing script does not stop other mods. | [Scripting](scripting.md) |
| Between mods | If two mods set the same value, the lower one in the load order wins, and the mod manager shows which. | [Rules between mods](manifest.md#rules-between-mods) |
| Game updates | Mods refer to rows and values by name, so most keep working. `cfstatus` shows what changed. | [Publish a mod](publishing.md) |
| Finding things | Exports the game's tables, loot lists and assets. Console commands show positions, nearby objects and the state of every mod. | [Game data](game-data.md) |

## What you write

- The mod's data: new rows, changed fields, recipes, terminal entries, in a Lua manifest.
- The mod's text: one language file per language.
- The mod's art: models, textures, sounds, made in your own tools and cooked with the pipeline.
- The mod's behaviour: Lua scripts, with the whole UE4SS API.

The [example mods](index.md#example-mods) show each of these, and the [tutorials](tutorials.md) build them step by step.
{% endraw %}
