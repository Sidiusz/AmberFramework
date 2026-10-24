---
title: Make your first mod
parent: Tutorials
nav_order: 1
---
{% raw %}

# Make your first mod

<p class="download-stub">Download the finished tutorial project: SaberBoost.zip</p>

This mod raises the damage of the Crimson Saber combo. It changes three numbers in the game data and nothing else.

The finished mods of this page are in `ModSource/Tutorials/SaberBoost` and `ModSource/Tutorials/BetterDrops` of the modder kit, `AmberFramework-ModderKit.zip`. The kit also has `Tools/` with `pack_mod.py` and every example mod with its sources.

You need Grounded 2 Mod Manager with Amber Framework installed (see [Playing with mods](players.md)). Unreal Engine is not needed for this tutorial.

## 1. Find the names

Every change in a mod names a table, a row and a field. Get them from your own game:

1. In the mod manager, press **Export game data**. After about a minute a folder opens.
2. Open `index.json` and search for "Attacks". The table with player weapon attacks is `/Game/Blueprints/Attacks/AllAttacks.AllAttacks`, written to `tables/AllAttacks.json`.
3. Open `tables/AllAttacks.json` and search for `SwordAntRed`. The Crimson Saber combo has three rows: `SwordAntRed`, `SwordAntRed2` and `SwordAntRed3`.
4. In each row, the damage is `DamageData`, a struct. It starts with `(Damage=21.000000,...` (23 and 26 in the other two rows). The field to change is `DamageData.Damage`.

More about the export: [Game data](game-data.md). For models, icons and other assets see [Explore the game files](tutorial-game-files.md).

## 2. Create the mod folder

Create a folder `SaberBoost` with this layout:

```text
SaberBoost/
  mod.json
  content/main.lua
```

If you have the [editor plugin](editor-plugin.md), **Amber Framework > New Mod...** with the template "Change game data" creates the same files.

`mod.json`:

```json
{
  "id": "SaberBoost",
  "name": "Saber Boost",
  "version": "1.0.0",
  "apiVersion": 2,
  "author": "Your name",
  "description": "Crimson Saber combo damage 21/23/26 -> 32/35/40.",
  "category": "Balance"
}
```

All fields are explained in [Mod folder and mod.json](create-a-mod.md).

## 3. Write the change

`content/main.lua`:

```lua
local attacks = "/Game/Blueprints/Attacks/AllAttacks.AllAttacks"

return {
    id = "SaberBoost",
    patches = {
        {table = attacks, row = "SwordAntRed", set = {["DamageData.Damage"] = 32}},
        {table = attacks, row = "SwordAntRed2", set = {["DamageData.Damage"] = 35}},
        {table = attacks, row = "SwordAntRed3", set = {["DamageData.Damage"] = 40}},
    },
}
```

- Each line names a row and the fields to change in it. Fields you do not name keep their values, and other mods can change them.
- `DamageData.Damage` is the `Damage` field inside `DamageData`. The square brackets and quotes are needed because of the dot.
- `set` replaces the number. `multiply = {["DamageData.Damage"] = 1.5}` would scale it instead, and `row = "SwordAntRed*"` would change every row whose name starts with `SwordAntRed`. See [Manifest reference](manifest.md#patches).

## 4. Install

This mod has no models, so the folder installs as it is: drag the `SaberBoost` folder onto the mod manager window. To share it, zip the folder. Building a pak and mods with models are on [Build and install](build.md).

After installing, the mod appears in the list. If the row shows a warning, read it. [Troubleshooting](troubleshooting.md) lists the common ones.

## 5. Check it in the game

1. Press **Play Modded**.
2. In the main menu, the version text ends with "Modded: Amber Framework, ... mods".
3. Open the game console with the `~` key (UE4SS's ConsoleEnablerMod turns it on) and type `cfstatus`. The answer appears in the UE4SS window and in `ue4ss/UE4SS.log`: `SaberBoost: applied` means the patches were written. The UE4SS window shows when `GuiConsoleEnabled = 1` is set in `UE4SS-settings.ini`.
4. Run `cfinspect /Game/Blueprints/Attacks/AllAttacks.AllAttacks SwordAntRed` to list the row, or hit a creature with the Crimson Saber.

## 6. Changing other game data

The same manifest changes any data of the game. Creature health and loot are part of the example `ModSource/GameTweaks`. All keys are in the [Manifest reference](manifest.md).

### Creature health

```lua
creatures = {
    {creature = "Weevil", healthMultiplier = 3},
},
```

`creature` is the row in the creature table. `health = 120` sets the number instead. See [classes and creatures](manifest.md#classes).

### Chest sizes

```lua
storage = {
    {building = "StorageBig", slots = 50},
},
```

The game's chests have 20 (Storage Basket), 40 (Storage Chest) and 60 (Large Storage Chest) slots. Chests already placed in a world get the new size too. See [storage](manifest.md#storage).

### Production time

Recipes at stations take game hours. Most recipes use their station's time. A recipe gets its own with `bOverridesProductionTime`:

```lua
patches = {
    {table = "CraftingRecipeTable", row = "FireBrick", set = {bOverridesProductionTime = true, ProductionTime = 0.5}},
},
```

Fire Bricks in the Oven now take half a game hour.

### Loot

Creature drops are not in a data table. Each creature's Blueprint has its own drop list. **Export game data** in the mod manager reads all of them from the game's files and writes `loot.json` next to the tables:

```text
%LOCALAPPDATA%\G2Launcher\GameData\<game version>\loot.json
```

```json
"BP_Weevil_C": [{"item": "WeevilNose", "count": 1, "chance": 0.3, "multiplier": 1, "type": 0}, {"item": "WeevilMeat", "count": 1, "chance": 1, ...}]
```

The key is the class name, the list is its drops with the original values. Search the file for the creature, for example `Weevil` or `Ant_`. Grass, plants, food and containers with drops are in the same file.

```lua
return {
    id = "BetterDrops",
    loot = {
        {source = "BP_Weevil_C", item = "WeevilNose", set = {chance = 1}},
        {source = "BP_Ant_*", item = "AntHead", multiply = {chance = 2}},
    },
}
```

- `source` is the class name. `*` matches any part, so `BP_Ant_*` covers every ant class.
- `set`, `add`, `subtract`, `multiply` and `divide` change `chance` (0 to 1), `count` or `multiplier` of that drop.

Other rule types:

```lua
{source = "BP_Snail_*", item = "SnailSlime", remove = true},                              -- drop no more
{source = "BP_Ladybug_*", drop = {item = "SteelGear_Ingot", count = 1, chance = 0.25}}, -- new drop
```

Rules always start from the original list. Two mods that multiply the same chance both apply. When two mods `set` the same value, the later one in load order wins.

All loot options: [loot](manifest.md#loot).

## Two mods on one item

The example mod Game Tweaks changes the Crimson Saber's damage and recipe. Another mod that changes only the recipe and this one, which changes only the damage, both apply, because they change different fields.

If you install Game Tweaks next to this mod, both set `DamageData.Damage` of the same rows. Values are never added together: the mod later in load order wins, and the log says which one overrides which. To combine with other mods instead, use `multiply` in place of `set`.

Next: [Explore the game files](tutorial-game-files.md).
{% endraw %}
