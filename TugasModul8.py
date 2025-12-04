# KELOMPOK 30 SHIFT 5

# anti blur
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import messagebox, ttk

# MODUL 5: OOP 1 (CLASS, CONSTRUCTOR, INHERITANCE)
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Halo, namaku {self.name}."

class Student(Person):          # Inheritance
    def __init__(self, name, scores):
        super().__init__(name)  # memanggil constructor parent
        self.scores = scores    # array/list

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def grade(self):
        avg = self.average_score()

        # MODUL 2: PENGKONDISIAN
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"


def process_scores():
    name = entry_name.get()
    scores_text = entry_scores.get()

    if name.strip() == "":
        messagebox.showerror("Error", "Nama tidak boleh kosong!")
        return

    try:
        # MODUL 1: VARIABEL, TIPE DAYA, DAN ARRAY
        scores = [int(x) for x in scores_text.split(",")]
    except:
        messagebox.showerror("Error", "Nilai harus berupa angka dipisahkan koma.")
        return

    student = Student(name, scores)

    # MODUL 3: PERULANGAN
    score_lines = ""
    for i, s in enumerate(scores):
        score_lines += f"Nilai ke-{i+1}: {s}\n"

    # output
    result = (
        f"{student.introduce()}\n"
        f"-----------------------------------\n"
        f"Daftar Nilai:\n{score_lines}\n"
        f"Rata-rata: {student.average_score():.2f}\n"
        f"Grade: {student.grade()}\n"
    )

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# MODUL 8: GUI PROGRAMMING
root = tk.Tk()
root.title("Program Penilaian (Modul 1-3 & Modul 5)")
root.geometry("800x600")
root.configure(bg="#9ABBDC")

label_title = tk.Label(root, text="Program Penilaian Sederhana", font=("Arial", 16, "bold"), bg="#9ABBDC")
label_title.pack(pady=10)

frame = tk.Frame(root, bg="#9ABBDC")
frame.pack(pady=20)

tk.Label(frame, text="Nama Siswa:", font=("Arial", 11), bg="#9ABBDC").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Nilai (pisahkan koma):", font=("Arial", 11), bg="#9ABBDC").grid(row=1, column=0, sticky="w")
entry_scores = tk.Entry(frame, width=30)
entry_scores.grid(row=1, column=1, padx=10, pady=5)

btn = tk.Button(root, text="Proses Nilai", width=15, command=process_scores)
btn.pack(pady=10)

text_output = tk.Text(root, width=60, height=12, font=("Arial", 10))
text_output.pack(pady=10)

root.mainloop()
