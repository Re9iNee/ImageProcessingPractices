import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

ROWS = 2
COLUMNS = 2

# create a figure
fig = plt.figure(figsize=(10, 7))


# import the image
originalImage = mpimg.imread('image.jpg')


# convert image into Unsigned integer then show it
convertedImage = originalImage.astype(np.uint8)

# Adds a subplot at the 1st position
fig.add_subplot(ROWS, COLUMNS, 1)
# showing original image
plt.imshow(originalImage)
plt.axis('off')
plt.title('Original Image')


# Adds a subplot at the 2nd position
fig.add_subplot(ROWS, COLUMNS, 2)
# showing converted image
plt.imshow(convertedImage)
plt.axis('off')
plt.title('Converted Image')


plt.show()
