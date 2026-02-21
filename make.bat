@echo off
magick -background none "icon.svg" -define icon:auto-resize=256,128,64,48,32,16 "icon.ico"

python -m venv "%TEMP%\qmenu_venv"
call "%TEMP%\qmenu_venv\Scripts\activate.bat"

python -m pip install -r requirements-win.txt pyinstaller --quiet

pyinstaller --noconfirm --onefile --console ^
 --exclude-module ssl ^
 --exclude-module _ssl ^
 --exclude-module hashlib ^
 --exclude-module _hashlib ^
 --exclude-module tkinter ^
 --exclude-module tcl ^
 --exclude-module tk ^
 --exclude-module _tkinter ^
 --exclude-module unittest ^
 --exclude-module pydoc ^
 --icon "%~dp0icon.ico" --workpath "%TEMP%\pyb" --specpath "%TEMP%\pyb" --distpath "." --name "qmenu" "qmenu.py"
 
call deactivate
rd /s /q "%TEMP%\qmenu_venv"
rd /s /q "%TEMP%\pyb"
del /q "icon.ico"