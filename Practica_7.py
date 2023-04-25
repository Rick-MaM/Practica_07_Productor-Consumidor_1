from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import time
import random


def open_image(name, size_1, size_2):
    image = Image.open(name)
    new_image = image.resize((size_1, size_2))
    render = ImageTk.PhotoImage(new_image)
    return render


if __name__ == "__main__":
    window = Tk()
    window.title("Practica 7")
    window.geometry("600x400")

    imag = open_image("Estacionamiento.png", 600, 400)
    lbl = Label(window, image=imag).pack()

    imag_2 = open_image("Vehiculo.png", 80, 150)

    window.mainloop()