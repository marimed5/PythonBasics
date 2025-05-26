File Handling, CSV Parsing, and File Renaming

Task Description:
You are given a folder with text files and a CSV file. Complete the following:

Read from a file:
    Open sample.txt using a context manager.

Read and print:
    The full content.
    First 20 characters.
    First line.
    All lines as a list.

Write and copy:
    Copy the contents of sample.txt to copy_target.txt using read/write in a context manager.

Rename files:
    Inside the same directory, files are named like report-1.txt, report-2.txt, etc.
    Rename them to Report_01.txt, Report_02.txt, etc.

Parse CSV file:
    Read people.csv using csv.DictReader.
    Print each name and email.

Generate random greeting emails:
    Randomly assign each person in people.csv a greeting (Hi, Hello, Hey).
    Save this to a new CSV file greetings.csv.

Regex (Bonus):
    Use regex to extract all email usernames (before the '@') from people.csv.

