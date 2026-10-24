---
title: Buildings
parent: Troubleshooting
nav_order: 6
---
{% raw %}
# Buildings

## A building is missing from the build menu

- The building needs its own Blueprint class, set in `PlacementData.Actor` with the `_C` suffix. See [Make a building with a script](tutorial-building.md#1-the-building-class).
- It needs a row in `BuildingRecipeTable` whose `Building` points at the building row.
- The recipe has to be unlocked: bought at the terminal, or `unlocked = true`.
- `CategoryTag` decides the tab. Look in the tab you set.
{% endraw %}
