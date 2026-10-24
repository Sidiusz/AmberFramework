---
title: FAQ
nav_order: 6
---
{% raw %}

# FAQ

## Players

**Q:** Are my saves safe?

**A:** Saves are never edited by the mod manager. The game saves mod items and buildings like its own. If you remove a mod, its equipped items and buildings are lost the next time the game saves, unless the mod uses `preserve` ([Removing mods](play-removing.md)). Back up your world before trying a mod you might remove.

**Q:** Does the game change on disk?

**A:** No. Mods are added when the game starts and removed when it closes. **Play Vanilla** starts the game without them. After a crash, the mod manager cleans up the next time it starts.

**Q:** What happens after a game update?

**A:** Most mods keep working, because they change single values. If a value a mod uses was renamed, that mod stops with a warning in `cfstatus` and the others keep running. Mods with their own models may need an update when the game moves to a newer Unreal Engine version.

**Q:** Can I play multiplayer with mods?

**A:** Yes, if all players have the same mods in the same versions. When someone joins, the mod lists are compared and differences are shown. Dedicated servers are not supported. See [Multiplayer](multiplayer.md).

**Q:** How do I remove a mod?

**A:** Right-click it in the mod manager and choose **Remove mod**. Read the save notes above first.

**Q:** The game does not start or crashes with mods.

**A:** See [Troubleshooting](troubleshooting.md). **Play Vanilla** always works without mods.

## Mod authors

**Q:** Do I need Unreal Engine?

**A:** Only for models, textures, icons, sounds and building classes. Changing numbers, recipes and drops needs only a text editor ([Make your first mod](tutorial-first-mod.md)).

**Q:** Can two mods change the same item?

**A:** Yes. Changes to different values both apply. If two mods set the same value, the mod lower in the load order wins. Neither is turned off ([Rules between mods](manifest.md#rules-between-mods)).

**Q:** Can I replace a game asset, like a texture or a model?

**A:** The recommended way is to add your own asset and point the game's row at it, which works alongside other mods. Replacing a game file directly is possible with `gamefiles/` ([Game files, DLL and UE4SS mods](native-mods.md)), but if two mods replace the same file only the lower one in the load order is used, and a game update can break it.

**Q:** Can I write C++ code?

**A:** C++ ships as a UE4SS DLL mod in `ue4ss/`, and players confirm code before it runs ([Game files, DLL and UE4SS mods](native-mods.md)). For Lua, see [Scripting](scripting.md).

**Q:** Where do I find row and field names?

**A:** In the [game data export](game-data.md). Models, icons and other assets: [Explore the game files](tutorial-game-files.md).

**Q:** How do I convert an old pak mod?

**A:** [Converting old mods](converting.md) turns table changes into patches once. After that the mod is a normal framework mod.

**Q:** What is the "framework" mod in the list?

**A:** Amber Framework itself. It comes with the mod manager and is always on. Mods marked "library" are shared parts other mods use. You can turn them off, and the mods that need them turn off too.
{% endraw %}
