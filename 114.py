import csv

def enterPeriod():
    ageStart = input("Please enter the start year: ")

    while not ageStart.isdigit():
        ageStart = input("Please enter the start year: ")

    ageEnd = input("Please enter the end Year: ")

    while not ageEnd.isdigit():
        ageEnd = input("Please enter the start year: ")

    return (ageStart, ageEnd)

def getBooksByYear():
    ask = enterPeriod()

    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)[1::]

    result = []

    for i in rows:
        if int(i[3]) >= int(ask[0]) and int(i[3]) <= int(ask[1]):
            result.append(i)

    if len(result) == 0:
        print("In this period we not have books")
    else:
        for j in result:
            print(j)

getBooksByYear()                        