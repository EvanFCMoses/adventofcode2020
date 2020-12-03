inputText = open('input.txt','r')
myDict = {}

for line in inputText:
	myDict[int(line)] = line[:-1]


for key in myDict:
	if (2020-key) in myDict:
		print('values are: ' + str(key) + ' and ' + str(myDict[2020-key]) + ' and multiply to ' + str(key*int(myDict[2020-key])))