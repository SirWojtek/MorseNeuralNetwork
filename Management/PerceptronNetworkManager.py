from Perceptron.PerceptronNetworkBuilder import *
from LearningData.LearningDataBuilder import *

class PerceptronNetworkManager:

    def __init__(self, fontPath, fontSize, morseSize):
        self._fontPath = fontPath
        self._fontSize = fontSize
        self._morseSize = morseSize
        self._initBuilders()
        self._data = self._dataBuilder.getLearningData()
        self._network = self._networkBuilder.buildSimpleNetwork()

    def _initBuilders(self):
        self._dataBuilder = LearningDataBuilder(self._fontPath, self._fontSize, self._morseSize)
        #It seems that fonts are not sized like 8x8 or 16x16 but 7x6 or 14x12
        self._networkBuilder = PerceptronNetworkBuilder(
            self._fontSize * self._fontSize, self._morseSize)

    def runNetwork(self):
        for data in self._data:
            self._network.run(data)
