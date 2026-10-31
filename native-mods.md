---
title: Game files, DLL and UE4SS mods
parent: Reference
nav_order: 6
---
{% raw %}

# Game files, DLL and UE4SS mods

Mods can change any file of the game and can ship their own code. To protect the PC, nothing is written outside the game folder, and every change is undone after the session.

## Parts of a mod

Pak files (`.pak`, `.ucas`, `.utoc`) in the mod folder hold the content. All mods are mounted from one folder of the mod manager, `Augusta/Content/Paks/_G2LauncherMods`.

`ue4ss/<ModName>/...` holds UE4SS mods with Lua scripts or C++ DLLs. They stay out of the game folder. The mod manager collects them into the session folder and adds one line, `+ModsFolderPaths = <session folder>/UE4SS`, to `UE4SS-settings.ini` for the session. An `enabled.txt` is created if the mod has none.

`gamefiles/` mirrors the game folder and is for any other file (ini files and so on). The files are put in place for the session. Replaced files are backed up in a journal. When the game closes, or on the next mod manager start after a crash, the originals come back and added files are removed.

When two mods replace the same game file, or ship a UE4SS mod with the same name, the later mod in load order wins.

`pack_mod.py` copies `gamefiles/` and `ue4ss/` next to the pak files.

## A ready-made mod as it is

A mod made without Amber works without changes:

1. Put its pak files (`.pak`, `.ucas`, `.utoc`) in a folder named after the mod, unchanged.
2. Put its DLL or other game files in `gamefiles/`, at the same path they have in the game folder, for example `gamefiles/Augusta/Binaries/Win64/MyMod.dll`. A UE4SS mod goes in `ue4ss/<ModName>/`.
3. Install the folder or a zip of it in the mod manager.

Name, version, picture and icon are optional. The mod manager reads `mod.json`, `preview.png`, `icon.png` and `settings.schema.json` from inside the pak, or from the folder next to it. Without them the mod is named after its folder.

UE4SS is loaded through `Augusta/Binaries/Win64/dwmapi.dll`. A DLL of the same name replaces it, so a mod's own loader DLL needs another name.

Leave out of the folder what the mod manager already provides:

- UE4SS itself (`dwmapi.dll`, `ue4ss/UE4SS.dll` and its settings). Players get it from the mod manager.
- An updater that writes into the game's `Content\Paks`. The mod manager adds a mod's paks only while the game runs and removes them afterwards, so such an updater would find nothing to update or would leave its own copy behind. For updates, put a Nexus Mods or GitHub link in `mod.json`. The mod manager checks it and shows when a newer version is out.

A translation made of paks, with its text bundles, textures and fonts, works this way unchanged: a folder with its three pak files is enough.

## Load order of pak files

Unreal ranks pak containers by their name. A name ending in `_<N>_P` with N of 1 or more ranks above one ending in plain `_P`. The game's own container is `Augusta-Windows_0_P`. A mod container named `MyMod_P` would rank the same as the game and could not replace any game asset.

The mod manager therefore mounts each container as `<name>_<100 + position>_P`. Every mod ranks above the game, and a mod later in the load order ranks above an earlier one. Mod authors do not need to name their files in any special way.
{% endraw %}
