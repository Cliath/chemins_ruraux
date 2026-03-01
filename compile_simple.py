#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de compilation pour le plugin QGIS Voirie Communale
Compile les fichiers .ui et .qrc sans dépendre de pyrcc5/pyuic5
"""

import sys
import os

try:
    from PyQt5 import uic
    from PyQt5.pyrcc_main import processResourceFile
except ImportError:
    print("Erreur: PyQt5 n'est pas installé")
    print("Installation: pip install PyQt5")
    sys.exit(1)

def compile_resources():
    """Compile resources.qrc -> resources.py"""
    print("Compilation de resources.qrc...")
    try:
        processResourceFile(['resources.qrc'], 'resources.py', False)
        print("✓ resources.py créé")
        return True
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False

def compile_ui():
    """Compile chemins_ruraux_dialog_base.ui -> chemins_ruraux_dialog_base.py"""
    print("\nCompilation de chemins_ruraux_dialog_base.ui...")
    try:
        with open('chemins_ruraux_dialog_base.ui', 'r', encoding='utf-8') as ui_file:
            with open('chemins_ruraux_dialog_base.py', 'w', encoding='utf-8') as py_file:
                uic.compileUi(ui_file, py_file)
        print("✓ chemins_ruraux_dialog_base.py créé")
        return True
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False

if __name__ == '__main__':
    print("=== Compilation du plugin Voirie Communale ===\n")
    
    # Changer vers le répertoire du script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    success = True
    success = compile_resources() and success
    success = compile_ui() and success
    
    if success:
        print("\n✓ Compilation terminée avec succès!")
        sys.exit(0)
    else:
        print("\n✗ Erreurs lors de la compilation")
        sys.exit(1)
