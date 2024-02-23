"""
Tabulate helps in creating and formatting the tables
"""
from tabulate import tabulate
from Solution1 import solution1b

tabledata = []
for day, info in solution1b.dict_days().items():
    tabledata.append([day, info[0], info[1], info[2], info[3], info[4]])

tableheaders = ["Name of the Day",
                 "Occurrences", 
                 "Short Form", 
                 "Name in Lower", 
                 "Name in Upper", 
                 "Length"]
table = tabulate(tabledata, headers=tableheaders, tablefmt='grid')
print(table)
