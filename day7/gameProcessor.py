

class GameProcessor:
	def __init__(self):
		self.instructions = self.readInstructions('input.txt')
		self.accumulator = 0


	def readInstructions(self, fileName):
		file = open(fileName, 'r')
		array = []
		for row in file:
			array.append(Instruction(row))
		return array


	def executeInstruction(self, position):
		print(position)
		inst = self.instructions[position]

		if inst.executed != 0:
			return -1

		if inst.instruction == "acc":
			self.accumulator = self.accumulator + inst.number
			inst.executed = inst.executed + 1
			return position + 1
		elif inst.instruction == "nop":
			inst.executed = inst.executed + 1
			return position + 1
		elif inst.instruction == "jmp":
			inst.executed = inst.executed + 1
			return position + inst.number	
		else:
			print("halt and catch fire")

	def runInstructionsOnce(self, startingLocation):
		execResult = self.executeInstruction(startingLocation)
		while execResult != -1:
			execResult = self.executeInstruction(execResult)

		return execResult


	def changeAnInstructionAndRun(self):
		for x in range(len(0, self.instructions)):
			if self.instructions[x].instruction == "jmp":
				self.instructions[x] = self.instructions[x].replace("jmp","nop")

		return ""
			


class Instruction:
	def __init__(self, inputString):
		self.instruction = inputString[0:3]
		self.number = self.processRowNumber(inputString[4:])
		self.executed = 0

	def processRowNumber(self, rowNumber):
		if rowNumber[0] == "+":
			return int(rowNumber[1:])
		else:
			return int(rowNumber)



gameProcessor = GameProcessor()



gameProcessor.runInstructionsOnce(0)

# for inst in gameProcessor.instructions:
# 	print(inst.instruction)
# 	print(inst.number)
# 	print(inst.executed)

print(gameProcessor.accumulator)