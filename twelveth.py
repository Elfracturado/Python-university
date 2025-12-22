import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import json


def get_repo_info():
    repo_fullname = entry.get().strip()
    if not repo_fullname or "/" not in repo_fullname:
        messagebox.showwarning("Ошибка", "Введите репозиторий в формате owner/repo")
        return

    try:
        url = f"https://api.github.com/repos/{repo_fullname}"
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("Ошибка", f"Репозиторий '{repo_fullname}' не найден")
            return
        data = response.json()

        result = {
            "company": None,  # для репо обычно нет company
            "created_at": data.get("created_at"),
            "email": None,
            "id": data.get("id"),
            "name": data.get("name"),
            "url": data.get("owner", {}).get("url")
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON файлы", "*.json")],
                                                 initialfile=f"{repo_fullname.replace('/', '_')}.json")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Готово", f"Информация сохранена в {file_path}")

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


# ---------- GUI ----------
root = tk.Tk()
root.title("GitHub Repo Info")

tk.Label(root, text="Введите репозиторий (owner/repo):").pack(padx=10, pady=10)
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

tk.Button(root, text="Получить информацию", command=get_repo_info).pack(pady=10)

root.mainloop()
