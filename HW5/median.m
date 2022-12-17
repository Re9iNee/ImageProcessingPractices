I = imread('flower.png');
Im = rgb2gray(I);

noisy = imnoise(Im, 'salt & pepper', 0.1);

[m, n] = size(noisy);
ouput = zeros(m, n);
output = uint8(output);

for i = 1:m

    for j = 1:n
        xmin = max(1, i - 1);
        xmax = min(m, i + 1);
        ymin = max(1, j - 1);
        ymax = min(n, j + 1);
        % neighborhood matrix
        temp = noisy(xmin:xmax, ymin:ymax);
        output(i, j) = median(temp(:), 'all');
    end

end

% Show Output
figure(1);
set(gcf, 'Position', get(0, 'ScreenSize'));
subplot(131), imshow(I), title("Original Image")
subplot(132), imshow(noisy), title("Noisy Image")
subplot(133), imshow(output), title("Output of Media Filter")
