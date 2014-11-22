#!/usr/bin/python
from Management.PerceptronNetworkManager import *
from collections import Counter

class PerceptronNetworkOptimalizer:

    def __init__(self):
        fontPath = 'LearningData/fonts/pixelmix.ttf'
        fontSize = 8
        morseSize = 4
        self._manager = PerceptronNetworkManager(fontPath, fontSize, morseSize)
        self._networkBuilder = self._manager.getNetworkBuilder()
        self._testData = self._manager.getTrainingData().getDataSet()

    def testWithChangingHiddenLayerNeurons(self, maxNeurons):
        for i in range(maxNeurons - 1):
            self._manager.setHiddenLayerNeurons(i + 1)
            self._manager.trainNetwork()
            eff = self.singleRun()
            print 'Network with %d hidden neurons has %f %% good predictions' % (i, eff)

    def testLinSigLinNetworkWithChangingHiddenLayerNeurons(self, maxNeurons):
        for i in range(maxNeurons):
            net = self._networkBuilder.buildLinSigLinNetwork(i + 1)
            self._manager.setNetwork(net)
            self._manager.trainNetwork()
            eff = self.singleRun()
            print 'Network with %d hidden neurons has %f %% good predictions' % (i + 1, eff)

    def testWithChangingBackPropLearningrate(self, delta):
        i = delta

        while i <= 1.0:
            self._manager.trainWithParameters(learningRate = i)
            eff = self.singleRun()
            print 'Network with %f learning rate has %f %% good predictions' %(i, eff)
            i += delta

    def testWithChangingBackPropMomentum(self, delta):
        i = 0.0

        while i <= 1.0:
            self._manager.trainWithParameters(momentum = i)
            eff = self.singleRun()
            print 'Network with %f momentum has %f %% good predictions' %(i, eff)
            i += delta

    def testWithChangingBackPropWeightDecay(self, delta):
        i = 0.0

        while i <= 1.0:
            self._manager.trainWithParameters(momentum = i)
            eff = self.singleRun()
            print 'Network with %f weight decay has %f %% good predictions' %(i, eff)
            i += delta

    def singleRun(self):
        results = self._manager.runNetwork(self._testData['input'])
        self._manager.resetNetwork()
        return self._computeResults(results) * 100

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
    PerceptronNetworkOptimalizer().testWithChangingBackPropWeightDecay(0.1)
