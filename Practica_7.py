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
