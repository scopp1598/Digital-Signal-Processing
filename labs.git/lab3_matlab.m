% Question 9
kern = -1/256*[1 4 6 4 1; 4 16 24 16 4; 6 24 -476 24 6; 4 16 24 16 4; 1 4 6 4 1];
y = conv2(imageOfInterest, kern, 'valid');
imshow(y, [])