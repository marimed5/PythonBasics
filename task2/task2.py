import os
import csv
import random
import re

#Reading and printing
filename = 'data/sample.txt'

try:
    with open(filename, 'r') as f:
        #Read and print
        print("\tPrinting full contents of file:")
        for line in f:
            print(line, end='')

        f.seek(0)
        print("\tPrinting first 20 characters of file:")
        first20 = f.read(20)
        print(first20)

        f.seek(0)
        print("\tPrinting first line:")
        first_line = f.readline()
        print(first_line, end='')

        f.seek(0)
        print("\tPrinting all lines as a list:")
        list_lines = f.readlines()
        print(list_lines)

        #Writing to new file
        f.seek(0)
        file = open('copy_target.txt', 'w')
        for line in f:
            file.write(line)

except FileNotFoundError:
    print("File not found")


#Renaming files
os.chdir('data/reports/')

for f in os.listdir():
    try:
        f_name, f_ext = os.path.splitext(f)
        f_header, f_num = f_name.split('-')

        newfile = '{}_{}{}'.format(f_header.capitalize(), f_num.zfill(2), f_ext)
        os.rename(f, newfile)
    except ValueError:
        pass

os.chdir('../..')

#Parsing CSV files

file = 'data/people.csv'

# Random greetings
greetings = ["Hi", "Hello", "Howdy", "Hey", "Bonjour"]

try:
    with open(file) as csvfile:

        f = open('greetings.csv', 'w')
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        print("Printing each name and email:")
        for row in csv_reader:
            print(row['name'])
            print(row['email'])
            f.write(random.choice(greetings) + ", " + row['name'] + "!\n")

except FileNotFoundError:
    print("File not found")

#Regex
with open(file) as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    print("\nShowing usernames before @: ")
    for row in csv_reader:
        pattern = re.compile(r"(\w+)@")
        matches = pattern.findall(row['email'])
        for match in matches:
            print(match)

