#!/usr/bin/python
from pybrain.supervised.trainers import BackpropTrainer

class PerceptronNetwork:

    def __init__(self, network):
        self._network = network

    def _roundResult(self, result):
        out = list()
        for value in result:
            temp = (int(round(value)))
            if temp > 1:
                temp = 1
            if temp < 0:
                temp = 0
            out.append(temp)
        return tuple(out)

    def getNetwork(self):
        return self._network

    def train(self, learningData):
        trainer = BackpropTrainer(self._network, learningData.getDataSet())
        trainer.trainUntilConvergence()

    def reset(self):
        self._network.reset()

    def run(self, data):
        result = self._network.activate(data)
        return self._roundResult(result)

