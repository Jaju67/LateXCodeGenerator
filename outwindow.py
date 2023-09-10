import tkinter as tk
from tkinter import ttk
from interpreterapi import imageRecognition

class outputWindow:

    def __init__(self, inputImagePath, windowNumber):       
        self.outWindow = tk.Tk()
        self.outWindow.title('Output ' + str(windowNumber))
        self.imagePath = 'output_image' + str(windowNumber)
        self.latexCode = imageRecognition(inputImagePath, self.imagePath)

        # self.icon = tk.PhotoImage(file = 'LXCG.png')
        # self.outWindow.wm_iconphoto(False, icon)
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
