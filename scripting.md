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

`settings` is the mod's settings table. Settings marked `live` change in this table when the player edits them in the [Mods screen](play-in-game.md).

Tutorial: [Make a building with a script](tutorial-building.md). Full example: `ModSource/SlotMachine/content/scripts/slot_machine.lua`.

## Contents

- [api reference](#api-reference)
- [Buildings](#buildings)
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
| `api.onKey(name, fn)` | | Calls `fn()` when the key is pressed, see [Keys](#keys). |
| `api.onWorld(fn)` | | Calls `fn()` once each time a world is loaded, on every player's game. |
| `api.loadClass(path[, keep])` | class or `nil` | Loads a Blueprint class such as `/Game/UI/Buttons/UI_IconSelectorButton.UI_IconSelectorButton_C` and returns the class the game keeps using. Load a class this way before `RegisterHook` on its functions. The engine can unload a class nobody uses and load it again later, which drops hooks on the old one, so check `class:GetAddress()` and hook again when it changes. `keep = true` holds the class for the whole session, for a class whose defaults the mod changes. |
| `api.onSettings(fn)` | | Calls `fn(key, value)` when the player changes a live setting. |
| `api.after(ms, fn)` | | Calls `fn()` once after `ms` milliseconds. Cannot be cancelled. |
| `api.random(n)` | 1 to n | Whole random number. |
| `api.player()` | `{X, Y, Z}` | Player position in cm. |
| `api.view()` | `{origin, forward}` | Camera position and direction. |
| `api.facing(normal, up)` | `{Pitch, Yaw, Roll}` | Rotation whose forward is `normal`, for labels lying on a surface. `up` defaults to `{X = 0, Y = 0, Z = 1}`. |
| `api.science.get()` | number | Raw Science of the party. |
| `api.science.add(n)` | `true` | Adds Raw Science. |
| `api.science.remove(n)` | boolean | Removes it. Returns `false` and changes nothing if the party has less. |
| `api.drop(item, count, at, velocity)` | `true` | Spawns `count` (1 to 999) of an item row at `at = {X, Y, Z}`. With `velocity = {X, Y, Z}` in cm/s the items are thrown. |
| `api.aimedBone(building, names, reach, tolerance)` | name or `nil` | The bone from `names` closest to where the player looks, within `reach` cm and `tolerance` cm of the view line. |
| `api.tag(actor, name)` | `true` | Adds an actor tag, such as the one a [quest](tutorial-quests.md#4-the-marker) marker points at. |
| `api.marker(at, {icon, color})` | handle with `remove()` | A marker at `at = {x, y, z}` over the world and on the map, with a Trail Marker's icon and color. `icon` is a name from the mod's [markers](manifest.md#markers) or a game icon number. `color` is a hex from the mod's colors or a game color number. Place it again in `api.onWorld`: it lasts until the world is left. |
| `api.dialog(spec)` | | The game's confirmation window, see [Windows](#windows). |
| `api.mods()` | list | The mods of this session: id, name, version, enabled, settings. |
| `api.modManager()` | object or `nil` | Turning mods on and off and changing settings, as the Mods Menu mod does. `nil` when the mod manager gave no mod list. |
| `api.placement()` | object or `nil` | The held item placement tool for authors, when Author tools are on in the mod manager. |
| `api.net` | | Messages between players, see [Multiplayer](multiplayer.md#messages-between-players). |
| `api.conversation` | | Dialogs of the mod: talking terminals, subtitles, trigger boxes and calls from Sloane, see [Add terminal dialogs](tutorial-dialogs.md#3-start-it-from-a-script) and [Add lines in the world](tutorial-lines.md). |
| `api.variables` | | Values the game saves with the world, see [World variables](#world-variables). |

`player`, `view`, `science` and `drop` need the world. Calling them in the main menu fails. In multiplayer, call `science` and `drop` on the host. Everything else the game offers is reached with UE4SS directly. `ModSource/AmberModMenu` builds its whole screen that way.

## Buildings

```lua
api.onBuilding("MyMod_SlotMachine", function(building)
    building.turn("b_lever", "x", 60)
    building.shift("b_button", "y", -2)
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

`bone`, `boneAxes`, `turn` and `shift` need the model to have `poseable = true`.

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

Placed in the world instead of on a bone:

```lua
building.label("sign", "TEXT", position, rotation, size, color, {font = "body"})
```

## Keys

```lua
api.onKey("E", function()
    local bone = api.aimedBone(building, {"b_lever", "b_button"}, 400, 45)
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

The game's own confirmation window with your title, text and button labels. Without `cancel` it has one button. `title` and `body` are required.

## World variables

A mod can keep its own values in the player's world, for example whether a lever was pulled. The game saves them with the world, like its own quest state. Declare them in `variables.json` in the mod folder:

```json
{
  "leverPulled": false,
  "visits": 0,
  "stage": {"default": 0, "type": "Uint8"}
}
```

A value is the default (`true`/`false` or a whole number), or `{"default": ..., "type": ...}` with one of the game's types: `Bool`, `Uint8`, `Uint16`, `Uint32`. `python Tools/cook_assets.py ModSource/<id>` builds them with the mod's other assets, so Unreal Engine is needed ([Authoring setup](authoring.md)).

| Function | Returns | Meaning |
| --- | --- | --- |
| `api.variables.get(name)` | number | The value in this world. `true` and `false` read as 1 and 0. |
| `api.variables.set(name, value)` | | Sets `true`, `false` or a whole number from 0 to 2147483647. |
| `api.variables.id(name)` | GUID | The variable's id, for the game's own functions that take one. |

In multiplayer the host's world is the one that is saved, so `set` on a player's game is sent to the host.

## Trust and errors

Scripts are code with the same access as any UE4SS mod. The mod manager lists a mod's scripts and asks the player before the first session, and again whenever a script changes.

- An error while a script loads is logged as `<mod>: script failed: <error>`. The mod's data still applies and other mods are not affected.
- An error inside a callback is logged as `<mod>: building handler failed` (or key, timer, settings, dialog) and the callback keeps working for the next event.
{% endraw %}
