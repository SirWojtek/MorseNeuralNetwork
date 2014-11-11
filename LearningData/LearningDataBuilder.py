from FontLoader import *
from LearningData import *

class LearningDataBuilder:

	def __init__(self, fontPath, fontSize):
		self._fontLoader = FontLoader(fontPath, fontSize)

	def getLearningData(self):
		letters = self._fontLoader.getLetters()
		morseDefault = (0,0,0,0)
		
		data = self._initLarningData(letters, len(morseDefault))
		self._fillLearningData(data, letters, morseDefault)

		return data
	
	def getMorseLength(self):
		return 4;

	def _initLarningData(self, letters, morseSize):
		return LearningData(LearningData.getLetterMatrixSize(
			letters[0]), morseSize)

	def _fillLearningData(self, learningData, letters, morseDefault):
		for letter in letters:
			print letter
			learningData.addLetter(letter, morseDefault)
