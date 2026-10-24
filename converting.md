---
title: Converting old mods
parent: Reference
nav_order: 7
---
{% raw %}

# Converting old mods

Most existing Grounded 2 mods replace whole data tables. Two such mods that touch the same table cannot be used together, and they break when the game updates the table.

The converter turns the table changes of such a mod into field patches:

1. It exports the game data with the old mod mounted.
2. It compares that export with a normal one.
3. It writes every changed field as a patch, with the value in Unreal text format.

```powershell
dotnet Tests/Launcher.Core.Tests/bin/Debug/net10.0/Launcher.Core.Tests.dll --convert-legacy <game folder> <old mod folder> <workspace> <output folder>
```

The output folder gets `mod.json`, `content/main.lua` and `CONVERSION.md`. The report lists what was not converted:

- New rows. Framework rows get the mod's namespace as a prefix. Rows that other assets look up by their exact name need `exactName = true` ([Common rules](manifest.md#common-rules-for-new-rows)).
- Rows the old mod removed. The framework does not delete game rows.
- Tables that only the old mod has. These stay in the mod's pak.

Models, textures and sounds of the old mod are still needed from its pak, without its table files.

## From UAssetGUI JSON files

When the author has the edited assets as UAssetGUI JSON exports, no old pak is needed and the mod does not have to load in the current game:

```powershell
python -I Tools/convert_table_json.py <folder with JSON files> <output mod folder>
python -I Tools/verify_conversion.py <folder with JSON files> <mod id>
python -I Tools/convert_class_json.py <folder with JSON files> <output mod folder>
```

1. `convert_table_json.py` compares every data table JSON with the [game data export](game-data.md) and writes `content/<table>.lua`: changed fields become patches, new rows keep their exact names (`exactName`).
2. `verify_conversion.py` starts the game hidden with the packed mod and reads every converted field back. It prints how many fields match and the ones that do not.
3. `convert_class_json.py` reads the class defaults of Blueprint JSON files, compares them with the game in a hidden run and writes the differences to `content/classes.lua` as [class edits](manifest.md#classes). It is not in the modder kit, because the hidden run needs the framework's own test setup.

A renamed copy of a game table (same row type, mostly the same rows) is converted as changes to that game table. `CONVERSION.txt` names it. Gameplay tags the game does not have are written as they are (see [Values](manifest.md#values)).

`CONVERSION.txt` in the output folder lists what was not converted: tables the game does not have, fields the JSON tool could not read, rows that appear twice with different values, and Blueprint graphs. Those need the author.

## After converting

Converting is done once. The output folder is the new source of the mod: from then on the author edits `content/main.lua` and `mod.json` directly and packs the mod like any other ([Make your first mod](tutorial-first-mod.md)). The converter is not needed again.

A game update does not require converting again either. Patches name rows and fields, and the framework applies them to whatever tables the updated game has. A mod needs a change only when:

- a row or field it uses was renamed or removed. `cfstatus` names it, and the [game data export](game-data.md) of the new version shows the new name.
- its own models, textures or sounds have to be cooked again because the game moved to a newer Unreal version.

## Limits

Only tables the game has loaded during the export are compared.

The old mod has to load in the installed game version, because the converter reads its tables from the running game. A mod built for an older version that crashes the current game cannot be converted this way. Ask its author for the edited tables (JSON or CSV export) or the source project instead. Turn the table edits from those into patches by hand.

Mods that replace Blueprints or maps cannot be expressed as patches. Their logic has to be rebuilt as [scripts](scripting.md) or in the author's own Blueprint classes.
{% endraw %}
