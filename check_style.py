"""flags long dashes, typographic symbols and stock phrasing in the docs"""
from pathlib import Path
import re
import sys

SYMBOLS = {'—': 'em dash', '–': 'en dash', '→': 'arrow', '•': 'bullet', '…': 'ellipsis',
           '“': 'curly quote', '”': 'curly quote', '‘': 'curly quote', '’': 'curly quote', '×': 'times sign'}
PHRASES = [r"\bnot (just|only|merely)\b", r"\bisn't just\b", r"\brather than\b", r",\s*but\s+(rather|instead)\b", r"\bnot \w+(?: \w+)?, but\b",
           r"\bseamless(ly)?\b", r"\brobust\b", r"\bleverag", r"\bpowerful\b", r"\bdelve", r"\bsimply\b", r"\beffortless",
           r"\belevate", r"\bcomprehensive\b", r"\bcrucial\b", r"\bvital\b", r"\bin summary\b", r"\bworth noting\b",
           r"\bnote that\b", r"\bensure[sd]?\b", r"\bunleash", r"\bharness", r"\bstreamline", r"\bembark", r"\btapestry\b",
           r"\bgame[- ]changer\b", r"\bnavigat(e|ing) the\b", r"\bkey takeaway", r"\bin today's\b", r"\bwhether you're\b"]
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')

problems = 0
for path in sorted(Path(__file__).parent.glob('*.md')):
    # lua tables like {{...}} break the jekyll build unless the page is raw
    if '{% raw %}' not in path.read_text(encoding='utf-8'):
        problems += 1
        print(f'{path.name}: missing {{% raw %}} after the front matter')
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        found = [name for char, name in SYMBOLS.items() if char in line]
        found += [p for p in PHRASES if re.search(p, line, re.IGNORECASE)]
        if EMOJI.search(line):
            found.append('emoji')
        if found:
            problems += 1
            print(f'{path.name}:{number}: {", ".join(found)}: {line.strip()[:100]}')
print(f'{problems} line(s) to fix')
sys.exit(1 if problems else 0)
