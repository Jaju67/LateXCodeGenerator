import tkinter as tk
from PIL import Image, ImageDraw
import PIL

import interface

# starting size of the interface (in pixels)
set_width = 600
set_height = 400

window = tk.Tk()
window.geometry(str(set_width)+'x'+str(set_height))
window.title('LateXCodeGenerator')


# ikonka
icon = tk.PhotoImage(file = 'LXCG.png')
window.wm_iconphoto(False, icon)


canvas = tk.Canvas(window, width=set_width, height=set_height, bg = 'grey')
canvas.pack()


image = PIL.Image.new('RGB', (set_width, set_height), (255, 255, 255))

interface.rysowanie_hud(canvas, image, window)

interface.draw(canvas, image)
window.mainloop()