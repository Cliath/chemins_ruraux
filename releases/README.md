# Releases - Voirie Communale

## Comment installer une version

1. Téléchargez le fichier `.zip` de la version souhaitée
2. Ouvrez QGIS
3. Menu **Extensions** → **Installer/Gérer les extensions**
4. Onglet **Installer depuis un ZIP**
5. Sélectionnez le fichier téléchargé
6. Cliquez sur **Installer l'extension**

## Versions disponibles

### [v0.1.0](chemins_ruraux-0.1.0.zip) - 2026-01-25

**Première version fonctionnelle**

- ✅ Intégration du flux WMS cadastre INSPIRE (DGFiP)
- ✅ Champ de saisie pour le code INSEE
- ✅ Sélection des couches cadastrales (parcelles, bâtiments, sections)
- ✅ Validation du code INSEE
- ✅ Documentation complète

**Fichier** : `chemins_ruraux-0.1.0.zip` (12.58 KB)

---

## Notes de version

Pour plus de détails sur les modifications, consultez le [CHANGELOG.md](../CHANGELOG.md).

## Build d'une nouvelle version

Pour créer un package d'une nouvelle version :

```bash
# Windows
build.bat

# Linux/macOS
chmod +x build.sh
./build.sh
```

Ou manuellement :
```bash
# 1. Compiler
python compile_plugin.py

# 2. Packager
python package.py
```

Le fichier ZIP sera créé dans le dossier `releases/`.
