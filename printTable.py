tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


def printTable(list):
    columnWidth = 0
    #Find the longest item.
    for column in list:
        for item in column:
            if columnWidth < len(item):
                columnWidth = len(item)

    itemNum = 0
    while itemNum < len(column):
        colNum = 0
        for column in list:
            print(list[colNum][itemNum].rjust(columnWidth), end=' ')
            colNum += 1
        itemNum += 1
        print()





printTable(tableData)
