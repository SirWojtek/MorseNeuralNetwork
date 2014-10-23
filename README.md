MorseNeuralNetwork
==================

<h4>Configuration</h4>

<h5>1. Install SciPy</h5>

On Linux this command should work:

sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

Take notice that line above also install couple of useful things like matplotlib.

<h4>2. Install pyBrain</h4>

PyBrain in included in this git repo as submodule in root of project in /pybrain folder. Before first use you must intall it:

cd pybrain
sudo python setup.py install

After this step you can use pybrain for running neural networks.
