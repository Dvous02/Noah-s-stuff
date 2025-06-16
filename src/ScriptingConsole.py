import os, tempfile, subprocess, datetime, shutil
from tkinter import Tk, Button, messagebox, scrolledtext, StringVar, OptionMenu, Menu, Frame, filedialog
from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator

SCRIPTS_DIR = r"C:\Commander\scripts"
LOG_DIR = r"C:\Commander\dist\log"
os.makedirs(SCRIPTS_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

def detect_script_type(code):
    if code.strip().startswith("import") or "def " in code or "os." in code:
        return "Python"
    elif "$" in code or "Get-" in code:
        return "PowerShell"
    elif ":" in code and "echo" in code.lower():
        return "Batch"
    else:
        return "Batch"

def execute_script(event=None):
    script = text_area.get("1.0", "end-1c").strip()
    if not script:
        messagebox.showwarning("Empty", "Script input is empty.")
        return
    lang = detect_script_type(script)
    script_type.set(lang)
    ext = { "Python": ".py", "Batch": ".bat", "PowerShell": ".ps1" }[lang]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(LOG_DIR, f"used_script_{timestamp}{ext}")
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write(script)
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext, mode="w", encoding="utf-8") as f:
        f.write(script)
        temp_path = f.name

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        if lang == "Python":
            result = subprocess.run(["python", temp_path],
                                    capture_output=True,
                                    text=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW,
                                    startupinfo=startupinfo)
        elif lang == "PowerShell":
            result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", temp_path],
                                    capture_output=True,
                                    text=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW,
                                    startupinfo=startupinfo)
        else:
            result = subprocess.run(["cmd.exe", "/c", temp_path],
                                    capture_output=True,
                                    text=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW,
                                    startupinfo=startupinfo)

        output_console.insert("end", "\n[+] Output:\n" + result.stdout + "\n")
        if result.stderr:
            output_console.insert("end", "[!] Errors:\n" + result.stderr + "\n")
        output_console.see("end")
        messagebox.showinfo("Success", "Script executed successfully.")
    except subprocess.CalledProcessError as e:
        output_console.insert("end", "[!] Subprocess failed:\n" + str(e) + "\n")
        messagebox.showerror("Error", f"Script failed.\n\n{e}")
    finally:
        os.remove(temp_path)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

def load_file():
    path = filedialog.askopenfilename(initialdir=SCRIPTS_DIR, filetypes=[("Script Files", "*.bat *.py *.ps1")])
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        text_area.delete("1.0", "end")
        text_area.insert("1.0", content)
        script_type.set(detect_script_type(content))

def save_template():
    path = filedialog.asksaveasfilename(initialdir=SCRIPTS_DIR, defaultextension=".bat",
        filetypes=[("Python", "*.py"), ("Batch", "*.bat"), ("PowerShell", "*.ps1")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", "end-1c"))
        messagebox.showinfo("Saved", f"Template saved to:\n{path}")

def open_scripts_folder():
    subprocess.Popen(f'explorer "{SCRIPTS_DIR}"')

# --- GUI Setup ---
app = Tk()
app.title("Commander Script Console")
app.geometry("900x650")

frame = Frame(app)
frame.pack(fill="x", padx=5, pady=2)

script_type = StringVar(value="Batch")
dropdown = OptionMenu(frame, script_type, "Batch", "Python", "PowerShell")
dropdown.pack(side="right", padx=5)
Button(frame, text="Open Scripts Folder", command=open_scripts_folder).pack(side="right", padx=5)
Button(frame, text="Load Script", command=load_file).pack(side="right", padx=5)
Button(frame, text="Save As Template", command=save_template).pack(side="right", padx=5)

text_area = scrolledtext.ScrolledText(app, wrap="word", font=("Consolas", 11), undo=True)
text_area.pack(expand=True, fill="both", padx=5, pady=5)
Percolator(text_area).insertfilter(ColorDelegator())

output_console = scrolledtext.ScrolledText(app, height=8, state="normal", wrap="word", bg="white", fg="black", font=("Consolas", 9))
output_console.pack(fill="x", padx=5, pady=(0, 5))

run_btn = Button(app, text="Run Script (Ctrl+Enter)", bg="black", fg="lime", height=2, command=execute_script)
run_btn.pack(fill="x")

context_menu = Menu(app, tearoff=0)
for label, event in [("Cut", "<<Cut>>"), ("Copy", "<<Copy>>"), ("Paste", "<<Paste>>"), ("Select All", "<<SelectAll>>")]:
    context_menu.add_command(label=label, command=lambda ev=event: text_area.event_generate(ev))

text_area.bind("<Button-3>", show_context_menu)
text_area.bind("<Control-Return>", execute_script)

app.mainloop()
