---
title: Build and install
parent: Reference
nav_order: 1.5
---
{% raw %}

# Build and install

Every tutorial ends with this step. It turns the mod folder into what players install.

## Mods without assets

A mod with only `mod.json`, `content/` and `text/` needs no Unreal Engine. Two ways:

- Drag the mod folder onto the mod manager window. To share it, zip the folder. This works only without `text/`: the game reads a mod's texts from its pak.
- Build a pak, from the modder kit folder:

```powershell
python Tools/pack_mod.py ModSource/MyMod -o Build/Packages/MyMod
```

The packer checks `mod.json`, builds one text table per language from `text/`, and writes `MyMod_P.pak` to the output folder (with `.ucas` and `.utoc` when there are texts).

## Mods with assets

Models, textures, icons, sounds, Blueprint classes, levels, dialogs and world variables are cooked with Unreal Engine 5.7 first ([Authoring setup](authoring.md)).

In Unreal Editor: **Amber Framework > Cook & Pack Mod**. It saves changed assets, cooks the mod in the background and packs it into `Build/Packages/<id>`.

From a console, without opening the editor:

```powershell
python Tools/cook_assets.py ModSource/MyMod
python Tools/pack_mod.py ModSource/MyMod -o Build/Packages/MyMod
```

`cook_assets.py` imports the files listed in `SourceArt/assets.json`, runs its Blender and editor steps, and cooks everything into `ModSource/MyMod/Cooked`. For a mod made in the editor, without `assets.json`, use `python Tools/cook_project_mod.py MyMod` instead. Along the way it:

- builds the conversation set from `dialogs/*.json` ([Add terminal dialogs](tutorial-dialogs.md)).
- builds the world variables from `variables.json` ([World variables](scripting.md#world-variables)).
- patches the `staticmesh` entries with PadSM2, which the game needs to load them ([Models](models.md)). `cook_project_mod.py` finds and patches the static meshes of an editor-made mod.

`pack_mod.py` then adds the cooked files and writes `MyMod_P.pak`, `.ucas` and `.utoc`. Cook again after changing an asset. Packing alone is enough after changing only `content/`, `text/` or `mod.json`.

## Install and play

1. Install `Build/Packages/MyMod` with the mod manager: drag the folder onto its window.
2. Press **Play Modded**.
3. In the main menu, the version text ends with "Modded: Amber Framework, ... mods". `cfstatus` in the game console lists each mod as `applied`, `waiting`, `not ready: <table>.<row>` or `turned off` with the reason.

If something is missing, see [Troubleshooting](troubleshooting.md).
{% endraw %}
