# pip vs conda
`pip` and `conda` are package manager for Python.
They allow to 

## pip
Make sure you have the latest pip
```shell
pip3 install --upgrade pip
```

(Using `pip` instead of `pip3` should work if you don't have Python 2.)

## Conda / Mamba

Anaconda

>mamba: a Python-based CLI conceived as a drop-in replacement for conda, 
offering higher speed and more reliable environment solutions

I prefer `mamba`.


## how to use them 
- Note mixing channels/manager
## virtual envs
I would highly recommend using virtual environment.

Note: You do not need to this on Google Colab as it creates a Linux instance every time you launch it,
but more on that later.

### venv
I personally have never used the `venv` to create a virtual environment, but you can
read up on it [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

### Conda
I have only used the `conda`/`mamba` virtual environment manager as I prefer it.

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

### Local / colab
You can either run jupyter locally on your computer, or you can use Google Colab.
However, Colab comes with some caveat, you are limited in runtime, it now runs Python 3.10 (no easy way to change it),
and the terminal access is granted through the Pro version.