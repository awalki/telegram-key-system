@echo off
setlocal

:: Choice menu
echo 1. Open keygen
echo 2. Open telegram bot
set /p choice="Choose action (1 or 2): "

:: Choose handler
if "%choice%"=="2" (
    if not exist "venv" (
        python -m venv venv
	call venv\Scripts\activate.bat
        pip install -r requirements.txt
        set PYTHONPATH=..\telegram-key-system
        py src\telegram\main.py
    ) else (
        call venv\Scripts\activate.bat
        set PYTHONPATH=..\telegram-key-system
        py src\telegram\main.py
    )
) else if "%choice%"=="1" (
    if not exist "node_modules" (
	npm i -g yarn
	yarn install
	yarn tsc
	yarn keygen
    ) else (
	yarn tsc
	yarn keygen
)
) else (
    echo Invalid choice! Please select 1 or 2.
)

pause
endlocal
