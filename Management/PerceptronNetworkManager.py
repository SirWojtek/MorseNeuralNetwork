from Perceptron.PerceptronNetworkBuilder import *
from LearningData.LearningDataBuilder import *

class PerceptronNetworkManager:

	def __init__(self, fontPath, fontSize):
		self._initBuilders(fontPath, fontSize)

		self._data = self._dataBuilder.getLearningData()
		self._network = self._networkBuilder.buildSimpleNetwork()

	def _initBuilders(self, fontPath, fontSize):
		self._dataBuilder = LearningDataBuilder(fontPath, fontSize)
		self._networkBuilder = PerceptronNetworkBuilder(
			fontSize * fontSize, self._dataBuilder.getMorseLength())

	def runNetwork(self):
		for data in self._data:
			self._network.run(data)
