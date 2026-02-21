#!/bin/bash

python3 -m pip install -r requirements-linux.txt pyinstaller --quiet

pyinstaller --noconfirm --onefile --console \
--workpath "/tmp/pyb" \
--specpath "/tmp/pyb" \
--distpath "." \
--name "qmenu" "qmenu.py" && rm -rf "/tmp/pyb"

echo "Done. Executable 'qmenu' created."