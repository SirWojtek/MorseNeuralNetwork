#!/usr/bin/python
from pybrain.datasets import SupervisedDataSet

class LearningData:

    def __init__(self, inputSize, outputSize):
        self._inputSize = inputSize
        self._outputSize = outputSize
        self._dataset = SupervisedDataSet(inputSize, outputSize)

    def addLetter(self, letterMatrix, morseCode):
        letterTable = self.convertToTable(letterMatrix)
        self._checkForSizeError(len(letterTable), len(morseCode))
        self._dataset.addSample(letterTable, morseCode)

    def _checkForSizeError(self, letterTableLen, morseCodeLen):
        if letterTableLen != self._inputSize:
            raise RuntimeError("Size of letter different than size declared. Expect %d actual %d" % (self._inputSize, letterTableLen))
        if morseCodeLen != self._outputSize:
            raise RuntimeError("Size of morse code different than size declared. Expect %d actual %d" % (self.outputSize, morseCodeLen))

    def getInputSize(self):
        return self._inputSize

    def getOutputSize(self):
        return self._outputSize

    def getDataSet(self):
        return self._dataset

    @staticmethod
    def convertToTable(letterMatrix):
        letterTable = []
        for row in letterMatrix:
            letterTable.extend(row)
        return letterTable

    @staticmethod
    def getLetterMatrixSize(letterMatrix):
        count = 0
        for row in letterMatrix:
            count += len(row)
        return count

    def __iter__(self):
        return self._dataset.__iter__()

    def next(self):
        return self._dataset.next()
