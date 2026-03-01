#!/bin/bash

# Script pour compiler et packager le plugin QGIS Chemins Ruraux

echo "========================================"
echo " Compilation et packaging du plugin"
echo "========================================"
echo

# Étape 1 : Compilation
echo "[1/2] Compilation des ressources et UI..."
python3 compile_plugin.py
if [ $? -ne 0 ]; then
    echo "Erreur lors de la compilation"
    exit 1
fi
echo

# Étape 2 : Packaging
echo "[2/2] Création du package ZIP..."
python3 package.py
if [ $? -ne 0 ]; then
    echo "Erreur lors du packaging"
    exit 1
fi

echo
echo "========================================"
echo " Terminé !"
echo "========================================"
