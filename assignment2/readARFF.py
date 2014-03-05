"""
Reads an ARRF file.
Returns in the following format:
dataSet = {'relation', 'attributes', 'data'}
'relations' => relation
'attributes' => [(attribute1, (value1, value2, ...)),
				...
				(attributeN, (value1, value2, ...) )]
'data' => [(attributeValue, attribute2Value1, ... , True/False),
			...
			(attributeValue, attributeValue, ..., True/False)]
"""

def readARFF(filename):
	with open(filename) as f:
		content = f.readlines()
	# close file
	f.close()
	
	readData = False
	dataSet = {}
	allAttr = []
	allData = []
	# unwanted symbols
	badChars = ['{', '}', ',', "'"]

	for line in content:
		line = line.lower()
		if not line.strip():
			# do nothing
			pass
		elif line.startswith('%'):
			# remove comments
			pass
		elif not readData:
			line = ''.join(i for i in line if i not in badChars)
			lineSplit = line.split()
			if lineSplit[0] == '@relation':
				relation = lineSplit[1]
				dataSet.update({'relation': relation})
			if lineSplit[0] == '@attribute':
				attribute = lineSplit[1]
				values = []
				for value in range(2,len(lineSplit)):
					values.append(lineSplit[value])
				allAttr.append( [attribute, tuple(values)] )
			if lineSplit[0] == '@data':
				readData = True
		else:
			# split line on ,
			lineSplit = line.split(',')
			# remove \n from end
			lineSplit[-1] = lineSplit[-1].replace('\n', '')
			dataLine = []
			for data in lineSplit:
				try:
					# try to convert to int
					data = int(data)
				except ValueError:
					# do nothing
					pass
				dataLine.append(data)
			allData.append(dataLine)

	# associate keyword with value
	dataSet.update({'attributes': allAttr})
	dataSet.update({'data': allData})

	return dataSet
