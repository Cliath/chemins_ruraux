#!/bin/bash

# Script to compile resources and UI files for the QGIS plugin

# Compile resources
pyrcc5 resources.qrc -o resources.py

# Compile UI files
pyuic5 chemins_ruraux_dialog_base.ui -o chemins_ruraux_dialog_base.py

echo "Compilation terminée!"
