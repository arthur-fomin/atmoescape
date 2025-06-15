#!.venv/bin/python
from sh import Command
from pathlib import Path
import json
import os

def настройка_экстеншнов():
    нужные_расширения = '''
alefragnani.bookmarks
anthonyattard.zoomer
bierner.markdown-mermaid
danlevett.regex-robin
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
oderwat.indent-rainbow
telesoho.vscode-markdown-paste-image
johnpapa.vscode-peacock
bierner.markdown-image-size
hediet.vscode-drawio
    '''.strip().split('\n')

    cmd = Command('code-server')
    for рас in нужные_расширения:
        os.system(f'code-server --install-extension {рас}')


def настройки_vscode(путь_к_профилю='.vscode'):
    профиль_кат = Path(путь_к_профилю) 
    профиль_кат.mkdir(exist_ok=1, parents=1)
    настройки_путь = профиль_кат / "settings.json"
    настройки_путь.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        настр = json.loads(настройки_путь.read_text()) if настройки_путь.exists() else {}
    except json.JSONDecodeError:
        настр = {}
    
    настр["editor.minimap.enabled"] = False
    настр["editor.unicodeHighlight.ambiguousCharacters"] = False
    настр["editor.fontFamily"] = "Consolas,monospace"
    настр["editor.fontFamily"] = "Consolas,monospace"
    настр["security.workspace.trust.untrustedFiles"] = "open"
    настр["editor.mouseWheelZoom"] = True
    настройки_путь.write_text(json.dumps(настр, indent=4))

    
#настройка_экстеншнов()
настройки_vscode()
