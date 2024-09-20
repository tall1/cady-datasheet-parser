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
## To run:
With a python 3.10+ interpreter:
```commandline
python /path/to/main.py <path-to-folder-with-datasheets> <voltage-requirement> <temperature-requirement>
```
**Note**: voltage and temperature requirements can be either int or float. No need for measurement unit string (V or C etc.)