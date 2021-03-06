#!/usr/bin/python
from PerceptronNetwork import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import *

class PerceptronNetworkBuilder:

    def __init__(self, inputSize, outputSize):
        self._inputSize = inputSize
        self._outputSize = outputSize

    def buildSimpleNetwork(self, hiddenLayerNeurons):
        return PerceptronNetwork(
            buildNetwork(self._inputSize, hiddenLayerNeurons, self._outputSize))

    def buildLinSigLinNetwork(self, hiddenLayerNeurons = 15):
        return PerceptronNetwork(
            buildNetwork(self._inputSize, hiddenLayerNeurons, self._outputSize,
                hiddenclass = SigmoidLayer, outclass = LinearLayer))

    def buildLinSigLinNetworkWithoutBias(self, hiddenLayerNeurons):
        return PerceptronNetwork(
            buildNetwork(self._inputSize, hiddenLayerNeurons, self._outputSize,
                hiddenclass = SigmoidLayer, outclass = LinearLayer,
                bias = False, outputbias = False))

    # def _prepareNetwork(self, net, inLay, hidLay, outLay):
    #     self._prepareLayers(net, inLay, hidLay, outLay)
    #     self._prepareConnections(net, inLay, hidLay, outLay)
    #     net.sortModules()

    # def _prepareLayers(self, net, inLay, hidLay, outLay):
    #     net.addInputModule(inLay)
    #     net.addModule(hidLay)
    #     net.addOutputModule(outLay)

    # def _prepareConnections(self, net, inLay, hidLay, outLay):
    #     inToHidden = FullConnection(inLay, hidLay)
    #     hiddenToOut = FullConnection(hidLay, outLay)

    #     net.addConnection(inToHidden)
    #     net.addConnection(hiddenToOut)
