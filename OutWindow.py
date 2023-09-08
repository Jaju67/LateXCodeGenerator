import tkinter as tk
from tkinter import ttk

class outputWindow:

    def __init__(self, latexCode, imagePath, name = 'Output'):       
        self.outWindow = tk.Tk()
        self.outWindow.title(str(name))
        self.latexCode = latexCode
        self.imagePath = imagePath
        self.widgets()
        self.outWindow.mainloop()

    def widgets(self):
        self.image = tk.PhotoImage(file=self.imagePath)
        imageLabel = ttk.Label(self.outWindow, image = self.image)                                                        #LateX image 
        imageLabel.pack()
        textLabel = ttk.Label(self.outWindow, text = 'LateX code: ' + self.latexCode + ' ',font=("Arial Bold", 16))       #LateX code 
        textLabel.pack()
        
        def buttonCopy():                                                                                                 #Copy button display and functionality
            self.outWindow.clipboard_clear
            self.outWindow.clipboard_append(self.latexCode)
        copyButton = ttk.Button(self.outWindow, text = 'Copy', command = buttonCopy)
        copyButton.pack()