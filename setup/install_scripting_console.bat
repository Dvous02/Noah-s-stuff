@echo off
SETLOCAL ENABLEEXTENSIONS

echo.
echo [*] Welcome to the Scripting Console Installer (GUI only)
echo.

REM Set install path
SET "INSTALL_DIR=C:\Scripting Console"
IF NOT EXIST "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%\scripts"
    mkdir "%INSTALL_DIR%\dist\log"
)

echo [*] Checking for Python installation...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [!] Python not found. Please install Python 3.10+ and ensure it's added to your PATH.
    pause
    exit /b 1
)

echo [*] Installing Python requirements...
pip install -r requirements.txt

echo [*] Copying files to %INSTALL_DIR%...
xcopy /Y /I /S "ScriptingConsole.py" "%INSTALL_DIR%\ScriptingConsole.py"
xcopy /Y /I /S "ScriptingConsole.spec" "%INSTALL_DIR%\ScriptingConsole.spec"

echo [*] Installation complete.
echo Run 'python "%INSTALL_DIR%\ScriptingConsole.py"' to launch the GUI.
pause
