#1
import pathlib

path = pathlib.Path(__file__).parent.parent.parent

print(path)

#2
import pathlib as pl 

path = pl.Path(__file__).parent.parent

print(path)

#3
from pathlib import Path

path = Path(__file__)

print(path)