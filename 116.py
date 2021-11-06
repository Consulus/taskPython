import csv

def getValue():
    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    for i in rows:
        print(i)