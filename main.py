#!/usr/bin/python

import urllib.request
import sys
import os
import getopt
from datetime import date
from dotenv import load_dotenv, dotenv_values

def create_data(day, year='2022'):

    env = load_dotenv()
    if(not load_dotenv() or not dotenv_values('.env')['COOKIE']):
        sys.exit("Error loading session id")

    request = urllib.request.Request(f"https://adventofcode.com/{year}/day/{day}/input")
    request.add_header('cookie', dotenv_values('.env')['COOKIE'])

    try:
        with urllib.request.urlopen(request) as response:
            data = response.read().decode('utf-8').strip()
    except:
        sys.exit('Error fetching data')

    folder_name = f"day{day.rjust(2, '0')}"

    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except:
        sys.exit('Error creating folder')

    try:
        with open(f"{folder_name}/input.txt", 'w') as file:
            file.write(data)

        lines = ["with open('input.txt', 'r') as file:\n", "\tdata = [line for line in file.read().split('\\n')]\n\n"]

        if not os.path.exists(f"{folder_name}/part1.py"):
            with open(f"{folder_name}/part1.py", "w") as file:
                file.writelines(lines)

        if not os.path.exists(f"{folder_name}/part2.py"):
            with open(f"{folder_name}/part2.py", "w") as file:
                file.writelines(lines)
    except:
        sys.exit('Error writing file')

def main(argv):
    try:
        opts, _ = getopt.getopt(argv, "hd:")
    except:
        print('Usage: -d <day>')
        sys.exit()

    if opts:
        create_data(opts[0][1])
    else:
        create_data(str(date.today().day))

if __name__ == "__main__":
    main(sys.argv[1:])