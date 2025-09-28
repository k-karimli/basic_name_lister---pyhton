
import tkinter as tk
from tkinter import messagebox, simpledialog

# siyahı
names = []

# adlari göstərən funksiya
def update_listbox():
    listbox.delete(0, tk.END)
    for i, name in enumerate(names, start=1):
        listbox.insert(tk.END, f"{i}. {name}")

# ad əlavə et
def add_name():
    name = simpledialog.askstring("Ad əlavə et", "Əlavə etmək istədiyiniz adı yazın:")
    if name:
        names.append(name)
        update_listbox()

# ad sil
def remove_name():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Xəta", "Silinəcək adı seçin!")
        return
    index = selection[0]
    del names[index]
    update_listbox()

# ad dəyiş
def change_name():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Xəta", "Dəyişiləcək adı seçin!")
        return
    index = selection[0]
    new_name = simpledialog.askstring("Ad dəyiş", "Yeni adı daxil edin:")
    if new_name:
        names[index] = new_name
        update_listbox()

# əsas pəncərə
root = tk.Tk()
root.title("Adlar Siyahısı")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

# düymələr
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_add = tk.Button(btn_frame, text="Ad əlavə et", command=add_name)
btn_add.grid(row=0, column=0, padx=5)

btn_remove = tk.Button(btn_frame, text="Ad sil", command=remove_name)
btn_remove.grid(row=0, column=1, padx=5)

btn_change = tk.Button(btn_frame, text="Ad dəyiş", command=change_name)
btn_change.grid(row=0, column=2, padx=5)

btn_exit = tk.Button(btn_frame, text="Çıxış", command=root.quit)
btn_exit.grid(row=0, column=3, padx=5)

root.mainloop()
