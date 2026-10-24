---
title: Game data
parent: Reference
nav_order: 5
---
{% raw %}

# Game data

Mods refer to rows and fields by name. The mod manager can export the installed game's data so you can look them up. Because the export reads the game you have, it is always current, including after game updates.

## Export

Press **Export game data** in the mod manager. The game starts hidden with only the framework, writes every loaded data table and closes. It takes about a minute. Saves and game settings are not touched. The UE4SS console is hidden for this run and restored after it.

Output: `%LOCALAPPDATA%\G2Launcher\GameData\<game version>\`

- `index.json`: every table with its object path, row struct, row count and file.
- `tables/<Table>.json`: all rows with all fields as Unreal text.

```json
"WeevilNose": {
  "@name": "Weevil Nose",
  "LocalizedDisplayName": "(StringTableID=2,StringID=345)",
  "Icon": "/Game/Blueprints/Items/Icons/ICO_Weevil_Nose.ICO_Weevil_Nose",
  "ItemType": "General",
  "DuplicateBaseCost": "200"
}
```

`@name` is the name shown in the game, in the game's current language.

A typical lookup: find the item in `Table_AllItems.json` by `@name`, use its row name (`WeevilNose`) in your manifest, and use the field names you see in [patches](manifest.md#patches). Values in the files are in the format that `{unreal = "..."}` accepts.

Models, textures and other assets are not in the export. See [Explore the game files](tutorial-game-files.md).

## Loot

Drops are not in any table. Each creature, plant and container Blueprint has its own list. The export reads every one of them from the game's files and writes `loot.json`:

```json
"BP_Weevil_C": [{"item": "WeevilNose", "count": 1, "chance": 0.3, "multiplier": 1, "type": 0}, ...]
```

These are the original values, before any loot rules. While you play with mods, classes the export missed are added to the same file.

## In the game

The UE4SS console command `cfinspect <table> <row>` prints the fields of one row, for example `cfinspect AllItemsTable SpearTier3`.
{% endraw %}
