---
title: Scripts
parent: Troubleshooting
nav_order: 7
---
{% raw %}
# Scripts

## A script does nothing

- The file has to be in `content/scripts/` and return `function(api, settings)`.
- `cfstatus` and the log show `script loaded` or the error.
- `onBuilding` takes the full row name, with the mod id prefix: `SlotMachine_SlotMachine`.
- Bones only move when the model has `poseable = true`.
{% endraw %}
