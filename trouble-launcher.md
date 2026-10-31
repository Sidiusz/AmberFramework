---
title: Mod manager warnings
parent: Troubleshooting
nav_order: 2
---
{% raw %}
# Mod manager warnings

## Two mods change the same thing

This is not an error. The mod lower in the load order wins and both stay on. The UE4SS log and `cfstatus` show which mod overrides which. Move a mod in the **Load order** window to change the winner. Authors who want their change to combine with other mods use `multiply` or `add` instead of `set`. See [Rules between mods](manifest.md#rules-between-mods).

## A required mod is missing

The red line on the mod lists what it needs after "Requires:". Install those mods. A download link may be in the mod's details. "(turned off)" means the mod is installed but off, and a version such as "2.0+" means the installed one is too old.
{% endraw %}
