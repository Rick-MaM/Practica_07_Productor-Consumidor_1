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
            label='producto-consumidor',command=self.Edit)
        menu_bar.add_cascade(label="Editar", menu=menu_producer_consumer)
        self.window.config(menu=menu_bar)

    def is_time_random(self, producer_or_consumer):
        if (self.time_consumer == "Aleatorio" and producer_or_consumer == "consumer") or (self.time_producer == "Aleatorio" and producer_or_consumer == "producer"):
            rand = random.randint(0, 2)
            return self.List_time[rand]
        else:
            if self.time_producer != "Aleatorio" and producer_or_consumer == "producer":
                return float(self.time_producer)
            if self.time_consumer != "Aleatorio" and producer_or_consumer == "consumer":
                return float(self.time_consumer)
    
    def edit_time(self):
        self.time_consumer = self.cmb_time_consumer.get()
        self.time_producer = self.cmb_time_producer.get()
            
    def Edit(self):
        root = Tk()
        root.title("Edit")
        root.geometry("180x180")

        Label(root, text="Productor").place(x=10, y=10)
        variable_producer = StringVar()
        self.cmb_time_producer = ttk.Combobox(
            root, width=17, textvariable=variable_producer)
        self.cmb_time_producer["values"] = ("Aleatorio", "0.5", "1", "2")
        self.cmb_time_producer.place(x=10, y=40)
        self.cmb_time_producer.current(0)

        Label(root, text="Consumidor").place(x=10, y=80)
        variable_consumer = StringVar()
        self.cmb_time_consumer = ttk.Combobox(
            root, width=17, textvariable=variable_consumer)
        self.cmb_time_consumer["values"] = ("Aleatorio", "0.5", "1", "2")
        self.cmb_time_consumer.place(x=10, y=110)
        self.cmb_time_consumer.current(0)

        btn_save = Button(root, text="Guardar", command=self.edit_time)
        btn_save.place(x=20, y=150)

        root.mainloop()

    def parking(self, position):
        if position == 1:
            self.lbl_car_1 = Label(self.window, image=self.image)
            self.lbl_car_1.place(x=2, y=35)
        elif position == 2:
            self.lbl_car_2 = Label(self.window, image=self.image)
            self.lbl_car_2.place(x=103, y=35)
        elif position == 3:
            self.lbl_car_3 = Label(self.window, image=self.image)
            self.lbl_car_3.place(x=207, y=35)
        elif position == 4:
            self.lbl_car_4 = Label(self.window, image=self.image)
            self.lbl_car_4.place(x=310, y=35)
        elif position == 5:
            self.lbl_car_5 = Label(self.window, image=self.image)
            self.lbl_car_5.place(x=414, y=35)
        elif position == 6:
            self.lbl_car_6 = Label(self.window, image=self.image)
            self.lbl_car_6.place(x=516, y=35)
        elif position == 7:
            self.lbl_car_7 = Label(self.window, image=self.image)
            self.lbl_car_7.place(x=2, y=205)
        elif position == 8:
            self.lbl_car_8 = Label(self.window, image=self.image)
            self.lbl_car_8.place(x=103, y=205)
        elif position == 9:
            self.lbl_car_9 = Label(self.window, image=self.image)
            self.lbl_car_9.place(x=207, y=205)
        elif position == 10:
            self.lbl_car_10 = Label(self.window, image=self.image)
            self.lbl_car_10.place(x=310, y=205)
        elif position == 11:
            self.lbl_car_11 = Label(self.window, image=self.image)
            self.lbl_car_11.place(x=414, y=205)
        elif position == 12:
            self.lbl_car_12 = Label(self.window, image=self.image)
            self.lbl_car_12.place(x=516, y=205)

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