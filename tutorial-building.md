---
title: Make a building with a script
parent: Tutorials
nav_order: 9
---
{% raw %}

# Make a building with a script

<p class="download-stub">Download the finished tutorial project: SlotMachine.zip</p>

This tutorial walks through the Slot Machine example, `ModSource/SlotMachine`. It is a building with its own rigged model. A script moves its lever and reels, shows text on its screen and pays out prizes. Open the example files next to this page.

![The Slot Machine placed in the yard](assets/images/slot-machine.jpg)

Read [Add an item with a recipe](tutorial-item.md) and [Add a weapon with your own model](tutorial-model.md) first.

## 1. The building class

The game tells buildings apart by their Blueprint class. Two buildings with the same class are the same building to the game, in saves and in the build menu. A new building therefore needs its own class.

In `SourceArt/assets.json` the class is one entry:

```json
{"type": "blueprint", "parent": "/Script/Maine.Building", "folder": "Blueprints", "name": "BP_SlotMachine"}
```

In the editor, the same is **Add > Blueprint Class > All Classes > Building**. The class `Building` is there after step 4 of [Authoring setup](authoring.md#4-buildings-the-games-building-class). Save it as `/Game/Mods/SlotMachine/Blueprints/BP_SlotMachine`. The class can stay empty. The model and the behavior come from the manifest and the script.

## 2. The model

The slot machine is a skeletal mesh with bones for the parts that move: `b_lever`, `b_slot_01` to `b_slot_03`, `b_button_plus`, `b_button_minus` and `b_body`.

```json
{"type": "skeletalmesh", "source": "ModSource/SlotMachine/SourceArt/SlotMachine/SK_SlotMachine.fbx",
 "folder": "Meshes", "name": "SK_SlotMachine"},
{"type": "generated", "folder": "Meshes", "name": "SK_SlotMachine_Skeleton"}
```

The `generated` entry tells the cook tool that the import creates the skeleton asset, so it is packed as well.

Give each moving part its own bone and weight it fully to that bone. A script turns and moves bones, but it cannot move single vertices.

## 3. The manifest

`content/slot_machine.lua`, shortened:

```lua
local mod = "/Game/Mods/SlotMachine/"
local function asset(path) local name = path:match("[^/]+$"); return mod .. path .. "." .. name end

return {
    id = "SlotMachine",
    assets = {
        {path = mod .. "Blueprints/BP_SlotMachine.BP_SlotMachine_C", kind = "class", expectedClass = "/Script/Engine.Actor"},
    },
    buildings = {
        {
            name = "SlotMachine",
            template = "LampGnat",
            displayName = "slotMachine.name",
            description = "slotMachine.description",
            fields = {
                ["PlacementData.Actor"] = mod .. "Blueprints/BP_SlotMachine.BP_SlotMachine_C",
                CozinessContribution = 2,
            },
            model = {skeletal = asset("Meshes/SK_SlotMachine"), poseable = true},
        },
    },
    rows = {
        {table = "BuildingRecipeTable", template = "LampGnat", name = "SlotMachine", fields = {
            Building = {handle = {table = "BuildingsTable", row = "SlotMachine_SlotMachine"}},
            Requirements = {ingredients = {{item = "Clay", count = 4}, {item = "Sap", count = 3}, {item = "QuartzShard", count = 1}}},
            CategoryTag = {unreal = '(TagName="Recipe.Building.Decoration.Decor.Furniture")'},
        }},
    },
}
```

- The building row copies the Gnat Lamp and points `PlacementData.Actor` at the new class. The `_C` at the end names the generated class of the Blueprint.
- `poseable = true` lets the script move bones.
- The model gets an invisible blocking box from its bounds, so the player cannot walk through it.
- The recipe row in `BuildingRecipeTable` puts the building in the build menu. `CategoryTag` picks the tab.
- The full example also sells the building at the Ranger terminal with a `shop` entry. See [Sell recipes at the Ranger terminal](tutorial-shop.md#a-building-at-the-terminal).

## 4. The script

Scripts are files in `content/scripts/`. A script returns a function that gets the `api` table:

```lua
return function(api, settings)
    local machines = {}

    api.onBuilding("SlotMachine_SlotMachine", function(building)
        machines[building.key()] = {building = building, bet = 10}
        building.label("screen", "BET 10", {
            bone = "b_body",
            offset = {X = -0.02, Y = 0.19, Z = 0.53},
            rotation = {Pitch = 28, Yaw = -90, Roll = 180},
            size = 9,
            color = {1, 0.85, 0.3},
        })
    end)

    api.onKey("E", function()
        for _, machine in pairs(machines) do
            if machine.building.valid() and api.aimedBone(machine.building, {"b_lever"}, 400, 45) then
                if api.science.remove(machine.bet) then
                    machine.building.turn("b_lever", "x", 60)
                    api.after(300, function() machine.building.turn("b_lever", "x", 0) end)
                end
            end
        end
    end)
end
```

- `onBuilding` runs for each slot machine that appears, also for machines loaded from a save.
- `label` puts text on the model in the game's font. `offset` and `rotation` are in the bone's space. Change them until the text sits on the screen. The angle is yours to choose.
- `aimedBone` returns the bone the player looks at within 400 cm.
- `turn` rotates a bone around one of its axes, in degrees.

The full script animates the reels in steps of 60 degrees, picks three symbols with `api.random`, and pays Raw Science with `api.science.add` or throws an item with `api.drop`. All functions are listed in [Scripting](scripting.md).

## 5. Keep buildings when the mod is removed

Add `"preserve": true` to `mod.json`. The framework then records where the mod's buildings stand in each world. While the mod is removed they are hidden, and when it is installed again they come back. Without it, placed buildings of a removed mod are lost on the next save. See [Removing mods](play-removing.md).

## Check

[Build and install](build.md) the mod. In the game, open the build menu and find the slot machine under furniture. The menu shows your model. Place it, look at the lever and press E.

If the building does not appear in the menu, see [Troubleshooting](trouble-buildings.md#a-building-is-missing-from-the-build-menu).

Next: [Add a storage chest](tutorial-storage.md).
{% endraw %}
