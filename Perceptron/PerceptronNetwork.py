#!/usr/bin/python
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer


class PerceptronNetwork:

    def __init__(self, inputSize, hiddenLayerNeurons, outputSize):
        self._inputSize = inputSize
        self._outputSize = outputSize
        self._network = buildNetwork(self._inputSize,
            hiddenLayerNeurons, self._outputSize)

    def _roundResult(self, result):
        out = list()
        for value in result:
            temp = (int(round(value)))
            if temp > 1:
                temp = 1
            if temp < 0:
                temp = 0
            out.append(temp)
        return out

    def getInputSize(self):
        return self._inputSize

    def getOutputSize(self):
        return self._outputSize

    def getNetwork(self):
        return self._network

    def train(self, learningData):
        trainer = BackpropTrainer(self._network, learningData.getDataSet())
        trainer.trainUntilConvergence()

    def run(self, data):
        result = self._network.activate(data)
        return self._roundResult(result)

