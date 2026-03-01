# Guide de démarrage rapide - Plugin QGIS Voirie Communale

## Installation en mode développement

### 1. Créer un lien symbolique

**Windows (PowerShell, sans droits admin)** :
```powershell
cmd /c mklink /J "$env:APPDATA\QGIS\QGIS3\profiles\default\python\plugins\chemins_ruraux" "D:\chemins_ruraux"
```

**Linux/macOS** :
```bash
ln -s ~/path/to/chemins_ruraux ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/chemins_ruraux
```

### 2. Compiler les ressources

**Windows** :
```powershell
cd d:\chemins_ruraux
.\compile.bat
```

**Linux/macOS** :
```bash
cd ~/path/to/chemins_ruraux
chmod +x compile.sh
./compile.sh
```

### 3. Activer dans QGIS

1. Ouvrir QGIS
2. Menu : Extensions → Installer/Gérer les extensions
3. Onglet "Installées"
4. Chercher "Voirie Communale" et cocher la case

### 4. Installer Plugin Reloader (recommandé)

Pour faciliter le développement :
1. Menu : Extensions → Installer/Gérer les extensions
2. Onglet "Toutes"
3. Chercher "Plugin Reloader"
4. Installer

Après chaque modification du code Python :
- Cliquez sur l'icône Plugin Reloader (pas besoin de redémarrer QGIS)

## Structure des fichiers

```
chemins_ruraux/
├── .github/
│   └── copilot-instructions.md    # Instructions pour les agents IA
├── metadata.txt                    # Métadonnées du plugin (version, auteur, etc.)
├── __init__.py                     # Point d'entrée QGIS
├── chemins_ruraux.py              # Classe principale du plugin
├── chemins_ruraux_dialog.py       # Logique du dialogue
├── chemins_ruraux_dialog_base.ui  # Interface Qt Designer (XML)
├── resources.qrc                   # Liste des ressources (icônes)
├── resources.py                    # Ressources compilées (généré)
├── icon.png                        # Icône du plugin
├── compile.bat                     # Script de compilation Windows
├── compile.sh                      # Script de compilation Linux/macOS
├── .gitignore                      # Fichiers à ignorer par Git
└── README.md                       # Documentation
```

## Workflow de développement

### Modifier l'interface utilisateur

1. **Éditer** : Ouvrir `chemins_ruraux_dialog_base.ui` avec Qt Designer (ou éditeur XML)
2. **Compiler** : Exécuter `compile.bat` (Windows) ou `compile.sh` (Linux/macOS)
3. **Tester** : Recharger le plugin avec Plugin Reloader dans QGIS

### Modifier le code Python

1. **Éditer** : Modifier les fichiers `.py` (pas besoin de compiler)
2. **Tester** : Recharger le plugin avec Plugin Reloader dans QGIS

### Ajouter une icône/ressource

1. **Éditer** : Ajouter le fichier dans `resources.qrc`
2. **Compiler** : Exécuter `compile.bat` ou `compile.sh`
3. **Référencer** : Utiliser `:/plugins/chemins_ruraux/votre_fichier.png` dans le code

## Débogage

### Console Python QGIS

Ouvrir avec `Ctrl+Alt+P` (Windows/Linux) ou `Cmd+Alt+P` (macOS) :

```python
# Tester l'import du plugin
from chemins_ruraux import CheminsRuraux

# Accéder à l'interface QGIS
iface

# Lister les couches
QgsProject.instance().mapLayers()
```

### Logs

Ajouter dans le code :

```python
from qgis.core import QgsMessageLog, Qgis

QgsMessageLog.logMessage("Mon message de debug", "CheminsRuraux", Qgis.Info)
QgsMessageLog.logMessage("Erreur!", "CheminsRuraux", Qgis.Critical)
```

Voir les logs : Menu → Voir → Panneaux → Journal des messages

## Commandes utiles

```powershell
# Vérifier la version de QGIS
qgis --version

# Tester l'import Python (depuis le dossier du plugin)
python -c "from chemins_ruraux import CheminsRuraux; print('OK')"

# Lister les plugins installés
dir "$env:APPDATA\QGIS\QGIS3\profiles\default\python\plugins"
```

## Ressources

- [Documentation API QGIS](https://qgis.org/pyqgis/master/)
- [PyQGIS Cookbook](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/)
- [Qt Designer Manual](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- [Plugin Builder](http://g-sherman.github.io/Qgis-Plugin-Builder/)
