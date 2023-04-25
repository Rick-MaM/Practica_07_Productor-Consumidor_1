from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import time
import random


class Producer_Consumer:
    def __init__(self, image, window):
        self.window = window
        self.List_cars = []
        self.List_time = [.5, 1, 2]
        self.image = image
        self.time_producer = "Aleatorio"
        self.time_consumer = "Aleatorio"

        menu_bar = Menu(self.window)
        menu_producer_consumer = Menu(menu_bar)
        menu_producer_consumer.add_command(
            label='producto-consumidor')
        menu_bar.add_cascade(label="Editar", menu=menu_producer_consumer)
        self.window.config(menu=menu_bar)

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

    app = Producer_Consumer(imag_2, window)

    window.mainloop()