import csv
import re
import argparse
from argparse import RawTextHelpFormatter
from collections import defaultdict
from random import shuffle
from datetime import datetime

# Parser definition and setup
parser = argparse.ArgumentParser(description='Script to generate rides list for Sigma Chi Rush @ Purdue University\nAndrew Chu - Summer 2019', formatter_class=RawTextHelpFormatter)
parser.add_argument('brothersCsvDir', type=str, help='Input path for brothers .csv file')
parser.add_argument('pnmCsvDir', type=str, help='Input path for PNMs .csv file')
parser.add_argument('outputDir', type=str, help='Output directory for the finished rides.csv file')
parser.add_argument('--randomize', default=0, help='Randomly assign rides versus sequentially (i.e. Brothers will not have the same PNMs assigned every time).\n--randomize=0 (Default; not randomized)\n--randomize=1 (Randomize list used for dictionary initialization)')
args = parser.parse_args()

# Function to build rides; dictionary with brother as key, list of pnms as value
def buildRides(brotherPath, newMemberPath, randomize):
	rides = defaultdict(list)
	pnms = []
	brothers = []
	brothersPath = brotherPath
	pnmPath = newMemberPath

	# Loop to give dictionaries keys, representing brothers' names
	with open (brothersPath, encoding='utf-8-sig') as bCsv:
		brothersCsv = csv.reader(bCsv, delimiter=',')
		for row in brothersCsv:
			brothers.append(row)

		if randomize != 0:
			shuffle(brothers)

		for brother in brothers:
			rides.update({str(brother):[]})

	# Add three PNMs to each list of key brother
	with open (pnmPath, encoding='utf-8-sig') as pCsv:
		pnmCsv = csv.reader(pCsv, delimiter=',')

		# Creates list of PNMs
		for row in pnmCsv:
			pnms.append(row)

		# Assigns 3 rides/brother
		pnmCount = len(pnms)
		counter = 0;
		for key in rides:
			tempList = rides.get(key)
			for pnm in range(0, 3):
				if counter == pnmCount:
					return rides
				else:
					tempList.append(pnms.pop())
					counter += 1

def main():
	# Pass in path as arguments 0 and 1 to function
	brotherPath = args.brothersCsvDir
	newMemberPath = args.pnmCsvDir
	outputDir = args.outputDir
	randomize = args.randomize

	# Dictionary of assigned rides
	rides = buildRides(brotherPath, newMemberPath, randomize)
	filename = 'rides_' + datetime.today().strftime('%m-%d-%Y') + '.csv'
	output = outputDir + filename

	# Write to csv file
	with open(output, mode='w', encoding='utf-8-sig') as rideCsv:
		csvWriter = csv.writer(rideCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		# Get list for each brother
		for key, value in rides.items():
			rideList = value
			counter = 0
			# Iterate through elements in list
			for element in rideList:
				if counter == 0:
					# Removes dictionary formatting for key and parses to string
					strKey = re.sub(r'[^\w]', ' ', str(key))
					csvWriter.writerow([strKey, element[0], element[1], element[2]])
				else:
					csvWriter.writerow(["", element[0], element[1], element[2]])
				counter += 1
main()