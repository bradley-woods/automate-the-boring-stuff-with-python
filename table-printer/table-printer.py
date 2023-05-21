# Automate the Boring Stuff with Python
# Chapter 6 - Manipulating Strings: Table Printer

def printTable(tableData):
    colWidths = [0] * len(tableData) # [0, 0, 0]
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            # Store maximum width of each column
            colWidths[y] = len(max(tableData[y], key=len))
            print(tableData[y][x].rjust(colWidths[y]+1), end="")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],]

printTable(tableData)