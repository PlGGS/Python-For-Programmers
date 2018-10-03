def estimatePi(percentError):
    '''Estimates the value of pi to '''
    #if two values are smaller than the percentError, we return
    denominator = 3
    old = 4/1
    new = 4 - 4/denominator
    factor = -1
    while (abs(old - new) > percentError):
        old = new
        denominator += 2
        factor = -factor
        new += factor*(4/denominator)
    return round(old, len(str(percentError)))

import PIL.Image

def copyImageToGreyscale(img):
    '''Copies an image to a greyscale'''
    width, height = img.size
    res = PIL.Image.new(img.mode, img.size)
    for i in range(0, width):
        for o in range(0, height):
            pix = img.getpixel((i,o)) #Takes a tuple
            average = (pix[0] + pix[1] + pix[2]) / 3
            res.putpixel((i, j), (average, average, average))
        pass
