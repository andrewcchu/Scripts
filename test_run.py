# DEPENDENCIES: `pip install termcolor`

from subprocess import call
from termcolor import colored
import sys
import os
import glob

test_module = ''
test_runs = 0
counter = 1
success = True

test_module = glob.glob("*_test")
if not test_module:
    print colored('No _test file found', 'red'), colored(u'\u274C\n', 'red')
    sys.exit();

test_module = test_module[0]
while True:
	test_runs = raw_input('Enter desired number of test case runs: ')
	try:
		test_runs = int(test_runs)
		break
	except:
		print colored('\nPlease enter valid number', 'red'), colored(u'\u274C\n', 'red')
		pass

for i in range(test_runs):
	if call([test_module]) is not 100:
		print colored('\nTEST CASE FAILED ON RUN #', 'red'), colored(`counter`, 'red'), colored(u'\u274C', 'red')
		print ('Exiting....')
		success = False
		break
	counter += 1

if success:
	print colored('\nALL TEST CASES PASSED! (', 'green'), colored(`counter-1`, 'green'), colored(')', 'green'), colored(u'\u2705', 'green')
