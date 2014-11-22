#!/usr/bin/python
from Management.PerceptronNetworkManager import *
from Testing.TestDataBuilder import *

def testDataBuilderEq(fontPath, fontSize, morseSize):
    tdb = TestDataBuilder(fontPath, fontSize, morseSize)

    # Get single test data for single letter
    # will return one element list. Where first element is tuple
    # with letter bit matrix and morse code
    print '1. Single test single letter'
    testData = tdb.getDataSet().singleLetterWithNoise('B', 2)
    print testData

    # Get multiple test data for single letter
    # will return multiple element list. Where each element is tuple
    # with letter bit matrix and morse code
    print '\n2. Multiple test single letter'
    testData = tdb.getDataSet(2).singleLetterCut('B', 'up', 3)
    print testData

    # Get single test data for multiple letters
    # will return one element list. Where first element is dictionary
    # where each key is a letter character eg. 'B'
    # and value for each key is a tuple with letter bit matrix and morse code
    print '\n3. Single test multiple letters'
    testData = tdb.getDataSet().lettersCut(['B', 'D'], 'up', 2)
    print testData


if __name__ == '__main__':
    fontPath = 'LearningData/fonts/pixelmix.ttf'
    fontSize = 8
    morseSize = 4
    inputSet = [[[0, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]],
                [[1, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [1, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [1, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]],
                [[1, 1, 1, 1, 1, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]]
    manager = PerceptronNetworkManager(fontPath, fontSize, morseSize)
    manager.trainNetwork()
    result = manager.runNetwork(inputSet)
    print result