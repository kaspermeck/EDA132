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
	badChars = ['{', '}', ',']

	for line in content:
		if not line.strip():
			# do nothing
			pass
		elif not readData:
			line = line.lower()
			line = ''.join(i for i in line if i not in badChars)
			lineSplit = line.split()
			if lineSplit[0] == '@relation':
				relation = lineSplit[1]
				dataSet.update({'relation': relation})
			if lineSplit[0] == '@attribute':
				attribute = lineSplit[1]
				values = []
				for i in range(2,len(lineSplit)):
					values.append(lineSplit[i])
				allAttr.append( (attribute, tuple(values)) )

			if lineSplit[0] == '@data':
				readData = True
		else:
			# split line on ,
			lineSplit = line.split(',')
			# remove \n from end
			lineSplit[-1] = lineSplit[-1].replace('\n', '')
			dataLine = []
			for data in lineSplit:
				dataLine.append(data)
			allData.append(tuple(dataLine))

	# associate keyword with value
	dataSet.update({'attribute': allAttr})
	dataSet.update({'data': allData})

	return dataSet