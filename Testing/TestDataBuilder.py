#!/usr/bin/python
from TestDataSet import *

class TestDataBuilder:

    def __init__(self, fontPath, fontSize, morseSize):
        self._fontPath = fontPath
        self._morseSize = morseSize
        self._fontSize = fontSize

    def getDataSet(self, numberOfData=1):
        return TestDataSet(self._fontPath, self._fontSize, self._morseSize, numberOfData)