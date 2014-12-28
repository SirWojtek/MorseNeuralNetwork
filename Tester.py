#!/usr/bin/python
from Management.PerceptronNetworkManager import *
from Testing.TestDataBuilder import *
from collections import Counter


class Tester:

    def __init__(self):
        self._fontPath = 'LearningData/fonts/pixelmix.ttf'
        self._fontSize = 8
        self._morseSize = 4
        print 'Start network training. fontPath: ' + self._fontPath + ', fontSize: ' + str(self._fontSize) + ', morseSize: ' + str(self._morseSize)
        self._networkManager = PerceptronNetworkManager(self._fontPath, self._fontSize, self._morseSize)
        self._networkManager.trainWithParameters()
        print 'Network training success'

    def toCsv(self, path, data):
        file = open(path, 'w+')
        file.write('letter,noise,all,correct,wrong,%\n')
        for letter in data:
            for noise in data[letter]:
                correct = data[letter][noise]['correct']
                wrong = data[letter][noise]['wrong']
                all = correct + wrong
                proc = correct * 100 / all
                file.write(letter + ',' + str(noise) + ',' + str(all) + ',' + str(correct) + ',' + str(wrong) + ',' +  str(proc) + '\n')
        file.close()

    def scenarioWithRandomNoise(self, maxNoiseSize, maxDataSize, replace = 1):
        print 'Start scenario with random noise'
        print 'Preparing test data'
        testDataBuilder = TestDataBuilder(self._fontPath, self._fontSize, self._morseSize)
        letters = testDataBuilder.getDataSet().getLetters()
        results = self._createResults(maxNoiseSize, letters)
        print 'Test data ready'
        print 'Start test:'
        for noise in range(maxNoiseSize):
            testDataSet = testDataBuilder.getDataSet(maxDataSize).lettersWithNoise(letters, noise, replace)
            self.testNetwork(testDataSet, results, noise)
            print str((noise+1)*100/maxNoiseSize) + '%'
        return results

    def scenarioWithRandomCut(self, maxRowsToCut, maxDataSize):
        print 'Start scenario with random  rows cut'
        print 'Preparing test data'
        testDataBuilder = TestDataBuilder(self._fontPath, self._fontSize, self._morseSize)
        letters = testDataBuilder.getDataSet().getLetters()
        results = self._createResults(maxRowsToCut, letters)
        print 'Test data ready'
        print 'Start test:'
        for noise in range(maxRowsToCut):
            testDataSet = testDataBuilder.getDataSet(maxDataSize).lettersCut(letters, noise)
            self.testNetwork(testDataSet, results, noise)
            print str((noise+1)*100/maxRowsToCut) + '%'
        return results

    def testNetwork(self, testDataSet, results, noise):
        for data in testDataSet:
            for letter in data:
                result = self._networkManager.runNetworkOnce(data[letter][0])
                if result == data[letter][1]:
                    results[letter][noise]['correct'] += 1
                else:
                    results[letter][noise]['wrong'] += 1

    def _createResults(self, maxNoiseSize, letters):
        results = dict.fromkeys(letters);
        for letter in results:
            results[letter] = dict.fromkeys(range(maxNoiseSize))
            for noise in results[letter]:
                results[letter][noise] = {'correct' : 0, 'wrong' : 0}
        return results

if __name__ == '__main__':
    tester = Tester()
    result = tester.scenarioWithRandomNoise(10, 1000)
    tester.toCsv('test1.csv', result)
    result = tester.scenarioWithRandomNoise(10, 1000, 0)
    tester.toCsv('test2.csv', result)
    result = tester.scenarioWithRandomCut(8, 1000)
    tester.toCsv('test3.csv', result)
