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

REM Étape 3 (optionnelle) : Déploiement dans QGIS (push-only, sens unique)
set QGIS_PLUGINS=%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\chemins_ruraux
echo [Optionnel] Déployer dans QGIS ? (O/N)
set /p DEPLOY="> "
if /I "%DEPLOY%"=="O" (
    echo.
    echo [3/3] Déploiement vers %QGIS_PLUGINS%...
    set "SRC=%~dp0."
    robocopy "%SRC%" "%QGIS_PLUGINS%" /MIR /XD .git releases __pycache__ .github .vscode /XF *.zip *.qrc *.ui *.bat *.sh *.py.bak /NFL /NDL /NJH /NJS
    if %ERRORLEVEL% GTR 7 (
        echo Erreur lors du déploiement
    ) else (
        echo Deploiement termine avec succes ^!
    )
) else (
    echo Déploiement ignoré.
)

echo.
echo ========================================
echo  Terminé !
echo ========================================
pause
