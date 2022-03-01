14.02
import random
from time import sleep
def generator():
    k = random.randint(0, 10)
    while True:
        k = k + 10
        sleep(2)
        yield  k

g = generator()
for i in g:
    print(i)
print(next(g))

#14.04
import sys
import csv

import argparse
print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name',
required=True)
parser.add_argument('-ln', '--last-name',
required=True)
parser.add_argument('-age' '--age-age',
required=True)
parser.add_argument('echo')
args = parser.parse_args()
print(args)
print('First name:', args.first_name)
print('Last name:', args.last_name)
print('Age', args.age)
print('echo:', args.echo)
with open("file.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Имя", "Фамилия", "Возраст"])

