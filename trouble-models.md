---
title: Models
parent: Troubleshooting
nav_order: 5
---
{% raw %}
# Models

## The model is in the wrong place in the hand

Turn on **Developer mode** in the mod manager's **Settings**, hold the item, open the pause menu and choose **Item Placement**. Move the sliders or type exact numbers until it sits right, then close the screen to save. Copy the saved values into the item entry of `SourceArt/assets.json`. The button comes with the Mods Menu mod. See [Add a weapon with your own model](tutorial-model.md#7-place-the-model-in-the-hand).

## The model is invisible or grey

- `model` in the manifest names the item entry of `SourceArt/assets.json`, and that entry's `mesh` or `skeletal` names the cooked mesh, for example `Meshes/SM_Name`.
- Grey usually means the entry has no `material` and the model shows its fallback material. A texture the material names but that is missing stops the build.
{% endraw %}
