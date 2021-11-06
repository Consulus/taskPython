import csv

def askToAdd():
    ask = input("How many books you want add?")    
    
    while not ask.isdigit():
        ask = input("How many books you want add? ")
    
    return ask



def getValue():
    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    for i in rows:
        print(i)

def getLastNumberList():
    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    return int(rows[-1][0])

def addValueToList():
    file = open("Books.csv", "a")
    name = input("Name of book: ")
    author = input("Author of book: ")
    year = input("Year of book: ")
    
    num = getLastNumberList() + 1
    
    newRecord = str(num) + "," + name + "," + author + "," + year + "\n"
    file.write(str(newRecord))
    file.close()

def addFewValueToList():
    num = int(askToAdd())
    for i in range(num):
        y = i + 1
        print("Add number " + str(y) + " book")
        addValueToList()
    getValue()    

def getAuthor():
    name = input("Enter the author: ")

    file = open("Books.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    
    result = []
    for i in rows:
        if i[2] == name:
            result.append(i)
        
    if len(result) == 0:
        print("Dont have any book of this author")
    else:
        for j in result:
            print(j)            

    
askToAdd()
addValueToList()
getAuthor()        

    