#!/usr/bin/python
from pybrain.tools.shortcuts import buildNetwork

class PerceptronNetworkFactory:

	def __init__(self, inputSize, outputSize):
		self.inputSize = inputSize
		self.outputSize = outputSize

	def buildSimpleNetwork(self, hiddenLayerNeurons = 20):
		return buildNetwork(self.inputSize,
			hiddenLayerNeurons, self.outputSize)

