@echo off
REM Script pour compiler et packager le plugin QGIS Chemins Ruraux

echo ========================================
echo  Compilation et packaging du plugin
echo ========================================
echo.

REM Étape 1 : Compilation
echo [1/2] Compilation des ressources et UI...
python compile_plugin.py
if %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de la compilation
    pause
    exit /b 1
)
echo.

REM Étape 2 : Packaging
echo [2/2] Création du package ZIP...
python package.py
if %ERRORLEVEL% NEQ 0 (
    echo Erreur lors du packaging
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Terminé !
echo ========================================
pause
