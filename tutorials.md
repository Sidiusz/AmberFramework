---
title: Tutorials
nav_order: 3
has_children: true
has_toc: false
---
{% raw %}

# Tutorials

Each tutorial builds a working mod from an empty folder. Changes to existing game data (damage, health, loot, chest sizes, production time) are all in the first one, and the others add something new. Go in order: later tutorials build on earlier ones. Each one ends the same way: [Build and install](build.md) the mod, then check it in the game.

| Tutorial | You learn | Needs Unreal Engine |
| --- | --- | --- |
| [Make your first mod](tutorial-first-mod.md) | Looking up names, `mod.json`, patches, installing and checking in the game. Changing health, chest sizes, production time and loot | No |
| [Explore the game files](tutorial-game-files.md) | Mappings, FModel, asset paths, where things are, unpacking everything | No |
| [Add an item with a recipe](tutorial-item.md) | New items from templates, recipes, item names in several languages, a Ranger terminal entry | Yes, for the icons |
| [Add food with an effect](tutorial-food.md) | Status effects, consumables, drinks and food | No |
| [Add text and translations](tutorial-localization.md) | Item, effect and building text in the game's 11 languages | No |
| [Sell recipes at the Ranger terminal](tutorial-shop.md) | New terminal entries, adding to another mod's entry, selling buildings | No |
| [Add recipes to a station](tutorial-station.md) | Recipes at the Oven, Kiln, Jerky Rack and other stations, production time | No |
| [Add a weapon with your own model](tutorial-model.md) | Importing a model, materials, cooking, placing the model in the hand | Yes |
| [Make a building with a script](tutorial-building.md) | A building with its own class, a rigged model, a gameplay script | Yes |
| [Add a storage chest](tutorial-storage.md) | A storage building with its own model and size, and the sizes of the game's chests | Yes |
| [Add a decoration](tutorial-decor.md) | A building that only looks nice: model, glow, recipe, terminal entry | Yes |
| [Add an animated model](tutorial-animation.md) | Moving parts and a looping animation, on a decoration or a held item | Yes |
| [Add pictures for signs](tutorial-signs.md) | Your own pictures in the sign frames' Image Selector | Yes, for the textures |
| [Add marker icons and colors](tutorial-markers.md) | Your own icons and colors for Trail Markers, in the world and on the map | Yes, for the textures |
| [Place items in the world](tutorial-world.md) | Placing items on the ground once per world, finding positions | No |
| [Change the map](tutorial-level.md) | Removing map pieces and foliage, adding a level, moving pickups | For a level |
| [Add creatures](tutorial-creatures.md) | A new creature based on a game one: name, health, size, model, where it lives | For the model |
| [Add terminal dialogs](tutorial-dialogs.md) | Conversations with answers, your own speaker, terminal pictures, questions and calls from Sloane | Yes |
| [Add lines in the world](tutorial-lines.md) | Subtitles between characters, played at a place or from a script | Yes |
| [Add quests](tutorial-quests.md) | Quests in the game's list, objectives with markers, set by dialogs and scripts | Yes |
| [Publish a mod](publishing.md) | What to check, what to upload, versions and game updates | No |

Every tutorial's result is part of an example mod in `ModSource/`. When something is unclear, compare your files with the example.
{% endraw %}
