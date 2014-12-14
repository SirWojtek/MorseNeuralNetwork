#!/usr/bin/python
from LearningData.FontLoader import *

def addNoise(letterMatrix, noiseSize, replace=1):
    tempMatrix = numpy.copy(letterMatrix)
    probabilities = list()
    # rand weight for each replacement bit
    for i, row in enumerate(tempMatrix):
        for j, bit in enumerate(row):
            if bit == replace:
                probabilities.append((numpy.random.random(), i, j))
    #sort weights descending
    probabilities.sort(reverse=True)
    #replace bits in matrix
    for item in probabilities[:noiseSize]:
        tempMatrix[item[1]][item[2]] = int(not(replace))
    return tempMatrix

def cut(letterMatrix, rowsToCut):
    tempMatrix = numpy.copy(letterMatrix)
    probabilities = list()
    for i in range(tempMatrix.shape[0]):
        probabilities.append((numpy.random.random(), i))
    probabilities.sort(reverse=True)
    for item in probabilities[:rowsToCut]:
        for i, bit in enumerate(tempMatrix[item[1]]):
            tempMatrix[item[1]][i] = 0
    return tempMatrix

class TestDataSet:

    def __init__(self, fontPath, fontSize, morseSize, dataSetSize):
        self._morseSize = morseSize
        self._fontSize = fontSize
        self._dataSetSize = dataSetSize
        self._letters = FontLoader(fontPath, fontSize).getLetters()
        self._morseCode = {
            'A' : (0, 1),       'B' : (1, 0, 0 ,0), 'C' : (1, 0, 1, 0),
            'D' : (1, 0 ,0),    'E' : (0,),         'F' : (0, 0, 1, 0),
            'G' : (1, 1, 0),    'H' : (0, 0, 0, 0), 'I' : (0, 0),
            'J' : (0, 1, 1, 0), 'K' : (1, 0, 1),    'L' : (0, 1, 0, 0),
            'M' : (1, 1),       'N' : (1, 0),       'O' : (1, 1, 1),
            'P' : (0, 1, 1, 0), 'Q' : (1, 1, 0, 1), 'R' : (0, 1, 0),
            'S' : (0, 0, 0),    'T' : (1,),         'U' : (0, 0, 1),
            'V' : (0, 0, 0, 1), 'W' : (0, 1 ,1),    'X' : (1, 0, 0, 1),
            'Y' : (1, 0, 1, 1), 'Z' : (1, 1, 0, 0),
        }

    def getLetters(self):
        letters = list()
        for letter in self._morseCode:
            if letter in self._morseCode and len(self._morseCode[letter]) == self._morseSize:
                letters.append(letter)
        return sorted(letters)

    def singleLetterWithNoise(self, letter, noise, replace=1):
        dataSet = list()
        for i in range(self._dataSetSize):
            dataSet.append((addNoise(self._letters[letter], noise, replace), self._morseCode[letter]))
        return dataSet

    def singleLetterNoNoise(self, letter):
        dataSet = list()
        for i in range(self._dataSetSize):
            dataSet.append((self._letters[letter], self._morseCode[letter]))
        return dataSet

    def singleLetterCut(self, letter, rowsToCut):
        if rowsToCut < 0 and rowsToCut > self._fontSize():
            raise ValueError('Row number to cut do not match font size!')
        dataSet = list()
        for i in range(self._dataSetSize):
            dataSet.append((cut(self._letters[letter], rowsToCut), self._morseCode[letter]))
        return dataSet

    def lettersWithNoise(self, letters, noise, replace=1):
        dataSet = list()
        for i in range(self._dataSetSize):
            data = dict()
            for letter in letters:
                data[letter] = (addNoise(self._letters[letter], noise, replace), self._morseCode[letter])
            dataSet.append(data)
        return dataSet

    def lettersNoNoise(self, letters):
        dataSet = list()
        for i in range(self._dataSetSize):
            data = dict()
            for letter in letters:
                data[letter] = self.singleLetterNoNoise(letter)
            dataSet.append(data)
        return dataSet

    def lettersCut(self, letters, rowsToCut):
        dataSet = list()
        for i in range(self._dataSetSize):
            data = dict()
            for letter in letters:
                data[letter] = (cut(self._letters[letter], rowsToCut), self._morseCode[letter])
            dataSet.append(data)
        return dataSet