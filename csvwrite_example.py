import csv

outputfile = "test_csvwrite.csv"

data = [["web01", 101, "SRV"],
		["web02", 102, "SRV"],
		["web03", 103, "SRV"]]

print "Output data is"
print "   ", data
print ""
		
print "writing data to file: %s"%outputfile
print "To view:"
print "   cat %s"%outputfile
with open(outputfile, 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter='\t')
	for row in data:
		writer.writerow(row)
print ""


#
# output of csv writer using headers
#
outputfile_dict = "test_csvwrite_dict.csv"

data = [{ "name": "web01", "id": 101, "LAN": "SRV"}, 
		{ "name": "web02", "id": 102, "LAN": "SRV"},
		{ "name": "web03", "id": 103, "LAN": "SRV"}]

print "Output data is"
print "   ", data

fieldnames = data[0].keys()
print "Fields are ", fieldnames
print ""
	
print "writing dictionary data to file: %s"%outputfile_dict
print "To view:"
print "   cat %s"%outputfile_dict

with open(outputfile_dict, 'wb') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
	writer.writeheader()

	for row in data:
		writer.writerow( row )
print ""


