---
title: Scripting
parent: Reference
nav_order: 4
---
{% raw %}

# Scripting

Files in `content/scripts/*.lua` are the mod's code. They load in file name order when the game starts and have the whole [UE4SS Lua API](https://docs.ue4ss.com/lua-api.html): finding objects, calling game functions, hooks, key binds. Each one returns a function that receives the `api` table with Amber's helpers and the mod's settings:

```lua
return function(api, settings)
    api.log("loaded")
end
```

The function runs once, early, before the world exists. Register callbacks there (`onBuilding`, `onKey`, `onSettings`, `after`) and touch the world only inside them. All callbacks run on the game thread.

`settings` is the mod's settings table. Its values change when the player edits them in the [Mods screen](play-in-game.md).

Tutorial: [Make a building with a script](tutorial-building.md). Full example: `ModSource/SlotMachine/content/scripts/slot_machine.lua`.

## Contents

- [api reference](#api-reference)
- [Buildings](#buildings)
- [Creatures](#creatures)
- [Text on a model](#text-on-a-model)
- [Keys](#keys)
- [Windows](#windows)
- [World variables](#world-variables)
- [Trust and errors](#trust-and-errors)

## api reference

| Function | Returns | Meaning |
| --- | --- | --- |
| `api.log(text)` | | Writes `[CF] <mod>: text` to the UE4SS log. |
| `api.onBuilding(row, fn)` | | Calls `fn(building)` for every building of that row, see [Buildings](#buildings). |
| `api.onCreature(row, fn)` | | Calls `fn(creature)` for every creature of that row near the players, see [Creatures](#creatures). |
| `api.onKey(name, fn)` | | Calls `fn()` when the key is pressed, see [Keys](#keys). |
| `api.onWorld(fn)` | | Calls `fn()` once each time a world is loaded. On a player who joins someone else's world it is not tested yet. |
| `api.loadClass(path[, keep])` | class or `nil` | Loads a Blueprint class such as `/Game/UI/Buttons/UI_IconSelectorButton.UI_IconSelectorButton_C` and returns the class the game keeps using. Load a class this way before `RegisterHook` on its functions. The engine can unload a class nobody uses and load it again later, which drops hooks on the old one, so check `class:GetAddress()` and hook again when it changes. `keep = true` holds the class for the whole session, for a class whose defaults the mod changes. |
| `api.text(key, args)` | string | The mod's text for a key of its [language files](tutorial-localization.md), in the player's language. `{name}` in the text is replaced by `args.name`. |
| `api.onLanguage(fn)` | | Calls `fn()` when the player switches the game's language. |
| `api.onSettings(fn)` | | Calls `fn(key, value)` when the player changes a setting in the game or presses a `button` setting. |
| `api.after(ms, fn)` | | Calls `fn()` once after `ms` milliseconds. Cannot be cancelled. |
| `api.random(n)` | 1 to n | Whole random number. |
| `api.player()` | `{X, Y, Z}` | Player position in cm. |
| `api.playSound(path, volume, pitch)` | | Plays a sound asset of a mod or the game for this player, at the same volume wherever they stand. `volume` and `pitch` default to 1. Example: [Replace a game chest](tutorial-chest.md). |
| `api.playSoundAt(path, at, volume, pitch)` | | Plays a sound asset at `at = {X, Y, Z}`, fading with distance as far as the asset's `falloffDistance`. Example: `ModSource/SlotMachine/content/scripts/slot_machine.lua`. |
| `api.view()` | `{origin, forward}` | Camera position and direction. |
| `api.facing(normal, up)` | `{Pitch, Yaw, Roll}` | Rotation whose forward is `normal`, for labels lying on a surface. `up` defaults to `{X = 0, Y = 0, Z = 1}`. |
| `api.science.get()` | number | Raw Science of the party. |
| `api.science.add(n)` | `true` | Adds Raw Science. |
| `api.science.remove(n)` | boolean | Removes it. Returns `false` and changes nothing if the party has less. |
| `api.giveKeyItem(row)` | | Gives a note or audio log to the party. Tutorial: [Add a note and an audio log](tutorial-notes.md). |
| `api.drop(item, count, at, velocity)` | `true` | Spawns `count` (1 to 999) of an item row at `at = {X, Y, Z}`. With `velocity = {X, Y, Z}` in cm/s the items are thrown. |
| `api.aimedBone(building, names, reach, tolerance)` | name or `nil` | The bone from `names` closest to where the player looks, within `reach` cm and `tolerance` cm of the view line. |
| `api.tag(actor, name)` | `true` | Adds an actor tag, such as the one a [quest](tutorial-quests.md#4-the-marker) marker points at. |
| `api.marker(at, {icon, color})` | handle with `remove()` | A marker at `at = {x, y, z}` over the world and on the map, with a Trail Marker's icon and color. `icon` is a name from the mod's [markers](manifest.md#markers) or a game icon number. `color` is a hex from the mod's colors or a game color number. Place it again in `api.onWorld`: it lasts until the world is left. |
| `api.dialog(spec)` | | The game's confirmation window, see [Windows](#windows). |
| `api.windowButton(spec)` | | A button in the bottom bar of a chest, station or workbench window, see [Buttons in building windows](#buttons-in-building-windows). |
| `api.onWindow(spec)` | | The look of a building's window and a function when it opens, see [Buttons in building windows](#buttons-in-building-windows). |
| `api.itemRow(item)` | row name | The `AllItemsTable` row of an item object, such as an entry of an inventory's `GetItems()`. |
| `api.mods()` | list | The mods of this session: id, name, version, author, description, settings. |
| `api.modManager()` | object or `nil` | The mods of this session and their settings, which the Mods Menu mod changes. `nil` when the mod manager gave no mod list. |
| `api.placement()` | object or `nil` | The held item placement tool for authors, when Developer mode is on in the mod manager. |
| `api.net` | | Messages between players, see [Multiplayer](multiplayer.md#messages-between-players). |
| `api.conversation` | | Dialogs of the mod: talking terminals, subtitles, trigger boxes and calls from Sloane, see [Add terminal dialogs](tutorial-dialogs.md#3-start-it-from-a-script) and [Add character conversations](tutorial-lines.md). |
| `api.variables` | | Values the game saves with the world, see [World variables](#world-variables). |
| `api.effects` | | Gives, takes and counts status effects and runs a function when the game adds or removes one, see [Add a status effect](tutorial-effects.md#4-from-a-script). |

`player`, `view`, `science` and `drop` need the world. Calling them in the main menu fails. In multiplayer, call `science` and `drop` on the host. Everything else the game offers is reached with UE4SS directly. `ModSource/AmberModMenu` builds its whole screen that way.

## Buildings

```lua
api.onBuilding("MyMod_SlotMachine", function(building)
    building.turn("b_lever", "x", 60)
    building.shift("b_button_plus", "y", -2)
end)
```

`onBuilding` takes the full row name with the mod prefix. It runs once for every building of that row that appears, including ones loaded from a save. It only runs for buildings whose row has a [model](models.md).

| Function | Meaning |
| --- | --- |
| `building.valid()` | `false` once the building is gone. |
| `building.key()` | Unique id of this building for the session. |
| `building.location()` | Building position `{X, Y, Z}`. |
| `building.bone(name)` | World position of a bone. |
| `building.boneAxes(name)` | World directions of the bone's axes `{x, y, z}`. |
| `building.turn(name, axis, degrees)` | Rotates a bone from its rest pose. `"x"` rolls, `"y"` pitches, `"z"` yaws. Absolute, not added. |
| `building.shift(name, axis, cm)` | Moves a bone from its rest position along its own axis. Absolute. |
| `building.label(name, text, options)` | Text on the model, see below. |
| `building.tag(name)` | Adds an actor tag to the building, for a [quest](tutorial-quests.md#4-the-marker) marker. |
| `building.actor` | The building's actor, for the game's own functions on it. |

`turn` and `shift` need the model to have `"poseable": true` in `SourceArt/assets.json`.

## Creatures

```lua
api.onCreature("GiantAphid_Aphid", function(creature)
    creature.onDamaged(function(amount)
        api.drop("Honeydew", 1, creature.location())
    end)
end)
```

`onCreature` takes a row of `Table_CharacterData`, a game creature such as `Ant_Soldier_Black` or a mod's own with its prefix. Far from the players a creature is only a record, and the game makes the full creature when a player comes near. The function runs each time that happens, and once for every living creature already near when a world loads.

| Function | Meaning |
| --- | --- |
| `creature.valid()` | `false` once the full creature is gone, dead or far again. |
| `creature.key()` | Unique id of this full creature for the session. |
| `creature.row()` | Its row in `Table_CharacterData`. |
| `creature.location()` | Position `{X, Y, Z}`. |
| `creature.health()` | Current and maximum health, two numbers. |
| `creature.dead()` | `true` once it died. |
| `creature.behavior()` | What its AI does now, for example `"Wander"`, `"Flee"`, `"Combat"` or `"Idle"`. |
| `creature.moveTo(at, radius)` | Its AI walks to `at = {X, Y, Z}` and stops within `radius` cm, 50 by default. Returns `false` when no path leads there. The behavior tree gives it the next goal afterwards. |
| `creature.kill()` | Kills it, as if its health ran out. |
| `creature.onDamaged(fn)` | Calls `fn(amount)` each time it takes damage. |
| `creature.onDeath(fn)` | Calls `fn()` when it dies. |
| `creature.actor()` | The creature's actor, for the UE4SS API. |

A creature's AI runs on the host, so in multiplayer `onDamaged` and `moveTo` work in the host's scripts. Behavior settings and own behavior trees are in [Add creatures](tutorial-creatures.md#5-behavior-and-loot).

## Text on a model

```lua
building.label("screen", "BET 10", {
    bone = "b_body",
    offset = {X = 0, Y = 0.2, Z = 0.5},
    rotation = {Pitch = 28, Yaw = -90, Roll = 180},
    size = 9,
    color = {1, 0.85, 0.3},
    font = "title",
})
```

| Option | Default | Meaning |
| --- | --- | --- |
| `bone` | required | Bone the text follows. |
| `offset` | `{0, 0, 0}` | Position in the bone's space, in model units. |
| `rotation` | `{0, 0, 0}` | Angle in the bone's space, in degrees. |
| `size` | 12 | Height of one line in world units. |
| `color` | white | `{r, g, b}` or `{r, g, b, a}`, 0 to 1. |
| `font` | `"title"` | `"title"` (headings such as item names), `"body"` (descriptions) or a loaded font asset path. |

Calling `label` again with the same name changes the text.

The text can be a key of the mod's language files instead, with values for its `{name}` parts. Such a label is drawn again in the new language when the player switches it:

```lua
building.label("screen", {text = "slot.bet", args = {bet = 10}}, {bone = "b_body", size = 9})
```

With `"slot.bet": "BET {bet}"` in `text/enus.json` and `"EINSATZ {bet}"` in `text/dede.json`, the screen shows BET 10 or EINSATZ 10.

Placed in the world instead of on a bone:

```lua
building.label("sign", "TEXT", position, rotation, size, color, {font = "body"})
```

## Keys

`api.onAction` adds a key the player can bind in the game's Options, under Keyboard. Tutorial: [Add a key the player can bind](tutorial-key.md).

```lua
api.onAction{name = "Mark", label = {text = "action.mark"}, key = "K", onPress = function() ... end}
```

`api.onKey` listens to one fixed key, which the player cannot change:

```lua
api.onKey("E", function()
    local bone = api.aimedBone(building, {"b_lever", "b_button_plus"}, 400, 45)
    if bone == "b_lever" then ... end
end)
```

Key names are UE4SS names: `A` to `Z`, `ZERO` to `NINE` (not `"1"`), `F1` to `F24`, `SPACE`, `RETURN`, `ESCAPE`, `TAB`, `LEFT_ARROW`, `UP_ARROW`, `RIGHT_ARROW`, `DOWN_ARROW`, `LEFT_MOUSE_BUTTON`, `RIGHT_MOUSE_BUTTON`, `MIDDLE_MOUSE_BUTTON` and others. Modifier keys cannot be combined. A key fires in menus too, so check what the player is looking at first.

## Windows

```lua
api.dialog{
    title = "SLOT MACHINE",
    body = "Long text scrolls.",
    accept = "Play", cancel = "Back",
    onAccept = function() ... end,
    onCancel = function() ... end,
}
```

The game's own confirmation window with your title, text and button labels. Without `cancel` it has one button. `title` and `body` are required. Each of them can also be a key, `{text = "key", args = {...}}`.

### Buttons in building windows

```lua
api.windowButton{
    building = {"Storage", "StorageBig"},
    label = {text = "button.store"},
    onPress = function(building)
        local storage = building.actor:GetComponentByClass(StaticFindObject("/Script/Maine.InventoryComponent"))
        api.log(building.row .. " holds " .. storage:GetTotalItemCount() .. " items")
    end,
}
```

The button is the game's own bottom-bar button, placed before **Close** in the window of the buildings you name: chests, production stations such as the Oven, and crafting stations such as the workbench. `building` is a `BuildingsTable` row, a list of rows or `"*"` for every building. Rows of mods take the mod prefix, as `BaseBuildings_Chest`. `label` is text or a key. `key` is an Unreal key name such as `"G"` or `"F5"`: the button shows it, the key presses it while the window is open, and **Options** lists it under the UI controls, where the player can bind another key. The game keeps that key in its own settings by the label's text key, so keep the key of a released button's label. Choose a key the window does not use already. `onPress` gets the building, as in [Buildings](#buildings), with `building.row` set. Tutorial: [Add a button to a building window](tutorial-window-button.md).

```lua
api.onWindow{
    building = "MyMod_Chest",
    title = {text = "chest.name"},
    onOpen = function(window)
        window.hide("HotDepositBox")
        window.find("UI_ItemDescriptionBox"):SetRenderOpacity(0.5)
    end,
}
```

`onWindow` takes the same keys as a manifest's [windows](manifest.md#windows) entry, with `title` as text or a key. `onOpen` runs after the game has filled the window. `onClose` runs when it closes and gets the building. `window.widget` is the game's window, `window.find(name)` one of its widgets, `window.hide(name)` leaves one out, `window.title(text)` sets the header and `window.building` is the building. Whatever a script changes in the window is done with UE4SS on the game's own widgets.

## World variables

A mod can keep its own values in the player's world, for example whether a lever was pulled. The game saves them with the world, like its own quest state. Declare them in `variables.json` in the mod folder:

```json
{
  "leverPulled": false,
  "visits": 0,
  "stage": {"default": 0, "type": "Uint8"}
}
```

A value is the default (`true`/`false` or a whole number), or `{"default": ..., "type": ...}` with one of the game's types: `Bool`, `Uint8`, `Uint16`, `Uint32`, `GameState`. Without a type a variable is `Uint32`, also for `true` and `false`. `python Tools/cook_assets.py ModSource/<id>` builds them with the mod's other assets, so Unreal Engine is needed ([Authoring setup](authoring.md)).

| Function | Returns | Meaning |
| --- | --- | --- |
| `api.variables.get(name)` | number | The value in this world. `true` and `false` read as 1 and 0. |
| `api.variables.set(name, value)` | | Sets `true`, `false` or a whole number from 0 to 2147483647. |
| `api.variables.id(name)` | GUID | The variable's id, for the game's own functions that take one. |

In multiplayer the host's world is the one that is saved, so `set` on a player's game is sent to the host. This is not tested with two players yet.

## Trust and errors

Scripts are code with the same access as any UE4SS mod.

- An error while a script loads is logged as `<mod>: script failed: <error>`. The mod's data still applies and other mods are not affected.
- An error inside a callback is logged as `<mod>: building handler failed` (or key, timer, settings, dialog, window button) and the callback keeps working for the next event.
{% endraw %}
