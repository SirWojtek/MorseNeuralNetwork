#!/usr/bin/python
from PIL import Image, ImageFont
import numpy
import string

class FontLoader:

    def __init__(self, fontPath, arraySize):
        self.fontPath = fontPath
        self.arraySize = arraySize

    def getLetters(self):
        letters = list();
        font = ImageFont.truetype(self.fontPath, self.arraySize)
        '''Just uppercase for now'''
        for char in string.uppercase:
            im = Image.Image()._new(font.getmask(char))
            binaryLetter = numpy.where(numpy.array(im)>0, 1, 0)
            letters.append(binaryLetter)
        return letters

if __name__ == '__main__':
    fl = FontLoader('pixelmix.ttf', 8)
    letters = fl.getLetters()
    for letter in letters:
        print letter
        print '\n'