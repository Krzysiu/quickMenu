# 🚀 QuickMenu (qmenu)

A lightweight CLI selector built for Windows batch scripts and automation workflows. It provides a visual menu for command-line interfaces, allowing users to make selections using arrow keys without complex scripting.

![readme-example](https://github.com/user-attachments/assets/33dc227c-3e99-4384-8305-845f88669166)


## ✨ Features
* **Zero Dependencies**: Standalone EXE, no Python environment needed on the target machine.
* **Dual-Output**: Get results via system exit code or by reading a generated file.
* **Modern Terminal Support**: Full UTF-8/Unicode support for icons and special characters.

---
## 💾 Download

You can find the latest standalone binary in the **[Releases](https://github.com/quickMenu/releases)** section:

* **`qmenu-0-0-1-win64.7z`**: Pre-compiled executable for Windows (64-bit). Just extract and run.
## 🛠 Usage

```bash
qmenu -c "Option 1,Option 2,Option 3" [options]
```

### Parameters

| Flag | Name | Description |
| :--- | :--- | :--- |
| `-c` | `--choices` | **Required.** Comma-separated list of items to display. |
| `-t` | `--title` | Custom menu title. |
| `-d` | `--desc` | Custom subtitle/description. |
| `-f` | `--file` | Save selected text to file. Defaults to `%TEMP%\lastItem.mnu`. |
| `-ne`| `--no-exit` | **Success Mode.** Returns exit code `0` on selection and `1` on Cancel/Esc. Perfect for `&&` chaining. |
| `-h` | `--help` | Show help and version information. |

---

## 💡 Examples

### 1. Simple Batch Selector (Success Mode)
QuickMenu maps the selection to `ERRORLEVEL`. Using `-ne` allows you to chain commands easily.

```batch
@echo off
qmenu -t "Weather Selection" -d "Choose your weather modifier" -c "Increase temperature,Decrease temperature,Quick flood mode" -ne && (
    echo "Modification applied successfully!"
) || (
    echo "Action cancelled by user."
)
```

### 2. Python Integration
Retrieve the selection index (from list) or the literal text from the output file.

```python
import subprocess
import os
import tempfile

options = ["Increase temperature", "Decrease temperature", "Quick flood mode"]
path = os.path.join(tempfile.gettempdir(), 'lastItem.mnu')

res = subprocess.run(['qmenu.exe', '-c', ','.join(options), '-t', 'Weather Selection', '-f'], capture_output=False)

if 0 < res.returncode < 255:
    print(f"Selected item index: {res.returncode}")
    print(f"Selected item text (internal): {options[res.returncode - 1]}")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            print(f"Selected item text (file): {f.read()}")
```

### 3. PHP Integration
```php
<?php
$options = ["Increase temperature", "Decrease temperature", "Quick flood mode"];
$tempFile = sys_get_temp_dir() . DIRECTORY_SEPARATOR . 'lastItem.mnu';

system('qmenu.exe -c "' . implode(',', $options) . '" -t "Weather Selection" -f', $retval);

if ($retval > 0 && $retval != 255) {
    echo "Selected item index: $retval\n";
    echo "Selected item text (internal): " . $options[$retval - 1] . "\n";
    
    if (file_exists($tempFile)) {
        echo "Selected item text (file): " . file_get_contents($tempFile) . "\n";
    }
}
?>
```

---

## 🛠 Build
To compile the binary yourself, use the provided build scripts. They handle environment cleanup and PyInstaller optimization automatically.

* **Windows:** Run `make.bat`
* **Linux (Cross-compile):** Run `./make.sh`

---

# ☕ Support the effort
Built to save your time and sanity. If it worked, you can say "thanks" by buying me a coffee!

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/krzysiunet)
