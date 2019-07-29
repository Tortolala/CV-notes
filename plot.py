# Author: Angel Tórtola

import numpy
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def imgview(img, title = None, filename = None):
    """ Description of this function.

    Args:
        img (numpy array): image array
        title (string): image title
        filename (string): image filename

    Returns:
        result (type): desc
    """

    if len(img.shape) > 2: 
        imgplot = plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')
        plt.show()
    
    else:
        imgplot = plt.imshow(img, cmap="gray", vmin=0, vmax=255)
        plt.title(title)
        plt.axis('off')
        plt.show()
        
    if (filename != None):
        plt.imsave(fname = filename + ".png", arr = img)


def imgcmp(img1, img2, title1 = None, title2 = None, filename = None):
    """ Description of this function.

    Args:
        img1 (numpy array): image array
        img2 (numpy array): image array
        title (string): image title
        filename (string): image filename

    Returns:
        result (type): desc
    """

    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    if len(img1.shape) > 2: 
        imgplot1 = plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
       
    else:
        imgplot1 = plt.imshow(img, cmap="gray", vmin=0, vmax=255)
    

    if len(img2.shape) > 2: 
        imgplot2 = plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    else:
        imgplot2 = plt.imshow(img, cmap="gray", vmin=0, vmax=255)
    


    fig, (imgplot1, imgplot2) = plt.subplots(1, 2)
    imgplot1.plot(x, y)
    imgplot2.plot(x, -y)
    plt.title(title2)
    plt.axis('off')
    plt.show()







img = cv.imread('./lenna.jpg', cv.IMREAD_COLOR)
img_gray = cv.imread('./lenna.jpg', cv.IMREAD_GRAYSCALE)

# imgview(img, title = "asas", filename="prueba")

imgcmp(img, img_gray, 'a', 'b')