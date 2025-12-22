import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

# Основное окно
root = tk.Tk()
root.title("Звягинцев Никита Александрович")
root.geometry("500x400")

# Вкладки
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill='both', padx=10, pady=10)  # равномерные отступы

# Калькулятор
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")

tk.Label(tab1, text="Число 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(tab1)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab1, text="Число 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(tab1)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(tab1, text="Операция:").grid(row=2, column=0, padx=5, pady=5)
operation = ttk.Combobox(tab1, values=["+", "-", "*", "/"], state="readonly")
operation.grid(row=2, column=1, padx=5, pady=5)
operation.current(0)

result_label = tk.Label(tab1, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operation.get()
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("Ошибка", "Деление на ноль!")
                return
            res = a / b
        result_label.config(text=f"Результат: {res}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

tk.Button(tab1, text="Вычислить", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

# Чекбоксы
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Чекбоксы")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

tk.Checkbutton(tab2, text="Первый", variable=var1).pack(anchor="w", padx=10, pady=5)
tk.Checkbutton(tab2, text="Второй", variable=var2).pack(anchor="w", padx=10, pady=5)
tk.Checkbutton(tab2, text="Третий", variable=var3).pack(anchor="w", padx=10, pady=5)

def show_selection():
    selections = []
    if var1.get():
        selections.append("первый")
    if var2.get():
        selections.append("второй")
    if var3.get():
        selections.append("третий")
    if selections:
        messagebox.showinfo("Выбор", "Вы выбрали: " + ", ".join(selections))
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

tk.Button(tab2, text="Показать выбор", command=show_selection).pack(pady=10)

# Работа с текстом
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Текст")

text_box = tk.Text(tab3, wrap="word")
text_box.pack(expand=1, fill="both", padx=10, pady=10)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f.read())

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть файл", command=open_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)


root.mainloop()
