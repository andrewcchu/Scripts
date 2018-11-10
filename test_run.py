# DEPENDENCIES: `pip install termcolor`

from subprocess import call
from termcolor import colored
import sys
import os

test_module = ''
test_runs = 0
counter = 1
success = True

while True:
	test_module = raw_input('Enter the name of the test module: ')
	test_module = os.getcwd() + '/' + test_module.strip()
	if os.path.isfile(test_module):
		break
	else:
		print colored('\nPlease enter a valid test module name', 'red'), colored(u'\u274C\n', 'red')

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
