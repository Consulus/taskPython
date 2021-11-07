import csv

def getValue():
    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    for i in rows:
        print(i)

def deleteRow():
    delRow = input("Enter number of row to delete: ")
    while not delRow.isdigit():
        delRow = input("Enter the number of record you want to change: ")

    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)[1::]
    newRow = list(filter(lambda x: x[0] != delRow, rows ))
    
    file = open("Books.csv", "w")
    x = 0
    for j in newRow:
        newRec = str(x) + "," + j[1] + "," + j[2] + "," + j[3] + "\n"
        file.write(newRec)
        x = x + 1
    file.close()    

def changeRec():

    getValue()

    num = input("Enter the number of record you want to change: ")
    while not num.isdigit():
        num = input("Enter the number of record you want to change: ")
    
    