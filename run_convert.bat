@echo off
setlocal

:: Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"
set "PYTHON_SCRIPT=%SCRIPT_DIR%pdf2pptx_converter.py"

:: Check if a file was dropped
if "%~1"=="" (
    echo Please drag and drop a PDF file onto this script.
    pause
    exit /b
)

:: Get file extension
set "FILE_EXT=%~x1"
if /I not "%FILE_EXT%"==".pdf" (
    echo The dropped file is not a PDF.
    pause
    exit /b
)

:: Generate output filename (InputName_Editable.pptx)
set "INPUT_FILE=%~1"
set "OUTPUT_FILE=%~dpn1_Editable.pptx"

echo Processing: "%INPUT_FILE%"
echo Output will be: "%OUTPUT_FILE%"
echo.
echo Starting conversion... This may take a while (downloading model or processing on CPU)...
echo.

python "%PYTHON_SCRIPT%" "%INPUT_FILE%" "%OUTPUT_FILE%"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error encounted!
    pause
) else (
    echo.
    echo Done! File created at:
    echo "%OUTPUT_FILE%"
    pause
)
