# 📄 Python File Word Counter

A simple Python program that allows users to select a file via a **graphical dialog** and count the total number of words in the file. This project is ideal for beginners learning **file handling, GUI interaction, and exception handling** in Python.

---

## 🚀 Features
- File selection using **Tkinter** file dialog  
- Supports multiple file formats: `.txt`, `.csv`, `.log`, `.md`, `.json`, `.py`  
- Counts total words in the selected file  
- Colored terminal output using **Colorama** (green for success, red for errors)  
- Handles file read errors and invalid selections gracefully  

---

## 🛠️ Technologies Used
- Python 3  
- Tkinter  
- Colorama  

---

## ⚙️ How to Run
- Ensure Python is installed on your system  
- Install `colorama` if not already installed:
```bash
pip install colorama
```
- Save the script as word_counter.py
4. Run the script:
```bash
python word_counter.py
```

---

## 🎮 How It Works
- A file dialog opens for the user to select a file
- The program reads the file content
- Splits the text into words
- Counts the total number of words
- Displays the result in the terminal with colored output

---

## ⚠️ Error Handling
- Shows a message if no file is selected
- Catches exceptions during file reading (e.g., permission issues, corrupted files)

---

## 📈 Future Improvements
- Count characters, lines, or sentences
- Add a GUI window to display results
- Support more file formats
- Add a history of word counts

---

### 💡 Beginner-friendly project to practice Python scripting, GUI basics, and text processing.
