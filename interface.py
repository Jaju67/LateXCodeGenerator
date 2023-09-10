import tkinter as tk
from PIL import Image, ImageDraw
from outwindow import outputWindow

def resize_window(window):
    window.geometry('1000x800')

class draw:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.image = image

        self.old_x = None
        self.old_y = None
        self.brush_size = 5
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.draw_image = ImageDraw.Draw(self.image)  # skróci pisanie

    def paint(self, e):
        if self.old_x and self.old_y:
            # Canvas drawing
            self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.brush_size, fill='black',
                                    capstyle='round', smooth=True)
            # Drawing in 'image' file
            self.draw_image.line([(self.old_x, self.old_y), (e.x, e.y)], fill='black', width=self.brush_size)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        self.old_x = None
        self.old_y = None


def rysowanie_hud(canvas, image, window):
    # Writing guide lines
    canvas.create_line((0, 100, 600, 100), dash=(5, 1))
    canvas.create_line((0, 300, 600, 300), dash=(5, 1))
    # upper text
    canvas.create_text((300, 50), text='Write your mathematical formula below:', font= ('Calibri', 30), width = 600)

    #definition of a 'Render' button function
    def show():
        image.save('drawnImage.png')
        windowInstance = outputWindow('drawnImage.png', 1)

    # 'Render' button
    canvas.create_window((500, 350), window=tk.Button(window, text='Render', font= ('Calibri', 30),
                                                      bg = 'purple', activebackground = 'green',
                                                      command=show))
    # 'Clear' button
    canvas.create_window((75, 350), window=tk.Button(window, text='Clear', font= ('Calibri', 30),
                                                     bg = 'purple', activebackground = 'green',
                                                     command = lambda: [canvas.delete('all'), ImageDraw.Draw(image).rectangle([(0, 0), (800, 600)], fill='white'), rysowanie_hud(canvas, image, window)]))
    # 'Resize' button
    canvas.create_window((300, 350), window=tk.Button(window, text='Resize', font=('Calibri', 30),
                                                     bg='purple', activebackground='green',
                                                     command=lambda: resize_window(window)))
