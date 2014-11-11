#!/usr/bin/python
from PerceptronNetwork import *

class PerceptronNetworkBuilder:

	def __init__(self, inputSize, outputSize):
		self._inputSize = inputSize
		self._outputSize = outputSize

	def buildSimpleNetwork(self, hiddenLayerNeurons = 20):
		return PerceptronNetwork(self._inputSize,
			hiddenLayerNeurons, self._outputSize)
