# Scripts

Collection of scripts for miscellaneous projects.

## slurm_scheduler.sh -- Slurm Job Scheduler Script with Dependency Management

This Bash script is designed to help users submit Slurm jobs and manage job dependencies efficiently. It allows users to submit an initial job and then schedule additional jobs with 'afterany' dependencies based on the initial job's completion or an existing job's completion. The script is flexible and accommodates both scenarios seamlessly.

### Usage

#### Command-line Options

- `-i <initial_job_script>`: Specify the initial job script to submit. This script will be the starting point for job submissions, and subsequent jobs will depend on it.
- `-e <existing_job_id>`: Specify an existing job ID to use as a dependency. If this option is used, the script will schedule additional jobs with 'afterany' dependencies on the specified existing job.
- `-s <script_to_schedule>`: Specify the script to schedule if using `-e`. This script will be submitted with 'afterany' dependencies when scheduling additional jobs based on an existing job.

#### Example Usage

1. Submit an initial job and two additional jobs with 'afterany' dependencies:
   ```
   ./slurm_scheduler.sh -i initial_job.sh
   ```

2. Use an existing job ID as a dependency and specify a script to schedule:
   ```
   ./slurm_scheduler.sh -e existing_job_id -s subsequent_job.sh
   ```

#### Job Scheduling Logic

- For the `-i` case, the script submits an initial job and then schedules two additional jobs with 'afterany' dependencies on the initial job.
- For the `-e` case, the script schedules one additional job with a 'afterany' dependency on either the existing job (if provided) or the previously submitted job.

### Error Handling

- The script includes error handling to check for invalid combinations of options and missing arguments.
- If both `-i` and `-e` options are used simultaneously, an error message is displayed, and usage instructions are shown.
- When using `-e`, the script checks that both an existing job ID and a script to schedule (`-s`) are provided; otherwise, an error message is displayed.

### Dependencies

- The script relies on the Slurm job scheduler (`sbatch`) for job submissions and dependencies.
  
## rush.py

`rush.py` is a simple script which generates a "rides list" - assigning potential new members brothers. It was created to aid me in my position as Rush Chairman at Sigma Chi at Purdue.

### Dependencies

**[Python](https://www.python.org/about/gettingstarted/)**

-   Python 3 (Created with v3.7.2)
    

### Usage

-   The script takes three parameters
    
    -   Path to a file for a `brothers.csv` file (containing names of brothers to assign PNMs to)
        
        -   Format of CSV should be a sole list (1 column of names)
            
    -   Path to a file for a `pnms.csv` file (containing names of PNMs)
        
        -   Format of CSV should be three columns: Name | Dorm | Phone Number
            
    -   Path to directory where created ride list should be placed
        
-   Optional flags
    
    -   `--randomize` determines if list should randomly distribute PNMs to brothers each time. (This may or may not be wanted depending on if you want drivers to develop a relationship with the PNMs they drive)
        

## test_run.py

The `test_run.py` script was created for running multiple test cases at a time for the CS240 course homework at Purdue University, as a single test case failure results in a grade of 0. This script ensures code robustness and the correct grade.

### Dependencies

Compatible versions of both Python and Pip pre-exist on Purdue CS machines.

**[Python](https://www.python.org/about/gettingstarted/)**

-   Python v2.7.15rc1+
    

**[Pip](https://pypi.org/project/pip/)**

-   Pip v9.0.1+
    
-   This script uses the python package `termcolor`.
    
    -   To install, run `pip install termcolor`
        

### Usage

-   Place the python file into desired homework folder containing test executable (SCP, PuTTY, etc.)
    
-   Run `python test_run.py`
    

Alternatively, place the script in any directory and create an alias in your `.bashrc` to access from anywhere.

-   Example: `alias confirm="python /homes/chu108/cs240/test_run.py"`
    

Once running, practical usage of the script should be self-explanatory.
