---
title: Crashes
parent: Troubleshooting
nav_order: 8
---
{% raw %}
# Crashes

## The game crashes when a mod item appears

A static mesh cooked by the stock Unreal cook crashes this game. Cook meshes with **Cook & Pack** or `Tools/cook_assets.py`, which apply the PadSM2 patch. `Tools/cook_project_mod.py` finds the static meshes by itself. See [Models](models.md#static-meshes-and-padsm2).

## The game crashes at start with an old pak mod

Pak mods that replace whole game files are made for one game version. After an update they can crash the game. Disable the mod. [Converting old mods](converting.md) can turn a table mod into patches that survive updates.
{% endraw %}
