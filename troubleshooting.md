---
title: Troubleshooting
nav_order: 5
has_children: true
has_toc: false
---
{% raw %}
# Troubleshooting

Start with two checks:

- The mod manager. A red or yellow sign on a mod shows the problem. Hover over it or click the mod.
- `cfstatus` in the game console (`~`). It prints one line per mod: `applied`, `waiting`, `not ready` or `turned off` with the reason. The same lines are in `ue4ss/UE4SS.log` in the game's `Binaries/Win64` folder.

| Category | Problems |
| --- | --- |
| [Playing](trouble-playing.md) | Mods don't load, Mods screen changes do nothing, a removed mod's buildings are gone, multiplayer problems |
| [Mod manager warnings](trouble-launcher.md) | Two mods change the same thing, a required mod is missing |
| [Game data](trouble-game-data.md) | cfstatus says a row or field was not found, or says waiting |
| [Text and names](trouble-text.md) | An item has no name |
| [Models](trouble-models.md) | The model sits wrong in the hand, is invisible or grey |
| [Buildings](trouble-buildings.md) | A building is missing from the build menu |
| [Scripts](trouble-scripts.md) | A script does nothing |
| [Crashes](trouble-crashes.md) | The game crashes when a mod item appears, or at start with an old pak mod |
| [Console and logs](trouble-console.md) | The UE4SS window does not open |
{% endraw %}
