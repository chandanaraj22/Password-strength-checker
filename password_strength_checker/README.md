# Password Strength Checker — Starter (macOS + VS Code)

## 1) Install Python 3 (if not already)
- Open Terminal and run: `python3 --version`
- If you don't see a version (e.g., 3.12.x), download from https://www.python.org/downloads/macos/ (macOS 64-bit universal2 installer). Run the installer.

## 2) Install VS Code
- Download from https://code.visualstudio.com/ and install.
- Launch VS Code.

## 3) Open this project
- In VS Code: File → Open Folder… → select the folder you unzipped: `password_checker_starter`.
- When prompted, install the **Python** extension by Microsoft.

## 4) Select the Python interpreter
- Press `Cmd+Shift+P` → type “Python: Select Interpreter” → choose a Python 3.x (not conda unless you use it).

## 5) Run the program
- In the Explorer (left), click `password_checker.py`.
- Open the integrated terminal: View → Terminal (or Ctrl+`).
- Run: `python3 password_checker.py`
- When prompted, type a password and press Enter.

## 6) Troubleshooting
- `zsh: command not found: python3` → Install Python from python.org, then restart VS Code.
- No “Run” button? Install the **Python** extension and reopen the `.py` file.
- Interpreter mismatch? Re-run “Python: Select Interpreter”.

## 7) Next steps
- Add suggestions if rules are missing.
- Add a scoring breakdown.
- Check against a common-passwords list.
- (Advanced) Entropy + HaveIBeenPwned API + GUI/Web UI.
