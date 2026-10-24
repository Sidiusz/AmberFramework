---
title: Add text and translations
parent: Tutorials
nav_order: 5
---
{% raw %}

# Add text and translations

<p class="download-stub">Download the finished tutorial project: EnergySoda.zip</p>

Every text a mod shows (item names, descriptions, effect names, terminal entries, creature names) comes from the mod's language files. The game shows the language the player picked in its settings. The example `ModSource/EnergySoda` has its texts in all 11 languages.

![The same pickup message in English and German](assets/images/compare/localization.jpg)

No Unreal Engine is needed: the packer turns the language files into the game's text tables.

## 1. Language files

One file per language in the mod's `text` folder, named by the game's language code. Each file maps a key you choose to the text:

```text
EnergySoda/
  text/
    enus.json
    dede.json
    frfr.json
```

`text/enus.json`:

```json
{
  "soda.name": "Energy Soda",
  "soda.description": "Move speed +30% for 3 minutes.",
  "rush.name": "Sugar Rush"
}
```

`text/dede.json`:

```json
{
  "soda.name": "Energiebrause",
  "soda.description": "Laufgeschwindigkeit +30 % für 3 Minuten.",
  "rush.name": "Zuckerschub"
}
```

- `enus.json` is required. Every other language is optional, and a missing file or key shows the English text.
- Language codes: `enus`, `dede`, `eses`, `esmx`, `frfr`, `itit`, `jajp`, `kokr`, `ptbr`, `zhch`, `zhtw`.
- The files are UTF-8, so accents and Japanese, Korean or Chinese characters work as they are.
- A key in another language that `enus.json` does not have is an error, so a typo does not go unnoticed.

## 2. Using the keys

The manifest uses the keys:

```lua
items = {
    {name = "Soda", template = "SmoothieAttack", displayName = "soda.name", description = "soda.description"},
},
shop = {
    {name = "Arsenal", cost = 500, title = "arsenal.title", description = "arsenal.description", recipes = {"Ingot"}},
},
creatures = {
    {name = "Aphid", template = "Aphid", displayName = "aphid.name"},
},
```

A text field of a table row takes `{text = "key"}`:

```lua
rows = {
    {table = "/Game/Blueprints/Attacks/Table_StatusEffects.Table_StatusEffects", template = "MealTier3MoveSpeed", name = "Rush", fields = {
        ["DisplayData.Name"] = {text = "rush.name"},
    }},
},
```

A number instead of a key uses a text the game already has, for example the name of a vanilla item.

## How keys become text

Every key gets a number from the mod's id and the key, the same on every PC. Two mods can use the same key without clashing, because their ids differ. Changing the mod's id changes the numbers, so keep the id once the mod is published.

## Check

[Build and install](build.md) the mod. The packer builds one text table per language. Pick another language in the game's settings and restart the game. Craft or pick up the item: its name appears in that language, as in the picture above.

If the text stays English or empty, see [Text problems](trouble-text.md).
{% endraw %}
