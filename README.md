# Scripts

Collection of scripts for miscellaneous projects.

## test_run.py

The `test_run.py` script was created for running multiple test cases at a time (500) for the CS240 course at Purdue University, as a single test case failure resulted in a grade of 0. This script ensures code robustness and correct grade.

#### Dependencies

This script uses the python package `termcolor`.

To install, run `pip install termcolor`

#### Usage

* Place the python file into desired folder containing test executable
* Run `python test_run.py`

Alternatively, place the script in any directory and create an alias in your .bashrc to access from anywhere.
* Example: `alias confirm="python /homes/chu108/cs240/test_run.py"`
