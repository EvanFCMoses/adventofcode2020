

class QuestionaireResults:
	def __init__(self):
		# self.groupOfRows = self.parseForRows('input.txt')
		self.listOfGroupResults = self.parseRows(self.parseForRows('input.txt'))


	def parseForRows(self, fileName):
		file = open(fileName, 'r')
		array = []
		currentRows = []
		for row in file:
			row = row[:-1]
			if row == "":
				array.append(currentRows)
				currentRows = []
			else:
				currentRows.append(row)

		array.append(currentRows)
		return array

	def parseRows(self, rowOfRows):
		
		groupResponses = []
		for rows in rowOfRows:
			response = GroupAnswers()
			response.groupSize = len(rows)
			for row in rows:
				self.appendAnswersToDict(response.answerDict, row) 
			groupResponses.append(response)
		return groupResponses


	def appendAnswersToDict(self, answers, row):
		for char in row:
			if char in answers:
				answers[char] = answers[char] + 1
			else:
				answers[char] = 1

	def getDictWithUnanimousAnswers(self):
		print("todo")


class GroupAnswers:
	def __init__(self):

		self.answerDict = {}
		self.groupSize = 0


questionaire = QuestionaireResults()

addition = 0
for result in questionaire.listOfGroupResults:
	
	for question in result.answerDict:
		if result.answerDict[question] == result.groupSize:
			addition = addition + 1
	print(result.answerDict)


print(addition)