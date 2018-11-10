# Scripts

Collection of scripts for miscellaneous projects.

## test_run.py

The `test_run.py` script was created for running multiple test cases at a time for the CS240 course at Purdue University, as a single test case failure results in a grade of 0. This script ensures code robustness and the correct grade.

#### Dependencies

**[Python](https://www.python.org/downloads/release/python-2715rc1/)**

* Python v2.7.15rc1+

**Pip**

* sudo apt-get install python-pip
* This script uses the python package `termcolor`.
** To install, run `pip install termcolor`

#### Usage

* Place the python file into desired folder containing test executable
* Run `python test_run.py`

Alternatively, place the script in any directory and create an alias in your `.bashrc` to access from anywhere.
* Example: `alias confirm="python /homes/chu108/cs240/test_run.py"`
