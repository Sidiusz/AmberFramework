---
title: Add a storage chest
parent: Tutorials
nav_order: 11
---
{% raw %}

# Add a storage chest

<p class="download-stub">Download the finished tutorial project: TreasureChest.zip</p>

This page builds the Treasure Chest from `ModSource/BaseBuildings` as a separate mod, TreasureChest. It is a storage building with its own model and 60 slots, sold at the Ranger terminal. It uses the game's own storage window and keeps its contents in saves.

The finished mod is in `ModSource/Tutorials/TreasureChest`.

![The Treasure Chest and its storage window with 60 slots](assets/images/treasure-chest.jpg)

Read [Make a building with a script](tutorial-building.md) first. This page makes a building class the same way, without a script.

## 1. The model

`SourceArt/TreasureChest_model.json` is the spec of a Blender step, `"blender": [{"script": "Tools/ExampleArt/prepare_model.py", "spec": "SourceArt/TreasureChest_model.json"}]` in `assets.json`, which prepares it before the import:

```json
{
  "name": "SM_TreasureChest",
  "kind": "building",
  "source": "ModSource/Tutorials/TreasureChest/SourceArt/Chest/stylized-chest.fbx",
  "frontAxis": "+X",
  "widthCm": 150,
  "albedo": "ModSource/Tutorials/TreasureChest/SourceArt/Chest/textures/chest_baseColor.png",
  "iconSize": 512, "iconRoll": 0, "iconDirection": [1.0, -0.6, 0.5],
  "fbx": "Build/Tutorials/TreasureChest/SM_TreasureChest.fbx",
  "icon": "Build/Tutorials/TreasureChest/T_TreasureChestIcon.png"
}
```

| Key | Meaning |
| --- | --- |
| `kind` | `building`: the origin goes to the bottom centre and the widest side is scaled to `widthCm`. The game's Storage Chest is about 150 cm wide. |
| `frontAxis` | The side of the source model that faces the player. |
| `albedo` | The color texture, for the icon. Needed when the source file does not link its textures, as with most FBX files. |

The textures are packed into the game's material inputs with `Tools/ExampleArt/pack_textures.py`, as in [Add a weapon with your own model](tutorial-model.md#3-textures). The snippets below are shortened: the full `assets.json` also has the `staticmesh` entry and the material's other textures (normal, RMA, emissive, masks).

## 2. The class

A chest needs its own class, like every new building. The `building` entry makes it a child of the Storage Chest's class, so the chest gets the inventory, the storage window and the deposit buttons of the game's chests:

```json
{"type": "material", "folder": "Materials", "name": "MI_TreasureChest",
 "parent": "/Game/_Augusta/Art/Items/Weapons/Gun_Paintball/Textures/MI_Weapon_Gun_Paintball_Equip.MI_Weapon_Gun_Paintball_Equip",
 "textures": {"Albedo": "/Game/Mods/TreasureChest/Textures/T_TreasureChest_C.T_TreasureChest_C"}},
{"type": "building", "name": "Chest", "template": "StorageBig", "mesh": "Meshes/SM_TreasureChest",
 "material": "Materials/MI_TreasureChest"}
```

## 3. The manifest

```lua
buildings = {
    {
        name = "Chest",
        template = "StorageBig",
        displayName = "chest.name",
        description = "chest.description",
        storage = {slots = 60},
        fields = {
            ["IconSoft"] = asset("Icons/T_TreasureChestIcon"),
        },
        model = "Chest",
    },
},
rows = {
    {table = "BuildingRecipeTable", template = "StorageBig", name = "Chest", fields = {
        ["Building"] = {handle = {table = "BuildingsTable", row = "TreasureChest_Chest"}},
        ["Requirements"] = {ingredients = {{item = "SteelGear_Ingot", count = 2}, {item = "GrassPlank", count = 6}}},
    }},
},
shop = {
    {name = "Vault", cost = 200, title = "vault.title", description = "vault.description", buildings = {"Chest"}},
},
windows = {
    {building = "Chest", title = "chest.name"},
},
```

- `template = "StorageBig"` copies the Storage Chest row. `model = "Chest"` points it at the class of step 2.
- `storage = {slots = 60}` sets the size. The game's chests have 20, 40 and 60 slots.
- The recipe uses Steel Gear's Steel Ingot, so `mod.json` lists `SteelGear` as a dependency.
- The building recipe and the terminal entry work as in [Sell recipes at the Ranger terminal](tutorial-shop.md#a-building-at-the-terminal).
- `windows` gives the chest's window the chest's name as its title, in place of the game's "Storage". See [windows](manifest.md#windows).

## Sizes of the game's chests

A mod can change the size of a chest from the game without a new building:

```lua
storage = {
    {building = "StorageBig", slots = 50},
}
```

The size applies to new chests and to chests already built, also in old saves. Items past a lowered size stay in the save. See [storage](manifest.md#storage).

## Check

[Build and install](build.md) the mod. Buy the Vault at the Ranger terminal, build the chest and open it: the storage window shows 6 rows of 10 slots. Put items in, save, load the save: the items are still there.
{% endraw %}
