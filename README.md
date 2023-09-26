# Installation

First clone this repository on your machine.  
In the terminal in the folder you desire do the following:

Please ask if you don't know how to use the terminal.

```shell
git clone https://github.com/ai4er-cdt/induction-jupyter.git
```

# pip vs conda
`pip` and `conda` are package manager for Python.
They allow to install packages.

## pip
If you want to use pip, make sure you have the latest pip
```shell
pip3 install --upgrade pip
```

(Using `pip` instead of `pip3` should work if you don't have Python 2.)

## Conda / Mamba

Anaconda is another package and environment manager

>mamba: a Python-based CLI conceived as a drop-in replacement for conda, 
offering higher speed and more reliable environment solutions

I prefer `mamba` as it is lighter.

## how to use them 
When doing a project it is better to keep to one package manager to install everything.
Of course, it will come a time when your project in conda needs a package that's only available through pip.
In this case it is fine to install it with pip, but try to do it for every other packages.  
What I like to do is install all the pip dependencies at the end.

## virtual envs
I would highly recommend using virtual environment, as it packages all the dependencies 
for a project and avoid having a mess of different version.

Note: You do not need to this on Google Colab as it creates a Linux instance every time you launch it,
but more on that later.

### venv
I personally have never used the `venv` to create a virtual environment, but you can
read up on it [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

### Conda
I have only used the `conda`/`mamba` virtual environment manager as I prefer it.
For this workshop you can simply do the following:

```shell
conda env create -f environment.yaml
```

```shell
conda activate ai4er-ws
```

Now this is the explanation if you wanted to do it from scratch.
```shell
conda create -n $name python=3.11
```

Where `$name` is the name of the environment (do NOT use spaces).

Then you will need to activate the environment:
```shell
conda activate $name
```

# Installing Jupyter

## pip

```shell
pip3 install jupyter
```

## Conda

```shell
conda install jupyter
```


# Opening the notebook
## Start a server
To use jupyter notebook you need to first launch the jupyter server.  
In a terminal (with the correct environment activated):
```shell
jupyter notebook
```
(To stop simply type `Ctrl + c` in the terminal).  

Now open your browser and go to `http://localhost:8888`

If you are using Colab will do all that for you.

### Local vs colab
You can either run jupyter locally on your computer, or you can use Google Colab.
However, Colab comes with some caveat, you are limited in runtime, it now runs Python 3.10 (no easy way to change it),
and the terminal access is granted through the Pro version.