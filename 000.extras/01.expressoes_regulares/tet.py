import re
import csv

path = 'database.csv'

with open ( path ) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    header = next(csv_reader)

    data = [ row for row in csv_reader ]

    

    # print(header)
    print(data[0][0])

    # for row in csv_reader:
    #     print(row)
