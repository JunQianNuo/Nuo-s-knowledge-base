@echo off
cd /d "%~dp0"

set "PY=python"
where python >nul 2>nul
if not errorlevel 1 goto start

set "PY=py -3"
where py >nul 2>nul
if errorlevel 1 goto nopython

:start
echo Installing PyInstaller...
%PY% -m pip install pyinstaller

echo Building...
%PY% -m PyInstaller --noconfirm --windowed --name "MinerU_MD_Tool" app.py

echo Build complete: dist\MinerU_MD_Tool\MinerU_MD_Tool.exe
pause
exit /b 0

:nopython
echo [ERROR] Python not found. Please install Python and add to PATH.
pause
exit /b 1
