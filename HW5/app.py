import random
import cv2
import numpy

# path
imagePath = r'/Users/re9inee/VSCode/AI/Image_Processing_Class_Ferdowsi/HW5/flower.png'


def add_noise(img):
    # Getting the dimensions of the image
    row, col = img.shape

    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):

        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        img[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):

        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img


# salt-and-pepper noise can
# be applied only to grayscale images
# Reading the color image in grayscale image
img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original Image', img)
cv2.waitKey(0)

# make the image noisy and store it in a variable
noisyImage = add_noise(img)


cv2.imshow('Noisy Image', noisyImage)
cv2.imwrite('NoisyImage.png', noisyImage)
cv2.waitKey(0)


medianBlurImage = cv2.medianBlur(noisyImage, 5)


cv2.imshow('Output of Media Filter', medianBlurImage)
cv2.imwrite('Output.png', medianBlurImage)
cv2.waitKey(0)


# closing all open windows
cv2.destroyAllWindows()
