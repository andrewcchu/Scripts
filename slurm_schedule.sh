#!/bin/bash

# Initialize variables
initial_job_script=""
existing_job_id=""
script_to_schedule=""
previous_job_id=""

# Function to print usage and exit
print_usage() {
  echo "Usage: $0 [OPTIONS]"
  echo "Options:"
  echo "  -i <initial_job_script> : Specify the initial job script to submit."
  echo "  -e <existing_job_id>    : Specify an existing job ID to use as a dependency."
  echo "  -s <script_to_schedule> : Specify the script to schedule if using '-e'."
  exit 1
}

# Parse command-line options
while getopts "i:e:s:" opt; do
  case $opt in
    i)
      initial_job_script="$OPTARG"
      ;;
    e)
      existing_job_id="$OPTARG"
      ;;
    s)
      script_to_schedule="$OPTARG"
      ;;
    \?)
      print_usage
      ;;
  esac
done

# Check if both '-i' and '-e' are used at the same time
if [ -n "$initial_job_script" ] && [ -n "$existing_job_id" ]; then
  echo "Error: Please choose either '-i' or '-e', but not both."
  print_usage
fi

# Check if '-e' is used without both an existing job ID and a script to schedule
if [ -n "$existing_job_id" ] && [ -z "$script_to_schedule" ]; then
  echo "Error: When using '-e', please provide both an existing job ID and a script to schedule ('-s')."
  print_usage
fi

# Check if neither initial job script nor existing job ID is provided
if [ -z "$initial_job_script" ] && [ -z "$existing_job_id" ]; then
  print_usage
fi

# Submit three jobs with 'afterany' dependencies
for i in {1..3}; do
  dependency=""
  if [ -n "$existing_job_id" ]; then
    dependency="--dependency=afterany:$existing_job_id"
    if [ -n "$previous_job_id" ]; then
      dependency="--dependency=afterany:$previous_job_id"
    fi
    printf "sbatch $dependency $script_to_schedule\n"
    job_id=$(sbatch $dependency "$script_to_schedule" | awk '{print $4}')
    printf "Submitted job $job_id\n\n"
  elif [ -n "$initial_job_script" ]; then
    dependency=""
    if [ -n "$previous_job_id" ]; then
      dependency="--dependency=afterany:$previous_job_id"
    fi
    printf "sbatch $dependency $initial_job_script\n"
    job_id=$(sbatch $dependency "$initial_job_script" | awk '{print $4}')
    printf "Submitted job $job_id\n\n"
  fi
  previous_job_id=$job_id
done
