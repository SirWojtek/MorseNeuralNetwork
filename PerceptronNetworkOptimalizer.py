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

    def testLinSigLinNetworkWithChangingHiddenLayerNeurons(self, maxNeurons):
        for i in range(maxNeurons):
            net = self._networkBuilder.buildLinSigLinNetwork(i + 1)
            self._manager.setNetwork(net)
            (trainErr, valErr) = self._manager.trainWithParameters()
            eff = self.singleRun()
            print 'Network with %d hidden neurons has %f %% good predictions' % (i + 1, eff)
            print 'TrainingErr: %f\tValidationErr: %f' % (trainErr[-1], valErr[-1])

    def testLinSigLinNetworkWithoutBiasWithChangingHiddenLayerNeurons(self, maxNeurons):
        for i in range(maxNeurons):
            net = self._networkBuilder.buildLinSigLinNetworkWithoutBias(i + 1)
            self._manager.setNetwork(net)
            (trainErr, valErr) = self._manager.trainWithParameters()
            eff = self.singleRun()
            print 'Network with %d hidden neurons and bias has %f %% good predictions' % (i + 1, eff)
            print 'TrainingErr: %f\tValidationErr: %f' % (trainErr[-1], valErr[-1])

    def testWithChangingBackPropLearningrate(self, delta):
        i = delta

        while i < 1.0:
            self._manager.setHiddenLayerNeurons(15)
            (trainErr, valErr) = self._manager.trainWithParameters(learningRate = i)
            eff = self.singleRun()
            print 'Network with %f learning rate has %f %% good predictions' %(i, eff)
            print 'TrainingErr: %f\tValidationErr: %f' % (trainErr[-1], valErr[-1])
            i += delta

    def testWithChangingBackPropMomentum(self, delta):
        i = 0.0

        while i < 1.0:
            self._manager.setHiddenLayerNeurons(15)
            (trainErr, valErr) = self._manager.trainWithParameters(
                momentum = i)
            eff = self.singleRun()
            print 'Network with %f momentum has %f %% good predictions' %(i, eff)
            print 'TrainingErr: %f\tValidationErr: %f' % (trainErr[-1], valErr[-1])
            i += delta

    def testWithChangingBackPropWeightDecay(self, delta):
        i = 0.0

        while i < 1.0:
            self._manager.setHiddenLayerNeurons(15)
            (trainErr, valErr) = self._manager.trainWithParameters(
                weightDecay = i)
            eff = self.singleRun()
            print 'Network with %f weight decay has %f %% good predictions' %(i, eff)
            print 'TrainingErr: %f\tValidationErr: %f' % (trainErr[-1], valErr[-1])
            i += delta

    def singleRun(self):
        results = self._manager.runNetwork(self._testData['input'])
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
    opt = PerceptronNetworkOptimalizer()
    # opt.testLinSigLinNetworkWithChangingHiddenLayerNeurons(25)
    # opt.testLinSigLinNetworkWithoutBiasWithChangingHiddenLayerNeurons(25)
    # opt.testWithChangingBackPropLearningrate(0.1)
    # opt.testWithChangingBackPropMomentum(0.1)
    # opt.testWithChangingBackPropWeightDecay(0.1)

    # TODO: test high LR and lrcDelay < 1
    # TODO: test low LR and lrcDelay > 1
