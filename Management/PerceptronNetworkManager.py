from Perceptron.PerceptronNetworkBuilder import *
from LearningData.LearningDataBuilder import *
from LearningData.LearningData import *
from pybrain.supervised.trainers import BackpropTrainer

class PerceptronNetworkManager:

    def __init__(self, fontPath, fontSize, morseSize):
        self._fontPath = fontPath
        self._fontSize = fontSize
        self._morseSize = morseSize
        self._initBuilders()
        self._learningData = self._dataBuilder.getLearningData()
        self._network = self._networkBuilder.buildLinSigLinNetwork()

    def _initBuilders(self):
        self._dataBuilder = LearningDataBuilder(self._fontPath, self._fontSize, self._morseSize)
        self._networkBuilder = PerceptronNetworkBuilder(
            self._fontSize * self._fontSize, self._morseSize)

    def _isMatrix(self, data):
        try:
            data[0][0]
            return True
        except IndexError:
            return False

    def setHiddenLayerNeurons(self, hiddenLayerNeurons):
        self._network = self._networkBuilder.buildSimpleNetwork(hiddenLayerNeurons)

    def setNetwork(self, network):
        self._network = network

    def resetNetwork(self):
        self._network.reset()

    def getNetworkBuilder(self):
        return self._networkBuilder

    def getTrainingData(self):
        return self._learningData

    def trainWithParameters(self, learningRate = 0.2,
        momentum = 0.0, weightDecay = 0.0):
        trainer = BackpropTrainer(self._network.getNetwork(),
            learningrate = learningRate,
            momentum = momentum, weightdecay = weightDecay)
        return trainer.trainUntilConvergence(trainingData=self._learningData.getDataSet(),
            validationData=self._learningData.getDataSet())

    def runNetworkOnce(self, inputData):
        return self._network.run(inputData)

    def runNetwork(self, inputDataSet):
        outputSet = list()
        for data in inputDataSet:
            if self._isMatrix(data):
                result = self.runNetworkOnce(LearningData.convertToTable(data))
            else:
                result = self.runNetworkOnce(data)
            outputSet.append(result)
        return outputSet