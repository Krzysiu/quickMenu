#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QuickMenu (qmenu)
Lightweight CLI selector for batch scripts.
(C) 2026 krzysiu.net
"""

import sys
import os
import argparse
import tempfile
import curses
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem

__version__ = "0.0.1"

class HotkeyMenu(CursesMenu):
    def process_user_input(self, *args, **kwargs):
        key = args[0] if args else self.stdscr.getch()
        
        if 49 <= key <= 57:
            sel = key - 49
            if sel < len(self.items):
                self.selected_option = sel
                self.items[self.selected_option].action()
                return 
        curses.ungetch(key)
        super().process_user_input()

def print_help():
    print(f"QuickMenu v{__version__} (bin: qmenu.exe)")
    print(f"(C) 2026, krzysiu.net, MIT license\n")
    print("Usage: qmenu -c \"opt1,opt2\" [-f [file]] [-ne]\n")
    print("Parameters:")
    print("\t-c, --choices\tcomma-separated list of options")
    print("\t-t, --title\tcustom menu title")
    print("\t-f, --file\tsave to [file] (default: %TEMP%\\lastItem.mnu)")
    print("\t-ne, --no-exit\talways return exit code 0 on success\n")

def main():
    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-c", "--choices", type=str, required=True)
    parser.add_argument("-t", "--title", type=str, default="QuickMenu")
    parser.add_argument("-d", "--desc", type=str, default="Select an option and press Enter")
    parser.add_argument("-f", "--file", nargs='?', const='lastItem.mnu')
    parser.add_argument("-ne", "--no-exit", action="store_true")

    try:
        args = parser.parse_args()
    except SystemExit:
        sys.exit(255)

    options = [opt.strip() for opt in args.choices.split(",")]
    state = {"idx": None, "text": None}

    def on_select(idx):
        state["idx"] = idx
        state["text"] = options[idx]
        menu.exit()

    menu = HotkeyMenu(title=args.title, subtitle=args.desc, show_exit_item=False)
    for i, opt in enumerate(options):
        menu.items.append(FunctionItem(opt, on_select, args=[i]))

    menu.show()

    if state["idx"] is not None:
        if args.file:
            path = args.file
            if path == 'lastItem.mnu':
                path = os.path.join(tempfile.gettempdir(), 'lastItem.mnu')
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(state["text"])
            except:
                pass
        sys.exit(0 if args.no_exit else state["idx"] + 1)
    else:
        sys.exit(255)

if __name__ == "__main__":
    main() 