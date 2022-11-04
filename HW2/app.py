import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Import image and convert it into Unsigned integer then show it
image = mpimg.imread('image.jpg')
convertedImage = image.astype(np.uint8)

imgplot = plt.imshow(image)

plt.show()
