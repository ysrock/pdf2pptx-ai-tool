@echo off
setlocal EnableDelayedExpansion

echo ========================================================
echo PDF2PPTX - CPU Standalone EXE Builder
echo ========================================================
echo.
echo This script will:
echo 1. Create a clean temporary environment (venv_build).
echo 2. Install CPU-only versions of Torch (to keep size small).
echo 3. Install necessary dependencies.
echo 4. Use PyInstaller to build a standalone .exe file.
echo.
echo [IMPORTANT] This will NOT affect your current GPU environment.
echo.

set "VENV_DIR=venv_build"

:: 1. Create Venv
if exist "%VENV_DIR%" (
    echo Cleaning up old venv...
    rmdir /s /q "%VENV_DIR%" 2>nul
    if exist "%VENV_DIR%" (
        echo [ERROR] Cannot delete old venv_build folder!
        echo Please close all terminals and manually delete: %CD%\%VENV_DIR%
        pause
        exit /b 1
    )
)
echo Creating virtual environment...
python -m venv %VENV_DIR%
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo [ERROR] Failed to create virtual environment!
    pause
    exit /b 1
)

:: 2. Activate Venv
call %VENV_DIR%\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment!
    pause
    exit /b 1
)
echo [OK] Virtual environment activated.

:: 3. Install CPU Dependencies
echo.
echo Installing CPU dependencies...
:: First install CPU torch to avoid downloading 4GB+ GPU binaries
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

:: Install other requirements
:: specific minimal list to ensure clean build
pip install pdfplumber opencv-python-headless rapidocr-onnxruntime python-pptx simple-lama-inpainting PyInstaller tkinterdnd2

:: 4. Build EXE
echo.
echo Building EXE with PyInstaller...
:: Define model path (using user home variable)
set "MODEL_PATH=%USERPROFILE%\.cache\torch\hub\checkpoints\big-lama.pt"

if not exist "%MODEL_PATH%" (
    echo [WARNING] Model file not found at %MODEL_PATH%
    echo The EXE will try to download it on first run.
    set "ADD_DATA="
) else (
    echo [INFO] Bundling LaMa model into EXE...
    set "ADD_DATA=--add-data "%MODEL_PATH%;.""
)

pyinstaller ^
    --name "PDF2PPTX_AI_Tool" ^
    --clean ^
    --onefile ^
    --noconfirm ^
    --collect-all rapidocr_onnxruntime ^
    --collect-all simple_lama_inpainting ^
    --collect-all tkinterdnd2 ^
    --hidden-import PIL ^
    --hidden-import cv2 ^
    --hidden-import pdfplumber ^
    --hidden-import tkinter ^
    --exclude-module pandas ^
    --exclude-module sklearn ^
    --exclude-module scipy ^
    --exclude-module matplotlib ^
    --exclude-module PyQt5 ^
    --exclude-module PyQt6 ^
    --exclude-module PySide6 ^
    --exclude-module IPython ^
    --exclude-module notebook ^
    --exclude-module jupyter ^
    %ADD_DATA% ^
    pdf2pptx_converter.py

echo.
echo Build Complete!
echo.
echo Your file is located in the "dist" folder:
echo dist\PDF2PPTX_AI_Tool.exe
echo.
echo You can now delete the 'venv_build' folder if you wish.
echo Done.
