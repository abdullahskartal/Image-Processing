# Image-Processing
Erosion, Dilation, Opening, Closing, Gradient with opencv and numpy


## Requirement
- Opencv Library
- Numpy Library


## What exactly do we do?

### Erosion
The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). 

### Dilation
It is just opposite of erosion. Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases. It is also useful in joining broken parts of an object.

### Opening
Opening is just another name of erosion followed by dilation.

### Closing
Closing is reverse of Opening, Dilation followed by Erosion.

### Gradient
It is the difference between dilation and erosion of an image.
