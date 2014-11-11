#!/usr/bin/python
from Management.PerceptronNetworkManager import *

def main():
	# fl = FontLoader('LearningData/fonts/pixelmix.ttf', 8)
	# fonts = fl.getLetters()
	# B = fonts[1]
	# morseB = (1,0,0,0)
	# print "Matrix loaded from font:"
	# print B

	# data = LearningData(LearningData.getLetterMatrixSize(B), len(morseB))
	# data.addLetter(B, morseB)
	# print "Contructed learning data object:"
	# print data

	# factory = PerceptronNetworkFactory(data.getInputSize(), data.getOutputSize())
	# net = factory.buildSimpleNetwork()
	# print "Neural network instance:"
	# print net

	# # only for testing purpose
	# letterTable = LearningData._convertToTable(B)
	# print "Network output with random weight:"
	# print net.runNetwork(letterTable)

	manager = PerceptronNetworkManager(
		'LearningData/fonts/pixelmix.ttf', 8)
	manager.runNetwork()


if __name__ == '__main__':
	main()
