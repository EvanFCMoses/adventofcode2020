

inputText = open('input.txt','r')

class Hillside:
	def __init__(self, file):
		self.topography = self.readTopography(file)



	def readTopography(self, file):
		array=[]
		for row in file:
			if row[len(row)-1] == '\n':
				segments = list(row[:-1])
			else:
				segments = list(row)
			array.append(segments)

		return array


	def checkCollision(self, xCoord, yCoord):
		return self.topography[yCoord][xCoord] == "#"

	def moveATobogan(self, tobogan):
		if tobogan.coord.x + tobogan.xMove > (len(self.topography[0])-1):
			tobogan.coord.x = ((tobogan.coord.x + tobogan.xMove)-(len(self.topography[0])-1)-1)
			tobogan.coord.y = tobogan.coord.y + tobogan.yMove
		else:
			tobogan.coord.x = tobogan.coord.x + tobogan.xMove
			tobogan.coord.y = tobogan.coord.y + tobogan.yMove

		if self.checkCollision(tobogan.coord.x, tobogan.coord.y):
			tobogan.numberOfCollisions = tobogan.numberOfCollisions+1


	def wouldAMoveMovePastBottom(self, tobogan):
		return tobogan.coord.y + tobogan.yMove >= len(self.topography)



class Tobogan:
	def __init__(self, xMove, yMove, currentX, currentY):
		self.xMove = xMove
		self.yMove = yMove
		self.coord = Coordinates(currentX, currentY)
		self.numberOfCollisions = 0


class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y



hill = Hillside(inputText)\
# for row in hill.topography:
# 	print(row)

redRunner = Tobogan(1,2, 0, 0)

while not hill.wouldAMoveMovePastBottom(redRunner):
	hill.moveATobogan(redRunner)

print(redRunner.numberOfCollisions)

# print(len(hill.topography[0]))
# print(len(hill.topography))

