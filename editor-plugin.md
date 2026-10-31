---
title: Editor plugin
parent: Reference
nav_order: 8
---
{% raw %}

# Editor plugin

The plugin `Plugins/AmberFramework` of your authoring project adds an **Amber Framework** menu to the main menu bar of Unreal Editor 5.7. It is written in Python and needs no compiling. The Python Editor Script plugin must be enabled in the project.

It is installed by `Tools/setup_authoring_project.py` from `Editor/AmberFramework` in the framework folder ([Authoring setup](authoring.md)).

## Menu

| Entry | What it does |
| --- | --- |
| New Mod... | Asks for id, name, version, author, category, tags, description, dependencies, links, a template and a preview picture. Creates `ModSource/<id>` with `mod.json` and `content/main.lua`, and the folder `/Game/Mods/<id>` for assets. |
| Mod Info... | Edits `mod.json` of a mod: name, version, author, category, tags, description, dependencies, [links](create-a-mod.md#links), preview picture. Fields this window does not show are kept. |
| Cook & Pack Mod | Saves changed assets, cooks `/Game/Mods/<id>` in the background, patches static meshes and packs the mod into `Build/Packages/<id>`. A message reports the result. |
| Open Mod Folder | Opens `ModSource/<id>` in Explorer. |
| Framework Documentation | Opens this site. |
| Settings... | The framework folder (with `Tools/` and `ModSource/`), the `python.exe` used for the tools and the documentation URL. |

The mod the menu works on is the one whose folder under `/Game/Mods` is open in the Content Browser, otherwise the last mod used. Without either the menu asks you to pick one.

## New Mod defaults

The form starts with Name "My Mod", Id "MyMod" and your last used author name. If you change the name and leave the id as "MyMod", the id is made from the name.

Templates write a starting `content/main.lua` with commented examples:

| Template | Section |
| --- | --- |
| Empty | `items`, `buildings`, `patches`, `loot` |
| New item | `items` |
| New weapon | `items` with a model |
| New building | `buildings` |
| Change game data | `patches` |
| Loot changes | `loot` |

The new mod loads without errors before you edit anything.

## Dependencies

One per line: a mod id, optionally with a minimum version as `SteelGear>=1.0.0`. Amber Framework is not listed. The mod manager adds it.

## Without the editor

`Cook & Pack` runs `python Tools/cook_project_mod.py <id>`, which can also be used from a console. It finds the static meshes of the mod by itself and gives each the PadSM2 patch.
{% endraw %}
