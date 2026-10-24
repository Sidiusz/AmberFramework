---
title: Publish a mod
parent: Tutorials
nav_order: 99
---
{% raw %}

# Publish a mod

This page covers what to check before sharing a mod, what to upload and how updates reach players.

## Before you share

- `mod.json` has `id`, `name`, `version`, `author` and a short factual `description` ([Mod folder and mod.json](create-a-mod.md)).
- `dependencies` names every mod yours needs, with `minVersion`. Always list `AmberFramework`.
- `preview.png` is the cover (960 x 540 works well) and `icon.png` the square icon in the mod list (256 x 256).
- `links` points at your mod page and source, if you have them ([Links](create-a-mod.md#links)).
- Install the packed mod in the mod manager with only the framework and your dependencies. Check that it shows no sign, that `cfstatus` says `applied` and that the content works in a copy of a save.
- Install it next to the example mods. Problems show up as signs on the mods before you play, and the UE4SS log lists which mod overrides which.
- Models, textures and sounds you did not make: keep their authors and the links to the model pages in a `CREDITS.txt` next to the source files and on your mod page.

## What to upload

```powershell
python Tools/pack_mod.py ModSource/MyMod -o Build/Packages/MyMod
```

Zip the folder `Build/Packages/MyMod`. Players drag the zip onto the mod manager. An archive with several mod folders installs each of them.

Do not upload `settings.json`, because it holds your own values. The mod manager creates it from `settings.schema.json` on the player's PC.

## Versions and updates

- Raise `version` with every release: `1.0.0`, `1.0.1`, `1.1.0`. The mod manager compares the parts as numbers.
- If `links` has a Nexus Mods page or a GitHub repository, players are told about new versions. The mod manager compares your `version` with the version on the Nexus Mods page or the tag of the latest GitHub release (`v1.1.0` and `1.1.0` both work), so keep them in sync with `mod.json`.
- Installing a newer zip replaces the old version and keeps the player's settings, as long as the new schema still accepts them.
- Keep `id` and row names the same between versions. Items and buildings in saves are stored by row name. A renamed row is a different item, and the old one disappears from saves.
- If a setting changes meaning, give it a new `key`.

## Saves and removal

- Items of a removed mod that are in an inventory stay in the save. Equipped mod items are lost when the game saves without the mod.
- Buildings of a removed mod are lost on the next save, unless `mod.json` has `"preserve": true` ([Removing mods](play-removing.md)). Set it for mods that add buildings.

## After a game update

Patches name rows and fields, so most mods keep working. After an update:

1. Export the game data again in the mod manager.
2. Start the game with your mod and run `cfstatus`. `not ready` or `not found` names the row or field that changed.
3. Look up the new name in the export, fix the manifest, raise `version`, publish.
4. If the update moved the game to a newer Unreal version, cook the assets again.

See also [FAQ](faq.md).
{% endraw %}
