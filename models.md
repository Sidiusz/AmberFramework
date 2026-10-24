---
title: Models
parent: Reference
nav_order: 3
---
{% raw %}

# Models

An item or a building can show its own 3D model in place of the template's. The model is set with `model = {...}` on an entry in `items` or `buildings` ([Manifest reference](manifest.md)). Tutorials: [Add a weapon with your own model](tutorial-model.md), [Make a building with a script](tutorial-building.md).

```lua
model = {
    mesh = "/Game/Mods/MyMod/Meshes/SM_Gun.SM_Gun",
    material = {
        base = "/Game/_Augusta/Art/Items/Weapons/Gun_Paintball/Textures/MI_Weapon_Gun_Paintball_Equip.MI_Weapon_Gun_Paintball_Equip",
        textures = {Albedo = "/Game/Mods/MyMod/Textures/T_Gun_C.T_Gun_C"},
        vectors = {["Emissive Color"] = {6, 1.5, 1, 1}},
    },
    equipped = {location = {0, 0, 0}, rotation = {0, 0, 0}, scale = 1},
    preview = {size = 26},
}
```

## Mesh

Exactly one of these is used. If several are given, `geometry` wins over `skeletal`, `skeletal` over `mesh`.

| Key | Meaning |
| --- | --- |
| `mesh` | Static mesh object path. Cooked static meshes need the PadSM2 patch, see [below](#static-meshes-and-padsm2). |
| `skeletal` | Skeletal mesh object path. |
| `animation` | Animation object path, only with `skeletal`. Plays in a loop, also in the preview. |
| `poseable` | `true`: scripts move the bones ([Scripting](scripting.md#buildings)). Cannot be combined with `animation`. |
| `geometry` | A `.cfmesh` file in `content/data`, drawn without cooking. No preview in menus. |

## Material

The model gets an instance of a game material with the mod's textures, so no shaders are shipped.

| Key | Meaning |
| --- | --- |
| `base` | Object path of a game material. The paintball gun material in the example suits most hand-held items. |
| `textures` | `{Parameter = texture path}`. The paintball material uses `Albedo`, `Normal`, `RMA` (roughness, metallic, ambient occlusion), `Emissive Texture`, `FresnelMask` and `SSSMask`. |
| `vectors` | `{Parameter = {r, g, b}}` or `{r, g, b, a}`. `Emissive Color` above 1 makes the glow brighter. |

Parameter names come from the material. Open it in FModel to see them ([Explore the game files](tutorial-game-files.md)). Scalar parameters are not supported.

## Where the model appears

| Role | Key | Used for | Default component |
| --- | --- | --- | --- |
| In the hand | `equipped` | The item's equipped actor | `SkeletalMesh` |
| On the ground | `world` | The item's world actor | `StaticMesh` |
| Placed building | `building` | The class in `PlacementData.Actor` | `StaticMeshComponent` |

Each role takes a table or `false`. `false` keeps the template's look for that role, for example `equipped = false` for a crafting material.

Behaviour per role:

- In the hand, the model is attached to the base weapon's component and that component is hidden.
- On the ground, a static mesh replaces the world mesh. A skeletal model is attached to the invisible physics mesh.
- A building gets the model attached. A skeletal building model also gets an invisible blocking box from its bounds. `building = {collision = false}` turns it off.
- The crafting window and the build menu show the mod's model.

### Placement keys

| Key | Default | Meaning |
| --- | --- | --- |
| `location` | `{0, 0, 0}` | Offset in cm: forward, right, up. |
| `rotation` | `{0, 0, 0}` | Pitch, yaw, roll in degrees. |
| `scale` | `1` | A number or `{x, y, z}`, must be positive. |
| `component` | see table | Component of the actor to attach to. Without it, the framework tries `SkeletalMesh`, `StaticMesh` and `Mesh`. |
| `socket` | none | Socket on that component. |
| `hide` | the component | List of component names to hide, for example `{"SkeletalMesh", "ArrowMesh"}`. `{}` hides nothing. |
| `collision` | `true` | Buildings only, see above. |

```lua
equipped = {location = {0, 0, 0}, rotation = {0, 0, 0}, scale = 1},
```

The game holds an item on the same hand socket in first and third person, so one placement fits both views.

## Preview size

`preview = {size = 26}` sets the size of a skeletal model in the crafting window and the build menu. Defaults: 26 for items, 120 for buildings. Static meshes are fitted automatically.

## Item Placement

![Item Placement](assets/images/item-placement.jpg)

Item Placement is a tool for mod authors. Turn on **Mod author tools** in the mod manager's **Settings**, hold the mod item in the game, open the pause menu and choose **Item Placement**. The button appears only while you hold an item with a mod model.

| Row | Changes |
| --- | --- |
| First-person camera | Switches the camera to check the item in both views. Both views use the same values. |
| Position X, Y, Z | Forward, right and up, in cm |
| Pitch, Yaw, Roll | Rotation in degrees |
| Scale | Size of the model |

Drag a slider or type an exact number next to it, and the model moves right away. Closing the screen saves the values. They apply on your PC from then on (`%LOCALAPPDATA%\G2Launcher\Tuning\tuning.txt`). Next to that file, `<row>.lua.txt` has the same values as an `equipped = {...}` block. Copy it into the manifest so other players get them.

## Static meshes and PadSM2

The game's engine expects an extra value in each static mesh section that the stock Unreal 5.7 cook does not write. Such meshes crash the game. **Cook & Pack** in the [editor plugin](editor-plugin.md) and `Tools/cook_assets.py` cook static meshes unversioned and patch them with [PadSM2](https://github.com/hypermodule/PadSM2) automatically. Skeletal meshes, animations, textures and sounds need no patch.

## Text on models

Scripts can put text on a model with `building.label`, in the game's fonts. See [Scripting](scripting.md#text-on-a-model).
{% endraw %}
