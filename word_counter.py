import tkinter as tk
from tkinter import filedialog
from colorama import Fore, Style
import os


root_window = tk.Tk()
root_window.withdraw()
print("Use the dialog box to select your file: ")
file_path = filedialog.askopenfilename(
    parent = root_window,
    title = "Please select your file",
    filetypes = (
        ("Text files", "*.txt"),
        ("CSV files", "*.csv"),
        ("Log files", "*.log"),
        ("Markdown files", "*.md"),
        ("JSON files", "*.json"),
        ("Python files", "*.py"))
    )

root_window.destroy()

if file_path:
    try:
        with open(file_path, 'r') as fl:
            content = fl.read()
            words = content.split()
            num_of_words = len(words)
            filename = os.path.basename(file_path)
            print(Fore.GREEN + f"The file {filename} has {num_of_words} words" + Style.RESET_ALL)
        
    except Exception as e:
        print(Fore.RED + f"Error reading {filename}: {e}" + Style.RESET_ALL)
else:
    print(Fore.RED + "No file selected!\n" + Style.RESET_ALL)
