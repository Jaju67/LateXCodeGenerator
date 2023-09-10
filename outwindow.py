import tkinter as tk
from tkinter import ttk
from interpreterapi import imageRecognition

class outputWindow:

    def __init__(self, inputImagePath, windowNumber):       
        self.outWindow = tk.Toplevel()          #'Toplevel' indicates that the window will not be a main window
        self.outWindow.title('Output')
        self.imagePath = 'output_image' + str(windowNumber) + '.png'
        self.latexCode = imageRecognition(inputImagePath, self.imagePath)

        self.icon = tk.PhotoImage(file = 'LXCG.png')                                                                        #Import project icon
        self.outWindow.wm_iconphoto(False, self.icon)
        
        self.widgets()
        self.outWindow.mainloop()

    def widgets(self):                                                                                                      #Contents of the window
        self.image = tk.PhotoImage(file=self.imagePath)
        imageLabel = ttk.Label(self.outWindow, image = self.image)                                                          #Import and display LateX image 
        imageLabel.pack()

        textLabel = ttk.Label(self.outWindow, text = 'LateX code: ' + self.latexCode + ' ',font=("Arial Bold", 16))         #Display LateX code 
        textLabel.pack()
        
        def buttonCopy():                                                                                                   #Copy button display and its functionality
            self.outWindow.clipboard_clear
            self.outWindow.clipboard_append(self.latexCode)
        copyButton = ttk.Button(self.outWindow, text = 'Copy', command = buttonCopy)
        copyButton.pack()