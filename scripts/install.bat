@echo off
cd ..
echo Installing HyperOS Enchanter Requirements...
echo Creating virtual environment (venv)...
python -m venv venv
echo Activating venv and installing packages...
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo.
echo Install Complete! You can now use scripts\start.bat to launch the app.
pause
