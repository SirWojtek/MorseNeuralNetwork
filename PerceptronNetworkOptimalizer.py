#!/usr/bin/python
from Management.PerceptronNetworkManager import *
from collections import Counter

class PerceptronNetworkOptimalizer:

    def __init__(self):
        fontPath = 'LearningData/fonts/pixelmix.ttf'
        fontSize = 8
        morseSize = 4
        self._manager = PerceptronNetworkManager(fontPath, fontSize, morseSize)
        self._testData = self._manager.getTrainingData().getDataSet()

    def testWithChangingHiddenLayerNeurons(self, maxNeurons):
        for i in range(maxNeurons):
            self._manager.setHiddenLayerNeurons(i)
            eff = self.singleRun()
            print 'Network with %d hidden neurons has %f good predictions' % (i, eff)

    def singleRun(self):
        self._manager.trainNetwork()
        results = self._manager.runNetwork(self._testData['input'])
        return self._computeResults(results)

    def _computeResults(self, results):
        goodPred = 0
        for i, data in enumerate(results):
            if self._compareLists(
                data, self._testData['target'][i]):
                goodPred += 1
        return float(goodPred) / len(results)

    def _compareLists(self, a, b):
        return Counter(a) == Counter(b)

if __name__ == '__main__':
    PerceptronNetworkOptimalizer().singleRun()
