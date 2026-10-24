---
title: Text and names
parent: Troubleshooting
nav_order: 4
---
{% raw %}
# Text and names

## An item has no name

- The key in the manifest has to be in `text/enus.json`, spelled the same.
- The mod has to be packed again after a language file changes.
- The packer stops with a message when a language file is broken JSON or uses a key `enus.json` does not have.

## The text is English in another language

- The language file is missing or has no entry for that key. English fills the gaps.
- The file name must be the game's code, for example `dede.json`, not `de.json`.
- The game reads its language at start: restart it after changing the language.
{% endraw %}
