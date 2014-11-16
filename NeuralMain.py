#!/usr/bin/python
from Management.PerceptronNetworkManager import *

def main():
    pass
    # fl = FontLoader('LearningData/fonts/pixelmix.ttf', 8)
    # fonts = fl.getLetters()
    # B = fonts[1]
    # morseB = (1,0,0,0)
    # print "Matrix loaded from font:"
    # print B

    # data = LearningData(LearningData.getLetterMatrixSize(B), len(morseB))
    # data.addLetter(B, morseB)
    # print "Contructed learning data object:"
    # print data

    # factory = PerceptronNetworkFactory(data.getInputSize(), data.getOutputSize())
    # net = factory.buildSimpleNetwork()
    # print "Neural network instance:"
    # print net

    # # only for testing purpose
    # letterTable = LearningData._convertToTable(B)
    # print "Network output with random weight:"
    # print net.runNetwork(letterTable)


if __name__ == '__main__':
    fontPath = 'LearningData/fonts/pixelmix.ttf'
    fontSize = 8
    morseSize = 4
    inputSet = [[0, 1, 1, 1, 0, 0, 0, 0,
                 1, 0, 0, 0, 1, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 1, 0, 0, 0, 1, 0, 0, 0,
                 0, 1, 1, 1, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0,
                 1, 0, 0, 0, 1, 0, 0, 0,
                 1, 0, 0, 0, 1, 0, 0, 0,
                 1, 1, 1, 1, 0, 0, 0, 0,
                 1, 0, 0, 0, 1, 0, 0, 0,
                 1, 0, 0, 0, 1, 0, 0, 0,
                 1, 1, 1, 1, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 0, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 1, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0]]
    manager = PerceptronNetworkManager(fontPath, fontSize, morseSize)
    manager.trainNetwork()
    result = manager.runNetwork(inputSet)
    print result