# DEPENDENCIES: `pip install termcolor`

from subprocess import call
from termcolor import colored
import sys
import os


test_module = raw_input("Enter the name of the test module: ")
test_module = os.getcwd() + "/" + test_module.strip()
success = True
test_runs = 500
counter = 1

for i in range(test_runs):
	if call([test_module]) is 25:
		print colored('\nTEST CASE FAILED ON RUN #', 'red'), colored(`counter`, 'red'), colored(u'\u2717', 'red')
		print ("Exiting....")
		success = False
		break
	counter += 1

if success:
	print colored('\nALL TEST CASES PASSED! (', 'green'), colored(`counter-1`, 'green'), colored(')', 'green'), colored(u'\u2713', 'green')
