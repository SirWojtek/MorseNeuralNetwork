#!/usr/bin/python
from pybrain.tools.shortcuts import buildNetwork

class PerceptronNetwork:

	def __init__(self, inputSize, hiddenLayerNeurons, outputSize):
		self._inputSize = inputSize
		self._outputSize = outputSize
		self._network = buildNetwork(self._inputSize,
			hiddenLayerNeurons, self._outputSize)

	def getInputSize(self):
		return self._inputSize

	def getOutputSize(self):
		return self._outputSize

	def getNetwork(self):
		return self._network

	def run(self, inputData):
		return self._network.activate(inputData)