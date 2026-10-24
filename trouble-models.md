---
title: Models
parent: Troubleshooting
nav_order: 5
---
{% raw %}
# Models

## The model is in the wrong place in the hand

Turn on **Mod author tools** in the mod manager's **Settings**, hold the item, open the pause menu and choose **Item Placement**. Move the sliders or type exact numbers until it sits right, then close the screen to save. Copy the saved values into the manifest. See [Add a weapon with your own model](tutorial-model.md#6-place-the-model-in-the-hand).

## The model is invisible or grey

- The asset path in `model.mesh` or `model.skeletal` has to be the full object path, `.../SM_Name.SM_Name`.
- Grey means a texture was not found. Check the paths in `material.textures` and that the textures were cooked with the mod.
{% endraw %}
