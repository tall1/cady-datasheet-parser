# Cady datasheet parser:
## Description
Python program that parses component datasheets files in a given folder.
Parses voltage and temperature ranges.

Recieves: 
- folder path to datasheets
- voltage requirement
- temperature requirement

Prints:
- All the components (by file name) that match the requested voltage and temperature.

## Prerequisits:

- python 3.10+ interpreter

## To run:

With a python 3.10+ interpreter:
```commandline
python ./main.py <path-to-folder-with-datasheets> <voltage-requirement> <temperature-requirement>
```
### Important Notes: 
- voltage and temperature requirements - int or float
- path to folder - absolute path only!