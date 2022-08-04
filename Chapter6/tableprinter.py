tableData = [['apples', 'oranges', 'cheeries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colsWidths = [0]*len(table) #this variable will be used to store width of each column
    # I am using max function with key=len on each list in the table to find the longest string --> it's length be the length of the colum
    for i in range(len(table)):
        colsWidths[i] = len(max(table[i], key = len)) # colsWidths = [8,5,5]
    # Looping through the table to print columns
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colsWidths[j], " "), end = " ")
        print("\n")

printTable(tableData)