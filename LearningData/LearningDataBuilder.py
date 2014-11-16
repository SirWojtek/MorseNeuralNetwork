from FontLoader import *
from LearningData import *

class LearningDataBuilder:

    def __init__(self, fontPath, fontSize, morseSize):
        self._morseSize = morseSize
        self._fontSize = fontSize
        self._fontLoader = FontLoader(fontPath, fontSize)
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

    def getLearningData(self):
        letters = self._fontLoader.getLetters()
        data = self._initLearningData(letters, self._morseSize)
        self._fillLearningData(data, letters)
        return data

    def _initLearningData(self, letters, morseSize):
        return LearningData(self._fontSize*self._fontSize, morseSize)

    def _fillLearningData(self, learningData, letters):
        for letter in letters:
            if letter in self._morseCode and len(self._morseCode[letter]) == self._morseSize:
                learningData.addLetter(letters[letter], self._morseCode[letter])
