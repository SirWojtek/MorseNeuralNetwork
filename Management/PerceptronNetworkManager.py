from Perceptron.PerceptronNetworkBuilder import *
from LearningData.LearningDataBuilder import *

class PerceptronNetworkManager:

    def __init__(self, fontPath, fontSize, morseSize):
        self._fontPath = fontPath
        self._fontSize = fontSize
        self._morseSize = morseSize
        self._initBuilders()
        self._learningData = self._dataBuilder.getLearningData()
        self._network = self._networkBuilder.buildSimpleNetwork()

    def _initBuilders(self):
        self._dataBuilder = LearningDataBuilder(self._fontPath, self._fontSize, self._morseSize)
        self._networkBuilder = PerceptronNetworkBuilder(
            self._fontSize * self._fontSize, self._morseSize)

    def trainNetwork(self):
        self._network.train(self._learningData)

    def runNetworkOnce(self, inputData):
        return self._network.run(inputData)

    def runNetwork(self, inputDataSet):
        outputSet = list()
        for data in inputDataSet:
            result = self.runNetworkOnce(data)
            outputSet.append(result)
        return outputSet