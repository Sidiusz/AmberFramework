---
title: Authoring setup
parent: Reference
nav_order: 0
---
{% raw %}

# Authoring setup

Mods that only change data or text need no Unreal Engine. Models, textures, icons, sounds, building classes, conversations and world variables are cooked with an Unreal Engine 5.7 project prepared for the game. This page sets one up. The project can have any name and location.

## What you need

| Tool | Used for |
| --- | --- |
| Unreal Engine 5.7 (Epic Games Launcher) | Importing and cooking assets |
| Python 3.12 | The framework tools in `Tools/` |
| Blender 4 or later | Only for the `blender` steps in `SourceArt/assets.json` that prepare models and icons |
| The framework folder | The modder kit `AmberFramework-ModderKit.zip`, unpacked anywhere: `Tools/`, `ModSource/` (all examples with their sources) and `Editor/` |

## 1. Create the project

In the Epic Games Launcher, start Unreal Engine 5.7 and create a **Blank** project without starter content. Any name works, for example `GroundedMods`. Close the editor.

## 2. Prepare it for the game

From the framework folder:

```powershell
python Tools/setup_authoring_project.py "D:\Unreal Projects\GroundedMods\GroundedMods.uproject" --save --game "D:\SteamLibrary\steamapps\common\Grounded2"
```

`--game` is the folder of your Grounded 2 install.

This:

- installs the editor plugin from `Editor/AmberFramework` into the project's `Plugins` folder.
- enables the Python Editor Script and Editor Scripting Utilities plugins.
- copies the game's render settings into the project. Assets cooked with other settings make the game reject or crash on them.
- with `--save`, writes the project path to `Tools/authoring.json`, so the other tools find it.

Run it again after a game update. It refreshes the render settings and the plugin.

## 3. Tell the tools where things are

`Tools/authoring.json`:

```json
{
  "project": "D:\\Unreal Projects\\GroundedMods\\GroundedMods.uproject",
  "engine": "C:\\Program Files\\Epic Games\\UE_5.7\\Engine",
  "blender": "C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender.exe"
}
```

The environment variables `AMBER_PROJECT`, `AMBER_ENGINE` and `AMBER_BLENDER` override the file. `cook_assets.py` and `cook_project_mod.py` also take `--project` and `--editor`, and `cook_assets.py` takes `--blender`.

The editor plugin needs none of this: it always uses the project and engine it runs in. Point it at the framework folder once in **Amber Framework > Settings**.

## 4. Buildings: the game's building class

A new building needs a Blueprint class whose parent is one of the game's building classes ([Make a building with a script](tutorial-building.md), [Add a storage chest](tutorial-storage.md)). Unreal has to know that class. The framework adds minimal copies of `Building`, `WidgetBuilding`, `StorageBuilding`, `CraftingBuilding` and `ProductionBuilding` to the project as C++ code:

```powershell
python Tools/minimal_game_stubs.py
```

This needs Visual Studio 2022 with the "Game development with C++" workload, because the project gets a C++ module, and the modules of step 5 first. Mods without buildings skip this step.

## 5. Dialogs: the game's conversation classes

Dialogs ([Add terminal dialogs](tutorial-dialogs.md), [Add character conversations](tutorial-lines.md)) are conversation assets of the game's own type. The project gets copies of the game's conversation, text and scripting modules:

```powershell
python Tools/oei_stubs.py
```

It also needs Visual Studio 2022. Mods without dialogs and without buildings skip this step.

## Check

Open the project in Unreal Editor. The main menu bar shows **Amber Framework**. **New Mod** creates a mod. **Cook & Pack Mod** builds it into `Build/Packages/<id>`.

Next: [Editor plugin](editor-plugin.md), [Add a weapon with your own model](tutorial-model.md).
{% endraw %}
