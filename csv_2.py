import csv

filename='abc.csv'

with open(filename) as f:
	reader_row=csv.reader(f)
	row=next(reader_row)
	print(row)

for index,row_content in enumerate(row):
		print(index,row_content)
