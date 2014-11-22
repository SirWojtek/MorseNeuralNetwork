#!/usr/bin/python
from PIL import Image, ImageFont
import numpy
import string

class FontLoader:

    def __init__(self, fontPath, arraySize):
        self._fontPath = fontPath
        self._arraySize = arraySize

    def getLetters(self):
        letters = dict();
        font = ImageFont.truetype(self._fontPath, self._arraySize)
        '''Just uppercase for now'''
        for char in string.uppercase:
            im = Image.Image()._new(font.getmask(char))
            binaryLetter = numpy.where(numpy.array(im)>0, 1, 0)
            letters[char] = self._resize(binaryLetter)
        return letters

    def _resize(self, letterArray):
        letter = letterArray.copy()
        widthDiff = self._arraySize - len(letter)
        heightDiff = self._arraySize - len(letter[0])
        if heightDiff > 0:
            for i in range(0, heightDiff):
                letter = numpy.hstack((letter, [[0]]*len(letter)))
        if widthDiff > 0:
            for i in range(0, widthDiff):
                letter = numpy.vstack((letter, [0]*len(letter[0])))
        return letter
