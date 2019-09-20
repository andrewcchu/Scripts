import argparse
from argparse import RawTextHelpFormatter

luke = 0.35
mitch = 0.15
andrew = 0.5

parser = argparse.ArgumentParser(description='Script to split up costs for groceries', formatter_class=RawTextHelpFormatter)
parser.add_argument('totalCost', type=float, help='Total cost for groceries')
args = parser.parse_args()

def main():
    cost = args.totalCost
    result = "Luke: $" + (str)(cost * luke) + "\n" + "Mitch: $" + (str)(cost * mitch) + "\n" + "Andrew: $" + (str)(cost * andrew) + "\n"
    print(result)
main()
