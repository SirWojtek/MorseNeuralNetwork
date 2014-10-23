MorseNeuralNetwork
==================

Configuration

1. Install SciPy

On Linux this command should work:

sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

Take notice that line above also install couple of useful things like matplotlib.

2. Install pyBrain

PyBrain in included in this git repo as submodule in root of project in /pybrain folder. Before first use you must intall it:

cd pybrain
sudo python setup.py install

After this step you can use pybrain for running neural networks.
