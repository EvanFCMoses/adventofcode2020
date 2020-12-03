inputText = open('input.txt','r')
myDict = {}
fulldoubleaddition = []
index = 0

class Combinations:
	def __init__(self, num1, num2):
		self.number1=num1
		self.number2=num2
		self.addition=self.number1+self.number2

def IsCombinationInArray(array, value):
	for combo in array:
		if(combo.addition==value):
			return True;

def GetCombinationInArray(array, value):
	for combo in array:
		if(combo.addition==value):
			return combo;



for line in inputText:
	myDict[index] = int(line)
	index = index+1

print(len(myDict))
for indexValue in myDict:
	for y in range(indexValue,len(myDict)):
		fulldoubleaddition.append(Combinations(myDict[indexValue], myDict[y]))



for key in myDict:
	if IsCombinationInArray(fulldoubleaddition, 2020-myDict[key]) :
		combo = GetCombinationInArray(fulldoubleaddition, 2020-myDict[key])
		print('values are: ' + str(myDict[key]) + ' and ' + str(combo.number1) + 
			' and ' + str(combo.number2) + ' muliply to: ' + str(myDict[key]*combo.number1*combo.number2))


#it's late, I know this could look better, don't @ me /s