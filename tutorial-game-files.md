---
title: Explore the game files
parent: Tutorials
nav_order: 2
---
{% raw %}

# Explore the game files

Every mod refers to the game's rows, fields, models, materials, icons, sounds and Blueprint classes by name. This page shows where to find all of them in your own copy of the game.

There are two sources:

| Source | Gives you | Tool |
| --- | --- | --- |
| Game data export | Every data table with all rows and fields, item names in your language, creature drops | The mod manager, one button. See [Game data](game-data.md). |
| Game files | Models, textures, materials, icons, sounds, Blueprints, maps, and the tables in their original form | FModel, retoc |

Start with the export for anything in a table. Use the game files when you need an asset path or want to look at a model.

## 1. Mappings file

Grounded 2 is built with Unreal Engine 5. Its files do not store property names, so viewers need a mappings file (`.usmap`) made from the running game.

1. UE4SS comes with the mod manager, which adds it to the game on its first start ([First setup](play-setup.md)).
2. Start the game and wait for the main menu.
3. In the UE4SS window, open the **Dumpers** tab and press **Generate .usmap file**. UE4SS writes `Mappings.usmap` into `Grounded2\Augusta\Binaries\Win64\ue4ss\`.
4. Rename it with the game version, for example `Grounded2_0.6.0.3.usmap`, and keep it.

Make a new one after every game update.

### More dumps from the UE4SS window

The UE4SS window has a **Dumpers** tab with more than the mappings file:

1. In `ue4ss\UE4SS-settings.ini` set `GuiConsoleEnabled = 1` and `GuiConsoleVisible = 1`.
2. Start the game. The UE4SS window opens next to it.
3. Open **Dumpers**. Its buttons write, into the `ue4ss` folder:
   - the mappings file (`.usmap`)
   - C++ headers of all game classes, and headers in the format Unreal's header tool reads (UHT), for building a project with the game's classes
   - a dump of all loaded objects and their properties
   - Lua type files for UE4SS scripts

The C++ and UHT headers show every class, field and function of the game, also those no table lists.

## 2. Browse with FModel

[FModel](https://fmodel.app) shows the game's folders, 3D models, textures, sounds and tables without unpacking them.

1. Download FModel from [fmodel.app](https://fmodel.app) and start it.
2. **Directory Selector**: add the folder `...\steamapps\common\Grounded2`. UE version: the newest UE5 version in the list. The game files are not encrypted, so leave the AES key empty.
3. **Settings > General**: turn on **Local Mapping File** and select your `.usmap`.
4. Load `Augusta-Windows_0_P` in the Archives tab.

Now the folder tree on the left is the game's content.

- Double-click a model to open the 3D viewer, a texture to see it, a table to read it as JSON.
- Right-click a file and choose **Copy > Package Path** to get its path.
- Right-click and **Export** to save textures as PNG or models as glTF/PSK, for example to use a game model as a size reference in Blender.

## 3. From a file to a path in your mod

FModel shows files on disk, mods use Unreal object paths:

| In FModel | In a mod |
| --- | --- |
| `Augusta/Content/Blueprints/Items/Icons/ICO_Weevil_Nose.uasset` | `/Game/Blueprints/Items/Icons/ICO_Weevil_Nose.ICO_Weevil_Nose` |
| `Augusta/Content/Blueprints/Items/Table_AllItems.uasset` | `/Game/Blueprints/Items/Table_AllItems.Table_AllItems` |
| `Augusta/Content/Blueprints/Creatures/Weevil/Base/BP_Weevil.uasset` | class: `/Game/Blueprints/Creatures/Weevil/Base/BP_Weevil.BP_Weevil_C` |

The rule: `Augusta/Content/` becomes `/Game/`, drop `.uasset`, repeat the asset name after a dot. A Blueprint class gets `_C` at the end. Loot rules use only the class name, `BP_Weevil_C`.

## 4. Where things are

| Folder | Contents |
| --- | --- |
| `Blueprints/Items` | Item tables (`Table_AllItems`), recipes, icons (`Icons/ICO_*`), item Blueprints: `Equippable/` in the hand, `World/` on the ground |
| `Blueprints/Items/TechTreeTables` | Ranger terminal entries |
| `Blueprints/Attacks` | Attack tables (`AllAttacks`, `ItemAttacks`), damage types, projectiles |
| `Blueprints/Creatures` | Creature Blueprints (`BP_Weevil`, `BP_Ant_*`), their behaviour and loot |
| `Art/Items`, `_Augusta/Art/Items` | Item models, textures and materials, for example `_Augusta/Art/Items/Weapons/Gun_Paintball/Textures/MI_Weapon_Gun_Paintball_Equip` |
| `Art/Items/Buildings` | Building models and textures |
| `Art/Creatures`, `Art/Characters` | Creature and player models and animations |
| `Art/World` | Grass, plants, rocks, props of the world |
| `Art/Effects` | Particle effects, for example the fire hit used by the Fire Dagger |
| `Audio/Sfx`, `Audio/Music` | Sound cues and music |
| `UI` | Icons, HUD, fonts (`UI/Fonts/TitleFont`, `UI/Fonts/BaseFont`) |
| `Releases/Release_0_x_0` | Content added in each game update, with its own tables, for example `Release_0_3_0/.../Table_TechTree_PumpkinPatch` |
| `_Dev` | Developer test content. Avoid it. |

Content of later updates often sits in `Releases/` and not in the main folders. If a name is missing where you expect it, search the whole tree.

## 5. Search the full file list

FModel has a search (Ctrl+Shift+F). For a text list of every file, use [retoc](https://github.com/trumank/retoc):

```powershell
retoc list --path "D:\SteamLibrary\steamapps\common\Grounded2\Augusta\Content\Paks\Augusta-Windows_0_P.utoc" > files.txt
```

The list has about 120,000 lines. Search it in any editor: `SwordAntRed` finds `BP_Equippable_SwordAntRed`, `BP_World_SwordAntRed` and the item's other files.

## 6. Unpack everything

To have all files on disk, for example to open them in [UAssetGUI](https://github.com/atenfyr/UAssetGUI), convert the whole game to the classic format:

```powershell
retoc to-legacy "D:\SteamLibrary\steamapps\common\Grounded2\Augusta\Content\Paks" D:\G2Unpacked --version UE5_7
```

The game's files take 18.5 GB packed. Plan for at least twice that on disk and some time. Use `--filter` to convert only files whose name matches, for example `--filter Table_` for the tables.

Unpacked files are for reading. A mod never ships changed copies of them. It changes fields with [patches](manifest.md#patches) and adds its own assets.

## What to use where

| You need | Look in |
| --- | --- |
| Row name of an item, recipe, building | Export: `Table_AllItems.json`, `Table_CraftingRecipes.json`, `Table_AllBuildings.json` |
| Field names and current values | Export, or `cfinspect` in the game |
| Template for a new item | Export: a row that behaves like your item |
| Material for your model | FModel: `MI_*` next to a similar game item |
| Icon, sound, effect of a game item | FModel, the item's folder or the row fields in the export |
| Creature class for loot rules | Export: `loot.json`, or FModel: `Blueprints/Creatures` |
| Size and position of a game model | FModel 3D viewer, or export the model to Blender |

Next: [Add an item with a recipe](tutorial-item.md).
{% endraw %}
