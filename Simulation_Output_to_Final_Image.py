from PIL import Image
import numpy as np


pixels = [
  #Copy the contents of Tcl Console here to obtain the image back from pixel data.
]

# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
#The Output File will be saved in the same folder where the python file is saved
new_image.save('output.png')
