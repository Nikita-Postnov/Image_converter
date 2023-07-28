import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

def convert_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        image = Image.open(file_path)
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[
            ("JPEG files", "*.jpg"),
            ("PNG files", "*.png"),
            ("GIF files", "*.gif"),
            ("All Files", "*.*")
        ])
        if save_path:
            image.save(save_path)

# Создаем графический интерфейс
root = tk.Tk()
root.title("Image Converter")

# Кнопки для открытия изображения и конвертации
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

convert_button = tk.Button(root, text="Convert Image", command=convert_image)
convert_button.pack(pady=10)

# Метка для отображения выбранного изображения
image_label = tk.Label(root)
image_label.pack()

root.mainloop()
