originalImage = imread("image.jpg");

convertedImage = im2uint8(originalImage)
imshow(convertedImage);

figure;
imhist(convertedImage)
