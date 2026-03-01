@echo off
REM Script pour compiler les ressources et fichiers UI pour le plugin QGIS

REM Compiler les ressources
pyrcc5 resources.qrc -o resources.py

REM Compiler les fichiers UI
pyuic5 chemins_ruraux_dialog_base.ui -o chemins_ruraux_dialog_base.py

echo Compilation terminee!
pause
