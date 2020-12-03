

class Password:
	def __init__(self, stringInput):
		self.password = self.ParsePassword(stringInput)
		self.ruleLetter = self.ParseRuleLetter(stringInput)
		self.lowerBound = self.ParseLowerBound(stringInput)
		self.upperBound = self.ParseUpperBound(stringInput)
		self.isValid = self.ComputeRule()
		self.isValidForPart2 = self.ComputeRuleForPart2()

	def ParsePassword(self, input):
		splitInput = input.split(" ")
		return splitInput[2][:-1]

	def ParseRuleLetter(self, input):
		splitInput = input.split(" ")
		return splitInput[1][:-1]

	def ParseLowerBound(self, input):
		splitInput = input.split(" ")
		numbers = splitInput[0].split("-")
		return numbers[0]

	def ParseUpperBound(self, input):
		splitInput = input.split(" ")
		numbers = splitInput[0].split("-")
		return numbers[1]

	def ComputeRule(self):
		count = self.password.count(self.ruleLetter)
		return count <= int(self.upperBound) and count >= int(self.lowerBound)

	def ComputeRuleForPart2(self):
		upperBoundCheck = False
		lowerBoundCheck = False
		if(int(self.upperBound)<=(len(self.password))):
			upperBoundCheck=self.password[int(self.upperBound)-1]==self.ruleLetter
		if(int(self.lowerBound)<=(len(self.password))):
			lowerBoundCheck=self.password[int(self.lowerBound)-1]==self.ruleLetter
		return lowerBoundCheck != upperBoundCheck 


inputText = open('input.txt','r')
passwords=[]
validPasswordCount=0
validPasswordCountForPart2=0

for line in inputText:
	password = Password(line)
	if password.isValid:
		validPasswordCount=validPasswordCount+1
	if password.isValidForPart2:
		validPasswordCountForPart2=validPasswordCountForPart2+1
	passwords.append(password)


print(validPasswordCount)
print(validPasswordCountForPart2)