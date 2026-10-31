---
title: Buildings
parent: Troubleshooting
nav_order: 6
---
{% raw %}
# Buildings

## A building is missing from the build menu

- The building needs its own class: a `building` entry in `SourceArt/assets.json` and `model = "<entry name>"` on the building. See [Make a building with a script](tutorial-building.md#2-the-building-class).
- The mod log names a class it could not load. Cook and pack the mod again after changing the entry.
- It needs a row in `BuildingRecipeTable` whose `Building` points at the building row.
- The recipe has to be unlocked, for example bought at the Ranger terminal ([shop](manifest.md#shop)).
- `CategoryTag` decides the tab. Look in the tab you set.
{% endraw %}
