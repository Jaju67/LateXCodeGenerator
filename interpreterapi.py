from mathreader.api import *
from sympy import preview

def imageRecognition(input_image_path, output_image_path):
  #INPUT image file path ex.: 'file.png' + define the output image path 
  #function interprets the image as a handwritten equation then generates LateX code of said equation
  #RETURNS lateX code string
  #GENERATES LateX code visualisation and puts it in desired directory
 
  recognizer = HME_Recognizer() #initialize LateX interpreter
  try:
    recognizer.load_image(input_image_path,data_type="path") #loads image to the recognizer
  except:
    raise Exception("imageRecognition : invalid image path")

  try:
    expression, img = recognizer.recognize()
  except:
    preview("$$" + 'Formula\;not\;recognized, try\;again' + "$$", viewer = "file", filename = output_image_path, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 250","-bg","Transparent"])
    return '🍪'
                                                                  #-D 250 -> Setting dpi to 250 ; "-bg","Transparent" -> setting background to be transparent
  preview("$$" + expression + "$$", viewer = "file", filename = output_image_path, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 250","-bg","Transparent"])
  return expression     # the '$$' before and after expression are necessery
