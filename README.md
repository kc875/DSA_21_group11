# DSA Fall 2021 Group 11: Pivot Selection Project

## Members

**Kimberly Chang**

kc875

kc875@scarletmail.rutgers.edu

**Samuel Cho**

sc1724

sc1724@scarletmail.rutgers.edu

## Running the Code

Please download the data for this project at [this Google Drive link](https://drive.google.com/file/d/1J7ortUAc5YMFgLPUfwafLwIinJbW569-/view?usp=sharing).
Ensure the data is organized such that the downloaded data folder, which contains 2 subfolders, is in the project directory.

Alternatively, the entire project with the data can be downloaded at [this other Google Drive link](https://drive.google.com/file/d/1c34VQyzTp3SB_BkwbHz_1tbkRuB5BH4N/view?usp=sharing).
(This is recommended.)

As another alternative, data can be generated using the [`createlist.py` file](createlist.py). 
(This is not recommended.)


Run this project using the [`quicksort.py` file](quicksort.py). 
It does not need to be compiled. 
There are no program inputs.
It can be run with an instruction such as `python3 quicksort.py` from the project directory. 
This will generate output files, which contain the mean and standard deviation of testing the project on the randomly ordered list files from the downloaded data.

Alternatively, this project can be run in a separate Python file by importing the [`quicksort.py` file](quicksort.py) and using the `quicksort_from_file(filename, sort_type)` function.
The `sort_type` should be a number from 0 to 2, which corresponds to:
* 0 is the first element pivot selection
* 1 is the median of three pivot selection
* 2 is the random pivot selection