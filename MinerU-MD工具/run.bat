@echo off
cd /d "%~dp0"

set "PY=python"
where python >nul 2>nul
if not errorlevel 1 goto start

set "PY=py -3"
where py >nul 2>nul
if errorlevel 1 goto nopython

:start
%PY% -c "import PySide6, requests, pypdfium2" >nul 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    %PY% -m pip install -r requirements.txt
)

echo Starting MinerU MD Tool...
%PY% app.py
pause
exit /b 0

:nopython
echo [ERROR] Python not found. Please install Python and add to PATH.
pause
exit /b 1
