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

## 📁 Installation Directory
Installs to: `C:\Scripting Console\` by default


***Disclaimer: during the process of creating the exe file, my AV gave a false positive to malware. please make sure to confirm scripts a free from any malicious code before use, additionally utilise VirtualBox or take other sandbox precautions before use***


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
