# Voirie Communale - Plugin QGIS

Plugin QGIS pour le recensement de la voirie communale (voies communales et chemins ruraux).

## Installation

### Installation depuis un ZIP (recommandé)

1. Téléchargez la dernière version depuis [GitHub Releases](https://github.com/Cliath/chemins_ruraux/releases)
2. Ouvrez QGIS
3. Menu **Extensions** → **Installer/Gérer les extensions**
4. Onglet **Installer depuis un ZIP**
5. Sélectionnez le fichier `chemins_ruraux-X.X.X.zip` téléchargé
6. Cliquez sur **Installer l'extension**
7. Activez le plugin dans l'onglet **Installées**

### Installation en mode développement

1. Clonez ce dépôt dans le répertoire des plugins QGIS :
   - Windows : `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - Linux : `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - macOS : `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`

2. Compilez les ressources et fichiers UI :
   ```bash
   # Windows
   compile.bat
   
   # Linux/macOS
   chmod +x compile.sh
   ./compile.sh
   ```

3. Redémarrez QGIS et activez le plugin dans le gestionnaire d'extensions

## Structure du projet

```
chemins_ruraux/
├── .github/
│   └── copilot-instructions.md    # Instructions pour les agents IA
├── metadata.txt                    # Métadonnées du plugin
├── version.py                      # Gestion des versions
├── CHANGELOG.md                    # Historique des modifications
├── __init__.py                     # Point d'entrée du plugin
├── chemins_ruraux.py              # Classe principale du plugin
├── chemins_ruraux_dialog.py       # Classe de dialogue
├── chemins_ruraux_dialog_base.ui  # Interface utilisateur (Qt Designer)
├── resources.qrc                   # Ressources Qt (icônes, etc.)
├── resources.py                    # Ressources compilées
├── icon.png                        # Icône du plugin
├── compile.sh                      # Script de compilation (Linux/macOS)
├── compile.bat                     # Script de compilation (Windows)
├── compile_plugin.py               # Script de compilation Python
├── package.py                      # Script de packaging (création du ZIP)
├── build.sh                        # Script complet (compile + package)
├── build.bat                       # Script complet Windows
└── releases/                       # Packages ZIP des versions
    ├── README.md
    ├── chemins_ruraux-0.1.0.zip
    ├── chemins_ruraux-0.1.1.zip
    ├── chemins_ruraux-0.1.2.zip
    ├── chemins_ruraux-0.2.0.zip
    └── chemins_ruraux-0.2.1.zip
```

## Développement

### Prérequis

- QGIS 3.0 ou supérieur
- Python 3.6+
- PyQt5
- pyrcc5 et pyuic5 pour compiler les ressources

### Workflow de développement

1. **Modifier l'interface** : Éditez `chemins_ruraux_dialog_base.ui` avec Qt Designer
2. **Compiler** : Exécutez `compile.bat` ou `compile.sh`
3. **Tester** : Rechargez le plugin dans QGIS (Plugin Reloader recommandé)
4. **Déboguer** : Utilisez la console Python de QGIS ou un débogueur externe

### API QGIS utilisée

- `QgsInterface` : Interface principale de QGIS
- `QgsMapLayerComboBox` : Sélection de couches vectorielles
- `QgsVectorLayer` : Manipulation de couches vectorielles
- `QgsProject` : Accès au projet QGIS actuel

## Fonctionnalités

### Actuellement implémentées

- ✅ **Chargement automatique du flux WMS du Cadastre** : Intégration complète des données cadastrales françaises
  - 10 couches chargées automatiquement :
    - Parcelles cadastrales
    - Bâtiments
    - Subdivisions fiscales
    - Lieux-dits
    - Amorces cadastrales
    - Clôtures
    - Détails topographiques
    - Hydrographie
    - Voies de communication
    - Bornes et repères
  - Organisation automatique dans un groupe "Cadastre - {code INSEE}"
- ✅ **Sélection de couches** : Interface pour choisir la couche de chemins à analyser

### À développer

- [ ] Import de données de chemins ruraux depuis fichiers (Shapefile, GeoPackage, etc.)
- [ ] Analyse de connectivité des chemins
- [ ] Calcul automatique de longueurs et surfaces
- [ ] Export de rapports PDF/Excel
- [ ] Croisement avec les données cadastrales
- [ ] Détection de chemins non entretenus

## Utilisation

### Charger les données cadastrales

1. Ouvrez le plugin via le menu **Extensions → Voirie Communale** ou l'icône dans la barre d'outils
2. Dans la section **Cadastre**, saisissez le **code INSEE** de votre commune (5 chiffres)
   - Exemples : 75056 pour Paris, 13055 pour Marseille, 69123 pour Lyon
   - Vous pouvez trouver le code INSEE sur [le site de l'INSEE](https://www.insee.fr/fr/recherche/recherche-geographique)
3. Cliquez sur **Charger toutes les couches du Cadastre**
4. Les 10 couches cadastrales se chargent automatiquement dans un groupe "Cadastre - {code INSEE}"
5. Les couches sont organisées et prêtes à l'emploi dans votre projet QGIS

Le flux WMS utilise le service INSPIRE de la DGFiP (https://inspire.cadastre.gouv.fr) et couvre l'ensemble du territoire français.

## Développement

Les contributions sont les bienvenues ! Veuillez suivre ces étapes :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence GNU General Public License v2.0 ou ultérieure.

## Contact

Yann Schwarz - yann.schwarz@ign.fr
