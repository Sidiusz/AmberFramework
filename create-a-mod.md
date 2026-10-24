---
title: Mod folder and mod.json
parent: Reference
nav_order: 1
---
{% raw %}

# Mod folder and mod.json

## Folder layout

```text
MyMod/
  mod.json               required
  content/main.lua       the manifest: what the mod adds and changes
  content/scripts/*.lua  optional gameplay scripts
  content/data/          optional data files read by the manifest
  text/<language>.json   optional texts, one file per language
  settings.schema.json   optional settings
  preview.png            optional picture for the mod manager
  icon.png               optional square icon for the mod list
  SourceArt/assets.json  optional source files to cook (models, textures, sounds, Blueprints)
  Cooked/Augusta/...     cooked assets, written by the cook tools
  gamefiles/             optional files placed into the game folder
  ue4ss/                 optional UE4SS mods (Lua or DLL)
```

The [editor plugin](editor-plugin.md) creates this layout with **New Mod**. Without Unreal Engine, copy `ModSource/Templates/MyMod` from the modder kit: it has `mod.json`, a manifest, a script and a language file, with commented examples. The manifest is described in the [Manifest reference](manifest.md), `gamefiles/` and `ue4ss/` in [Game files, DLL and UE4SS mods](native-mods.md).

## mod.json

```json
{
  "id": "MyMod",
  "name": "My Mod",
  "version": "1.0.0",
  "apiVersion": 2,
  "engineVersion": "UE5_7",
  "author": "Me",
  "description": "Adds a dagger with a fire combo.",
  "category": "Weapons",
  "tags": ["weapon"]
}
```

