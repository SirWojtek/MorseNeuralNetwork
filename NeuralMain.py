#!/usr/bin/python
from pybrain.structure import FeedForwardNetwork
from FontLoader import *

def main():
	n = FeedForwardNetwork()
	fl = FontLoader('pixelmix.ttf', 8)
	fonts = fl.getLetters()
	A = fonts[0]

	print A

if __name__ == '__main__':
	main()
