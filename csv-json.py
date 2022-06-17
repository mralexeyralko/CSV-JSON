# The feature, that takes CSV file of a certain format and converts it to JSON, adds 'Total' 
# key to the end of it, counting values

import csv #import modules needed
import json 

def convert(fileName): #function declaration
    dictionary = {}
    other = {}

    with open(fileName, mode='r') as inp: #opens file
        reader = csv.reader(inp)
        dictionary = {rows[0]:[int(rows[1]), int(rows[2]), int(rows[3])] for rows in reader} #specifies the view of otput file

    x = iter(dictionary.keys()) #iterator declaration
    dictionary2 = dictionary.copy()
    dictionary2['Total'] = 'Value' #adds 'total' key to the end of the file

    for rows in dictionary: #counting total
        other.update({next(x):sum(dictionary[rows])})

    dictionary2['Total']= other

    with open('converted.json', 'w', encoding='utf-8') as f: #writes the file
        json.dump(dictionary2, f, ensure_ascii=False, indent=4)
         
    print('Done')

convert('data_sample.csv') #calls the function