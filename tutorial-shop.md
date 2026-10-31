---
title: Sell recipes at the Ranger terminal
parent: Tutorials
nav_order: 7
---
{% raw %}

# Sell recipes at the Ranger terminal

<p class="download-stub">Download the finished tutorial project: SteelGear.zip</p>

The Ranger terminal sells recipes for Raw Science. A mod can add its own entry there, or add its recipes to an entry another mod made. This page uses the example mods `SteelGear`, `ArsenalWeapons` and `SlotMachine`.

Read [Add an item with a recipe](tutorial-item.md) first.

## A new entry

```lua
shop = {
    {name = "Arsenal", cost = 500, title = "arsenal.title", description = "arsenal.description", recipes = {"Ingot", "Helmet"}},
},
```

| Key | Meaning |
| --- | --- |
| `name` | Short name of the entry. The row becomes `<namespace>_Arsenal`. |
| `cost` | Price in Raw Science. |
| `title`, `description` | Keys of the mod's language files ([Add text and translations](tutorial-localization.md)). Without them the entry shows the template's text. |
| `recipes` | Short names of this mod's crafting recipes. |
| `buildings` | Short names of this mod's building recipes (rows in `BuildingRecipeTable`). |
| `unlocks` | Any other rows: `{{table = "CraftingRecipeTable", row = "BowWorkbench"}}`. |
| `category` | Terminal tab as a tag, for example `"Recipe.Tech.Upgrades"`. Default: the template's tab. |
| `terminal` | Object path of another terminal table. Default: the starter terminal. |
| `template` | `{table = ..., row = ...}` of the entry to copy. Default: a smithing entry that fits any recipe. |

Recipes sold here should not be `unlocked = true`, because buying the entry unlocks them.

The framework turns this into a copied terminal row with your price and text, plus an `append` of the unlocks. You can still write that yourself with `imports` and `patches` ([Manifest reference](manifest.md#imports)).

## Adding to another mod's entry

```lua
shop = {
    {entry = "SteelGear_Arsenal", recipes = {"Rifle"}},
},
```

`entry` is the full row name of an existing entry. Several mods can add to the same entry, and the additions add up. List the mod that makes the entry as a dependency, so it loads first:

```json
"dependencies": [{ "id": "SteelGear", "minVersion": "1.0.0" }]
```

## A building at the terminal

```lua
shop = {
    {name = "LuckyMachines", cost = 300, title = "luckyMachines.title", description = "luckyMachines.description", buildings = {"SlotMachine"}},
},
```

After buying it, the building shows up in the build menu ([Make a building with a script](tutorial-building.md)).

## Check

[Build and install](build.md) the mod, start the game, open the Ranger terminal and find the entry. Buy it. The recipes appear in the crafting or build menu. `cfinspect /Game/Blueprints/Items/TechTreeTables/Table_TechTree_InitialData.Table_TechTree_InitialData SteelGear_Arsenal` prints the entry with its values.
{% endraw %}
