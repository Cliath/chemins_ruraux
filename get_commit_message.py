#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Extrait le premier bloc du CHANGELOG.md et le formate comme message de commit git.

Sortie :
    Première ligne  : "Release vX.Y.Z"
    Ligne vide
    Suite           : contenu du bloc (sous-titres + bullets)

Utilisé par build.bat via : python get_commit_message.py > .commit_msg.txt
"""

import re
import sys
from pathlib import Path

CHANGELOG = Path(__file__).parent / 'CHANGELOG.md'


def extract():
    content = CHANGELOG.read_text(encoding='utf-8')

    # Découpe en sections délimitées par "# ["
    sections = re.split(r'(?=^# \[)', content, flags=re.MULTILINE)
    sections = [s.strip() for s in sections if s.strip()]

    if not sections:
        print("Release", file=sys.stdout)
        return

    first = sections[0]
    lines = first.splitlines()

    # Titre : "# [0.10.4] - 2026-03-03"
    title_match = re.match(r'^# \[(.+?)\]', lines[0])
    title = f"Release v{title_match.group(1)}" if title_match else lines[0].lstrip('# ').strip()

    # Corps : sous-titres (###) et bullets (-), on retire le Markdown lourd
    body_lines = []
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        # Convertir ### Ajouté → [Ajouté]
        heading = re.match(r'^#{2,}\s+(.*)', stripped)
        if heading:
            body_lines.append(f"\n[{heading.group(1)}]")
        elif stripped.startswith('- '):
            # Supprimer le gras **texte** → texte
            clean = re.sub(r'\*\*(.+?)\*\*', r'\1', stripped)
            body_lines.append(clean)

    if body_lines:
        print(title)
        print()
        print('\n'.join(body_lines).strip())
    else:
        print(title)


if __name__ == '__main__':
    extract()
