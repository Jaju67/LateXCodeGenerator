import tkinter as tk
from tkinter import ttk
from interpreterapi import imageRecognition

class outputWindow:

    def __init__(self, inputImagePath):       
        self.outWindow = tk.Toplevel()          #'Toplevel' indicates that the window will not be a main window
        self.outWindow.title('Output')
        self.imagePath = 'generatedImage.png'
        self.latexCode = imageRecognition(inputImagePath, self.imagePath)

        self.icon = tk.PhotoImage(file = 'LXCG.png')                                                                        #Import project icon
        self.outWindow.wm_iconphoto(False, self.icon)
        
        self.widgets()
        self.outWindow.mainloop()

    def widgets(self):                                                                                                      #Contents of the window
        self.image = tk.PhotoImage(file=self.imagePath)
        imageLabel = ttk.Label(self.outWindow, image = self.image)                                                          #Import and display LateX image 
        imageLabel.pack()

        if(self.latexCode == '🍪'):
            pass
        else:
            textLabel = ttk.Label(self.outWindow, text = 'LateX code: ' + self.latexCode + ' ',font=("Arial Bold", 16))         #Display LateX code 
            textLabel.pack()
        
            def buttonCopy():                                                                                                   #Copy button display and its functionality
                self.outWindow.clipboard_clear()
                self.outWindow.clipboard_append(self.latexCode)
        
            copyButton = tk.Button(self.outWindow, text = 'Copy',
                                    font = ('Arial Bold', 16),
                                    bg = 'purple',
                                    activebackground = 'green',
                                    command = buttonCopy)
            copyButton.pack()