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
- The packer stops with a message when a language file is broken JSON, uses a key `enus.json` does not have, has a name that is not a game language code (`dede.json`, not `de.json`), or when `enus.json` is missing or lacks a key a dialog uses.

## The text is English in another language

- The language file is missing or has no entry for that key. English fills the gaps.
- Text a script passes to a label or a window as a plain string is shown as written. Pass a key, `{text = "key"}`, or use `api.text(key)` ([Scripting](scripting.md#text-on-a-model)).
{% endraw %}
