import csv

filename='abc.csv'
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
