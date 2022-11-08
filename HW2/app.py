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


# # Adds another subplot at the 3rd position
fig.add_subplot(ROWS, COLUMNS, 3)

# Write histogram for converted image
histogram, bin_edges = np.histogram(convertedImage.ravel(), 256, [0, 256])
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel('pixel count')
plt.xlim([0, 256])


plt.plot(bin_edges[0:-1], histogram)


# initialize the array to store histogram
myHistogram = np.zeros(256, np.uint8)

# get the row and column of the image
row, col = convertedImage.shape[0], convertedImage.shape[1]

print(row, col)

# creates the histogram of the image
for i in range(0, int(row / 8)):
    for j in range(0, int(col / 8)):
        myHistogram[convertedImage[i, j]] += 1

# Adds the last subplot at the 4th position
fig.add_subplot(ROWS, COLUMNS, 4)

plt.title("My Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel('pixel count')
plt.xlim([0, 256])


plt.plot(myHistogram)


plt.show()
