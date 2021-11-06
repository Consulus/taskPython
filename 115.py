import csv

def getValue():
    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)[1::]

    for i in rows:
        print(i[0])

getValue()        