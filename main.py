import tkinter as tk
from PIL import Image, ImageDraw
import PIL

import interface
import interpreterapi


window = tk.Tk()
window.geometry('600x400')
window.title('LateXCodeGenerator')

canvas = tk.Canvas(window, width=600, height=400, bg = 'grey')
canvas.pack()

image = PIL.Image.new('RGB', (600, 400), (255, 255, 255))

interface.rysowanie_hud(canvas, image, window)

interface.draw(canvas, image)
window.mainloop()