| Field | Default | Meaning |
| --- | --- | --- |
| `id` | folder name | Starts with a letter and has only letters, digits, `_` and `-`, at most 64 characters. Unique among installed mods. |
| `name` | id | Shown in the mod manager and the Mods screen. |
| `version` | | Compared part by part: `1.10.0` is newer than `1.9.2`. |
| `author`, `description` | | Shown in the mod manager and the Mods screen. Keep the description short and factual. |
| `category`, `tags` | | Shown in the mod manager. |
| `apiVersion` | 2 | Must be 2. |
| `engineVersion` | | `UE5_7`. Required when the mod has cooked assets. |
| `dependencies` | | See below. |
| `loadAfter` | | Mod ids that should load earlier when installed, without requiring them. |
| `preserve` | `false` | `true` keeps placed buildings of this mod while it is removed (see [Removing mods](play-removing.md)). |
| `multiplayer` | `"both"` | Who needs the mod in multiplayer: `"both"` (the host and every player), `"client"` (only whoever installs it, such as a minimap or a skin) or `"host"`. Only `"both"` mods are compared when a player joins. See [Multiplayer](multiplayer.md#who-needs-a-mod). |
| `gameVersions` | | Game versions the mod was made for, `*` allowed: `["0.6.*"]`. The version is the one in the game's main menu, such as `0.6.0.3`. On another game version the mod manager shows a yellow sign on the mod, but it still loads. |
| `isLibrary` | `false` | Marks a mod other mods build on. The mod manager shows it as a library. Players can turn it off like any mod, and the mods that need it are turned off with it. Only Amber Framework itself is built in and always on. |
| `links` | | Web pages of the mod, see [Links](#links). |

`preview.png` (or `.jpg`) next to `mod.json` is the cover in the mod's details, up to 8192 x 8192 pixels. 960 x 540 works well. `icon.png` (or `.jpg`) is the small square in the mod list. 256 x 256 works well. Without an icon, the list shows the middle of the cover.

### Dependencies

```json
"dependencies": [
  { "id": "SteelGear", "name": "Steel Gear", "minVersion": "1.0.0", "url": "https://www.nexusmods.com/grounded2/mods/123" },
  { "id": "GameTweaks", "optional": true }
]
```

| Key | Meaning |
| --- | --- |
| `id` | The other mod's id. |
| `name` | Shown in warnings. |
| `url` | Download page. Shown in the mod's details when the dependency is missing. |
| `minVersion` | Lowest accepted version. Also checked for optional dependencies. |
| `optional` | `true`: the mod also works without it, but loads after it when it is there. |

Amber Framework is not listed: every mod with content for it (`content/`, `dialogs/`, `text/`, `variables.json`) depends on it, with the version its `apiVersion` needs.

A missing, turned off or too old required dependency shows a red sign on the mod, for example "Requires: Steel Gear 1.0.0+", and the game does not start until it is fixed.

## Links

`links` groups web pages by kind. Each kind holds one or more links:

```json
"links": {
  "modPage": [
    "https://www.nexusmods.com/grounded2/mods/123",
    {"name": "Playground", "url": "https://example.com/mods/my-mod"}
  ],
  "source": ["https://github.com/me/my-mod"]
}
```

| Kind | Shown as |
| --- | --- |
| `modPage` | Mod page |
| `source` | Source code |
| `issues` | Bug reports |
| `community` | Community |
| `support` | Support the author |

A link is a URL or `{"name": ..., "url": ...}`. Without a name the mod manager shows the site: Nexus Mods, GitHub, Discord and so on. Only `http` and `https` links are accepted, and other kinds are ignored. In the [editor plugin](editor-plugin.md), **Mod Info** has a field per kind with one link per line, written as `https://...` or `Name https://...`.

## Settings

`settings.schema.json` declares options. The mod manager and the [Mods screen](play-in-game.md) show them, and the manifest and scripts receive the values.

```json
{
  "settings": [
    { "key": "damageMultiplier", "label": "Rifle damage", "type": "float",
      "default": 1.0, "min": 0.1, "max": 5.0, "step": 0.1,
      "description": "Scales the rifle's damage." },
    { "key": "tracers", "label": "Tracers", "type": "bool", "default": true, "live": true },
    { "key": "color", "label": "Color", "type": "choice", "choices": ["red", "blue"], "default": "red" }
  ]
}
```

| Field | Default | Meaning |
| --- | --- | --- |
| `key` | required | Name in the `settings` table. |
| `label` | key | Shown next to the control. |
| `description` | | Shown under the control in the mod manager. |
| `type` | `bool` | `bool`, `int`, `float`, `string` or `choice`. |
| `default` | per type | `false`, 0, `""` or the first choice. |
| `min`, `max` | none | Range of a number. |
| `step` | 1/20 of the range | Slider step in the Mods screen. |
| `choices` | | Values of a `choice`. |
| `live` | `false` | `true`: changes apply in the game right away and reach scripts through `api.onSettings`. Otherwise they apply after a restart. |

Values are stored in the mod folder as `settings.json`. A value outside the schema can't be saved and stops the game from starting. When a mod updates, values the new schema still accepts are kept. `string` settings can only be edited in the mod manager.

A manifest that uses settings returns a function. See [Manifest reference](manifest.md#shape-of-a-manifest).

## Assets

Models, textures, icons and sounds are cooked with an Unreal Engine 5.7 project prepared for the game ([Authoring setup](authoring.md)). Text needs no Unreal Engine (see [Text](#text)).

Two ways:

1. Work in the editor: put assets in `/Game/Mods/<id>` and use **Cook & Pack** from the [editor plugin](editor-plugin.md).
2. Work from source files: describe them in `SourceArt/assets.json` and run `python Tools/cook_assets.py ModSource/<id>`. This imports, cooks and patches them in the background. The editor window stays closed.

Both write `Cooked/` in the mod folder. Static meshes get the PadSM2 patch automatically.

## SourceArt/assets.json

```json
{
  "destination": "/Game/Mods/MyMod",
  "assets": [
    {"type": "staticmesh", "source": "ModSource/MyMod/SourceArt/SM_Blade.fbx", "folder": "Meshes", "name": "SM_Blade",
     "fallbackMaterial": "/Engine/BasicShapes/BasicShapeMaterial.BasicShapeMaterial", "lodGroup": "SmallProp"},
    {"type": "texture", "kind": "color", "source": "ModSource/MyMod/SourceArt/T_Blade_C.png", "folder": "Textures", "name": "T_Blade_C"}
  ]
}
```

| Key | Meaning |
| --- | --- |
| `destination` | Folder under `/Game/Mods/` the assets go to. |
| `assets` | List of entries, below. |
| `blender` | Optional steps run in Blender without a window before the import: `{"script": "...", "spec": "..."}`. The script gets the spec path after `--`. A script path is looked up in the mod folder first, then in the framework folder. The scripts the examples use are in `Tools/ExampleArt`, and your own script works the same way. |
| `editor` | Optional Python scripts run in the editor without a window after the import: `{"script": "...", "spec": "..."}`. The script sees `MOD_DIR`, `DESTINATION` and `SPEC`. The map example builds its level this way. |

Every entry has `type`, and all but `gameMesh` have `folder` (inside the destination) and `name` (the asset name). `source` paths are relative to the framework folder, and the file name must equal `name`.

| type | Extra keys | Result |
| --- | --- | --- |
| `staticmesh` | `source` (FBX), `fallbackMaterial` (required), `lodGroup` (for example `SmallProp`, builds smaller LODs), `collision` (`auto` or `none`) | Static mesh |
| `skeletalmesh` | `source` (FBX with a skeleton), `fallbackMaterial` (required), `animation` (name for the imported animation) | Skeletal mesh. List `<name>_Skeleton` as a `generated` entry |
| `texture` | `source` (PNG), `kind`: `color`, `mask` (linear, for roughness and metallic), `normal` or `icon` | Texture |
| `sound` | `source` (WAV), `falloffDistance` (default 4000), `volume` (default 1) | Sound. List `ATT_<name>` as a `generated` entry |
| `blueprint` | `parent`, for example `/Script/Maine.Building`, and for a game Blueprint parent also `nativeParent` | Empty Blueprint class |
| `generated` | | An asset another entry creates. It is only checked and packed |
| `level` | | A level you made in the editor or an `editor` step made. It is cooked and packed |
| `gameMesh` | `path` (a game mesh path, outside `/Game/Mods`), optional `source` (FBX) | A stand-in at the game's path for placing in levels. It is never packed |

### blueprint

`parent` is a class of the game. A C++ class (`/Script/Maine.StorageBuilding`) works directly. A game Blueprint is given by its class path, together with the C++ class it is built on:

```json
{"type": "blueprint", "folder": "Blueprints", "name": "BP_TreasureChest",
 "parent": "/Game/Blueprints/Items/BaseBlueprints/BP_BaseItemStorageBuilding.BP_BaseItemStorageBuilding_C",
 "nativeParent": "/Script/Maine.StorageBuilding"}
```

The cook tool then puts an empty stand-in for the game Blueprint into the authoring project at the same path. Only `/Game/Mods/` is packed, so in the game the class inherits from the real Blueprint, with its components and behavior. Base Blueprints of the game are in `/Game/Blueprints/Items/BaseBlueprints/`: `BP_BaseItemStorageBuilding`, `BP_BaseCraftingBuilding`, `BP_BaseItemProcessingBuilding`, `BP_WidgetBuilding`.

## Text

Texts are not cooked. Each language has a file `text/<language>.json` that maps keys to texts, and the manifest uses the keys. The packer builds the game's text tables from the files. See [Add text and translations](tutorial-localization.md).

## Packing

```powershell
python Tools/pack_mod.py ModSource/MyMod -o Build/Packages/MyMod
```

The result is a folder the mod manager installs: a `.pak` (plus `.ucas` and `.utoc` when the mod has cooked assets), and `gamefiles/` and `ue4ss/` if the mod has them. Zip that folder to share the mod. See [Publish a mod](publishing.md).

## Checking a mod

The mod manager runs the framework's patch engine over all mods that are on, without starting the game, and marks problems on the mods. In the game, the console commands `cfstatus` (state of each mod), `cfinspect AllItemsTable SpearTier3` (fields of a row) and `cfwhere` (the player's position) help. See [Troubleshooting](troubleshooting.md).
{% endraw %}
