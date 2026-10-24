---
title: Add an item with a recipe
parent: Tutorials
nav_order: 3
---
{% raw %}

# Add an item with a recipe

<p class="download-stub">Download the finished tutorial project: SteelGear.zip</p>

This tutorial adds a crafting material, the Steel Ingot, with its own name, icon and recipe, and sells the recipe at the Ranger terminal. The finished mod is `ModSource/SteelGear`.

Read [Make your first mod](tutorial-first-mod.md) first. Unreal Engine 5.7 is needed only to cook the icon. See [Authoring setup](authoring.md).

## 1. Pick a template

A new item is a copy of an existing row. Pick an item that behaves like yours: a material copies a material, a helmet copies a helmet. The copy keeps every field you do not change, so the item works in the inventory, the crafting menu and saves from the start.

In the [game data export](game-data.md), open `tables/Table_AllItems.json` and search by `@name`. Mighty Glob is the row `IngotQuartzite`. That is the template.

## 2. The item

`content/main.lua`:

```lua
local mod = "/Game/Mods/SteelGear/"

return {
    id = "SteelGear",
    assets = {
        {path = mod .. "Icons/T_IngotIcon.T_IngotIcon", expectedClass = "/Script/Engine.Texture2D"},
    },
    items = {
        {
            name = "Ingot",
            template = "IngotQuartzite",
            displayName = "ingot.name",
            description = "ingot.description",
            fields = {Icon = mod .. "Icons/T_IngotIcon.T_IngotIcon", Tier = 2},
        },
    },
}
```

- `name = "Ingot"` creates the row `SteelGear_Ingot`. Use the full name whenever another row or mod refers to it.
- `fields` changes fields of the copy. Field names come from the export.
- `displayName` and `description` are keys of the mod's language files (step 4).

## 3. The recipe

Add a `recipes` section:

```lua
recipes = {
    {
        name = "Ingot",
        template = "BowWorkbench",
        crafts = "Ingot",
        ingredients = {{item = "Clay", count = 2}, {item = "Sap", count = 1}, {item = "AcornShell", count = 1}},
        fields = {CategoryTag = {unreal = '(TagName="Recipe.Crafting.Materials.Refined")'}},
    },
},
```

- `template` is an existing row of `CraftingRecipeTable`. `BowWorkbench` is a plain workbench recipe.
- `crafts` names an item of this mod without the prefix.
- `CategoryTag` decides the tab in the crafting menu. Look at a vanilla recipe of the same kind in `tables/Table_CraftingRecipes.json` or one of the `tables/Table_Crafting_*.json` files to find the tag.
- Ingredients are row names from `Table_AllItems.json`.

Without `unlocked = true` the recipe has to be unlocked. Step 5 sells it at the Ranger terminal.

## 4. Name, description and icon

The text goes into the mod's language files, `text/enus.json` and one file per other language:

```json
{
  "ingot.name": "Steel Ingot",
  "ingot.description": "Crafting material. Made from clay, sap and an acorn shell.",
  "arsenal.title": "Arsenal",
  "arsenal.description": "Recipes for the Steel Ingot, the Steel Helmet and weapons."
}
```

`text/dede.json` has the same keys in German, and so on. A missing language shows the English text. Details: [Add text and translations](tutorial-localization.md).

The icon is a texture, described in `SourceArt/assets.json`:

```json
{
  "destination": "/Game/Mods/SteelGear",
  "assets": [
    {"type": "texture", "kind": "icon", "source": "ModSource/SteelGear/SourceArt/T_IngotIcon.png",
     "folder": "Icons", "name": "T_IngotIcon"}
  ]
}
```

An icon is a square PNG, 256 or 512 pixels, with a transparent background. It is cooked with the rest of the mod when you build it.

## 5. Sell the recipe at the Ranger terminal

```lua
shop = {
    {name = "Arsenal", cost = 500, title = "arsenal.title", description = "arsenal.description", recipes = {"Ingot"}},
},
```

This adds the entry `SteelGear_Arsenal` to the starter terminal, priced at 500 Raw Science, with the texts `arsenal.title` and `arsenal.description`. Buying it unlocks the ingot recipe. Other mods can add their recipes to the same entry, as Fire Dagger and AK-74 do. All options: [Sell recipes at the Ranger terminal](tutorial-shop.md).

## Check

[Build and install](build.md) the mod. Buy the Arsenal at the Ranger terminal. The ingot recipe appears in the crafting menu under refined materials.

If the item name shows as a number or as an empty line, the string table did not load. See [Troubleshooting](trouble-text.md#an-item-has-no-name).

## More

- A helmet uses the same steps with `template = "HeadAnt"` and armor fields. See `SteelGear` for the full example.
- All item and recipe options: [Manifest reference](manifest.md#items).
- Your own 3D model for the item: [Add a weapon with your own model](tutorial-model.md).

Next: [Add a weapon with your own model](tutorial-model.md).
{% endraw %}
