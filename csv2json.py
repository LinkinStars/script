# -*- coding:utf-8 -*-  
import csv
import json
 
file_path = "file.csv"
output_path = "file.json"

csv_file = open(file_path, 'r')
json_file = open(output_path, 'w')

reader = csv.DictReader( csv_file ) 
out = json.dumps([ row for row in reader ], ensure_ascii=False)

json_file.write(out)
