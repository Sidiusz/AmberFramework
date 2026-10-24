---
title: Multiplayer
parent: Reference
nav_order: 9
---
{% raw %}

# Multiplayer

The host and every player need the same mods in the same versions. Each player's game applies the mods itself. The game only sends what it always sends, such as which item row is in a slot.

## What runs where

| Part of a mod | Runs on | Why |
| --- | --- | --- |
| Data: items, recipes, rows, patches, loot, classes, text | Every player | Each game reads its own tables. A player without the mod has no row for the item. |
| Models, materials, signs, storage sizes | Every player | Drawn by each game. |
| Map pieces and foliage (`level`, `foliage`) | Every player | Hidden by each game. |
| Levels of the mod (`levels`) | Every player | Each game loads its own copy. Put only things that need no syncing in a level: meshes, lights, decoration. |
| Items placed once per world (`world`), moved pickups | Host | The host places them, and the game sends them to every player. |
| New creatures | Host spawns, every player applies the model | The host spawns them. Size and model are not sent, so every player's framework finds them by their row and applies both. |
| Restored buildings (`preserve`) | Host | |
| Recipes known from the start (`unlocked`) | Host | Known recipes belong to the party. |
| World variables (`api.variables`) | Host | The host's world is saved, and a player's change is sent to the host. |
| Conversations and terminals | Every player | Each game shows its own conversation window. |

`api.drop` and `api.science` change the world, so call them on the host (`api.net.isHost()`).

## Who needs a mod

The mod author says it in `mod.json`:

```json
"multiplayer": "both"
```

| Value | Meaning | Examples |
| --- | --- | --- |
| `"both"` (default) | The host and every player need it. | New items, creatures, buildings, recipes, data changes |
| `"client"` | Only whoever installs it. Others play without it. | A minimap, a skin, a menu |
| `"host"` | Only the host needs it. | Changes only the host's world makes, such as items placed once per world |

The mod manager shows "multiplayer: only you need it" or "multiplayer: only the host needs it" in the mod's details.

## The mod list check

When a player joins, their framework sends the host the list of their `"both"` mods, and the host answers with its own. When the lists differ, a window shows the host's list and the player's list, marking each mod the other side lacks or has in another version. A long list scrolls.

The host's setting **Only players with the same mods can join** (Amber Framework settings, on by default) decides what happens then:

- On: the player is sent back to the main menu, and both see the two lists. A player who sends no list within 30 seconds, because they have no Amber Framework, is sent back too when the host has any `"both"` mod.
- Off: both see the window and play on.

A player whose host plays without Amber Framework gets a "MODS NOT CONFIRMED" window after 30 seconds.

When a player stays in a game whose host lacks some of their `"both"` mods (the setting is off, or the host has no Amber Framework), placing a building from such a mod is cancelled, and a window names the mod, its id and version. The host's save never gets a building it cannot load.

To try this alone, type `cfhostlacks <mod id>` in the UE4SS console: the game then acts as if the host lacked that mod.

The UE4SS log shows `net: mod list sent to the host`, `net: <player> joined, mods match` on the host, and `net: the host answered, mods match` on the player.

## Messages between players

A mod script can send its own text between players. A player's message goes to the host, and the host sends to every player or to one.

```lua
return function(api)
    api.net.on("score", function(text, from)
        api.log(from.name .. " sent " .. text)
        if api.net.isHost() then api.net.sendTo(from, "score", "got it") end
    end)
    api.onKey("F7", function() api.net.send("score", "42") end)
end
```

| Function | Meaning |
| --- | --- |
| `api.net.on(channel, fn)` | Calls `fn(text, from)` for messages of this mod on `channel`. `from.name` is the sender's player name, `from.host` is `true` for messages from the host. |
| `api.net.send(channel, text)` | A player sends to the host. The host sends to every other player. |
| `api.net.sendTo(from, channel, text)` | Host only: answers the player of a received message. |
| `api.net.players()` | Host only: the other players, `{name, controller}` each. |
| `api.net.isHost()` | `true` for the host and in single player. |

- `channel` is made of letters, digits, `_`, `-` and `.`, and the text is any string up to 30000 bytes, sent as is. Turn tables into text yourself.
- Messages are only delivered to the same mod on the other side, so the other player needs your mod.
- A message to yourself is not delivered. In single player you are the host and `send` reaches no one.

Messages ride on two calls the game already sends: a player's note text to the host, and the engine's console message from the host to one player. No note is changed and nothing appears on screen.

## Limits

- Dedicated servers are not supported.
- Tested on one computer as the host. The way between two computers has not been tested with two players.
{% endraw %}
