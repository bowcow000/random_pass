import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    password_length = length_slider.get()
    chars = ''
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += "!@#$%"

    if not chars:
        messagebox.showwarning("Ошибка", "Выберите хотя бы один тип символов для генерации пароля!")
        return
    password = ''.join(random.choice(chars) for _ in range(password_length))

    print(f"Сгенерированный пароль: {password}")

    password_label.config(text=password)


root = tk.Tk()
root.title("Генератор паролей")

lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)

header_label = tk.Label(root, text="Генератор паролей", font=("Helvetica", 16))
header_label.pack(pady=10)

lowercase_checkbox = tk.Checkbutton(root, text="Нижние буквы (a-z)", variable=lowercase_var)
lowercase_checkbox.pack(anchor="w")

uppercase_checkbox = tk.Checkbutton(root, text="Высокие буквы (A-Z)", variable=uppercase_var)
uppercase_checkbox.pack(anchor="w")

digits_checkbox = tk.Checkbutton(root, text="Цифры (0-9)", variable=digits_var)
digits_checkbox.pack(anchor="w")

special_chars_checkbox = tk.Checkbutton(root, text="Спецсимволы (!@#$%)", variable=special_chars_var)
special_chars_checkbox.pack(anchor="w")

length_label = tk.Label(root, text="Длина пароля:")
length_label.pack(pady=(10, 0))

length_slider = tk.Scale(root, from_=1, to=50, orient="horizontal", length=300)
length_slider.set(8)
length_slider.pack(pady=(0, 10))

generate_button = tk.Button(root, text="Генерировать пароль", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", width=20, height=2, relief="sunken")
password_label.pack(pady=10)

root.mainloop()
