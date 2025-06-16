# Commander Scripting Console

# Scripting Console

A lightweight, GUI-based script execution platform for Windows systems.

## 🔍 What It Does
- Runs `.py`, `.bat`, and `.ps1` scripts silently
- GUI to write, load, and save script templates
- Logs outputs and errors for easy review

## 🎯 Intended Use
For developers and learners who want:
- A clean interface for script testing and usage
- To avoid syntax errors and shell noise
- A helpful GUI without needing to open CMD or PowerShell


> ⚠️ **Disclaimer**: During the build process, some antivirus programs may flag the generated `.exe` as potentially malicious. This is a common false positive with Python scripts compiled using PyInstaller, especially when scripts execute system commands or spawn processes.
>
> To stay safe:
> - Always review the source code before execution.
> - Run in a virtual machine (e.g., VirtualBox) or sandbox environment if unsure.
> - Avoid running unknown scripts unless you trust the source.

This project contains **no malicious code**, but precautions are encouraged — especially for beginners.





## 📁 Installation Directory
Installs to: `C:\Scripting Console\` by default



---

## Installation Guide

# 🛠 Installation Guide (Scripting Console GUI)

1. **Install Python 3.10+** from https://www.python.org (add to PATH during install)

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the EXE**
   ```bash
   pyinstaller --noconsole ScriptingConsole.spec
   ```

4. **Create Working Folders**
   ```cmd
   mkdir "C:\Scripting Console\scripts"
   mkdir "C:\Scripting Console\dist\log"
   ```

5. **Launch GUI**
   Run `ScriptingConsole.py` directly with Python or use the generated EXE.
