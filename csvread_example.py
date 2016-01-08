import csv

csvfilename = "server_L2.csv"

print "Printing all rows"
with open(csvfilename, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	for row in reader:
		print "   ", row
print ""

print "Printing all rows using header line"
with open(csvfilename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        print "   ", row
print ""


