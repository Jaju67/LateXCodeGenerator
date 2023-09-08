from mathreader.api import *
from sympy import preview
#UNTESTEDUNTESTEDUNTESTEDUNTESTEDUNTESTEDUNTESTEDUNTESTEDUNTESTED
def imageRecognition(input_image_path, output_image_path = 'out.png'):
    #INPUT image file path ex.: 'file.png'
    #function interprets the image as a handwritten equation then generates LateX code of said equation
    #RETURNS lateX code string
    #GENERATES LateX code visualisation and puts it in desired place
    
    recognizer = HME_Recognizer() #initialize LateX interpreter
    
    try:
        recognizer.load_image(input_image_path,data_type="path") #loads image to the recognizer
    except:
        raise Exception("imageRecognition : invalid image path")

    expression, img = recognizer.recognize()
    preview("$$" + expression + "$$", viewer = "file", filename = output_image_path)
    return expression