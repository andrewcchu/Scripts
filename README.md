# Scripts

Collection of scripts for miscellaneous projects.

## test_run.py

The `test_run.py` script was created for running multiple test cases at a time for the CS240 course homework at Purdue University, as a single test case failure results in a grade of 0. This script ensures code robustness and the correct grade.

### Dependencies

Compatible versions of both Python and Pip pre-exist on Purdue CS machines.

**[Python](https://www.python.org/downloads/release/python-2715rc1/)**

* Python v2.7.15rc1+

**[Pip](https://pypi.org/project/pip/)**

* Pip v9.0.1+
* This script uses the python package `termcolor`.
  * To install, run `pip install termcolor`
  
### Usage

* Place the python file into desired homework folder containing test executable (SCP, PuTTY, etc.)
* Run `python test_run.py`

Alternatively, place the script in any directory and create an alias in your `.bashrc` to access from anywhere.
* Example: `alias confirm="python /homes/chu108/cs240/test_run.py"`

Once running, practical usage of the script should be self-explanatory.
