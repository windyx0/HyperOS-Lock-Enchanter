@echo off
cd ..
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo VENV not found. Please run scripts\install.bat first!
    pause
    exit /b
)
call venv\Scripts\activate.bat
echo Loading...
python enchanter.py
pause
