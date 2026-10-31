---
title: First setup
parent: Playing with mods
nav_order: 1
---
{% raw %}

# First setup

Everything a player needs comes in one archive, `Grounded2-Mods-Player.zip`:

| In the archive | Contents |
| --- | --- |
| `Grounded 2 Mod Manager` | The mod manager, which installs mods and starts the game with them. It runs from any folder. |
| `Example mods.zip` | The example mods, if you want to try them. |

1. Close the game. Put the `Grounded 2 Mod Manager` folder anywhere and start `Grounded2ModManager.exe` in it. It finds the game by itself.
2. On its first start the mod manager adds UE4SS, the tool the framework runs on, to the game folder, and installs Amber Framework and the in-game Mods screen. A message lists what it added.
3. To try the example mods, drag `Example mods.zip` onto the mod manager window.

If the game already has UE4SS, the mod manager leaves it as it is. The framework is built for the UE4SS that comes with the mod manager. With another version, the mod manager does not install the framework and says why.

To remove everything, delete `dwmapi.dll` and the `ue4ss` folder from `Augusta\Binaries\Win64` in the game folder.

{% endraw %}
