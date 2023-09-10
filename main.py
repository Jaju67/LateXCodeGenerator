import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw
import PIL
import os

import interface

# starting size of the interface (in pixels)
set_width = 600
set_height = 400

window = tk.Tk()
window.geometry(str(set_width)+'x'+str(set_height))
window.title('LateXCodeGenerator')


# thumbnail icon
icon = tk.PhotoImage(file = 'LXCG.png')
window.wm_iconphoto(False, icon)


canvas = tk.Canvas(window, width=set_width, height=set_height, bg = '#d9d9d9')
canvas.pack()


image = PIL.Image.new('RGB', (set_width, set_height), (255, 255, 255))

interface.rysowanie_hud(canvas, image, window)

interface.draw(canvas, image)

def onClosing():    #asks if user wants to close with a popup window and removes tmp image files
    if messagebox.askokcancel("Quit", "Quit LXCG?"):
        try:
            os.remove('drawnImage.png')
            os.remove('generatedImage.png')
        except:
            pass
        window.destroy()

window.protocol("WM_DELETE_WINDOW", onClosing)
window.mainloop()