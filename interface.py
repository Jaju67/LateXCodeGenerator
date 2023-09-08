import tkinter as tk
from PIL import Image, ImageDraw
import PIL

window = tk.Tk()
window.geometry('600x400')
window.title('wpisz równanie')

canvas = tk.Canvas(window, width=600, height=400, bg = 'grey')
canvas.pack()

image = PIL.Image.new('RGB', (600, 400), (255, 255, 255))

# stare malowanie, które słabo działa
# def malowanie(event):
#    x = event.x
#    y = event.y
#    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')

# średnica w pikselach
# brush_size = 4

# malowanie gdy się rusza pointer
# canvas.bind('<B1-Motion>', malowanie)
# malowanie gdy się nie rusza
# canvas.bind('<Button-1>', malowanie)

# lepsze malowanie


class draw:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.image = image

        self.old_x = None
        self.old_y = None
        self.brush_size = 5
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.draw_image = ImageDraw.Draw(self.image) # skróci pisanie



    def paint(self, e):
        if self.old_x and self.old_y:
            # rysowanie na płótnie
            self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, width = self.brush_size, fill = 'black', capstyle='round', smooth = True)
            # rysowanie w pliku image
            self.draw_image.line([(self.old_x, self.old_y), (e.x, e.y)], fill = 'black', width = self.brush_size)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        self.old_x = None
        self.old_y = None
    def image_back(self):
        self.image.save('testttt.png')


def rysowanie_hud():
    # linie pomocnicze
    canvas.create_line((0, 125, 600, 125), dash=(5, 1))
    canvas.create_line((0, 275, 600, 275), dash=(5, 1))
    # tekst u góry
    canvas.create_text((250, 50), text = 'Napisz matematyczną formułę:', width=100)
    # przycisk do renderowania kodu
    canvas.create_window((500, 350), window = tk.Button(window, text = 'Render', command = lambda:[image.show(), image.save('image.png')]))
    # przycisk restar/clear
    canvas.create_window((200, 350), window=tk.Button(window, text='Clear', command=clear))

# restart/clear
def clear():
    canvas.delete('all') # wyczyszczenie interfejsu
    ImageDraw.Draw(image).rectangle([(0, 0), (800, 600)], fill = 'white') # wyczyszczenie image
    rysowanie_hud()

# pierwsze narysowanie hud
rysowanie_hud()


draw(canvas, image)
window.mainloop()