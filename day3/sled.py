

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
			print("wrapping unwrapped coord: " + str(tobogan.coord.x + tobogan.xMove) + "," + str(tobogan.coord.y + tobogan.yMove))
			tobogan.coord.x = ((tobogan.coord.x + tobogan.xMove)-(len(self.topography[0])-1)-1)
			tobogan.coord.y = tobogan.coord.y + tobogan.yMove
			print("new tobogan ruls: coords: " + str(tobogan.coord.x) + "," + str(tobogan.coord.y) + "  move: " + str(tobogan.xMove) + "," + str(tobogan.yMove))
		else:
			tobogan.coord.x = tobogan.coord.x + tobogan.xMove
			tobogan.coord.y = tobogan.coord.y + tobogan.yMove

		if self.checkCollision(tobogan.coord.x, tobogan.coord.y):
			print("collision check for: " + str(tobogan.coord.x + tobogan.xMove) + "  " + str(tobogan.coord.y + tobogan.yMove))
			tobogan.numberOfCollisions = tobogan.numberOfCollisions+1

		tobogan.coord.x = tobogan.coord.x + tobogan.xMove
		tobogan.coord.y = tobogan.coord.y + tobogan.yMove


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



hill = Hillside(inputText)
for row in hill.topography:
	print(row)

redRunner = Tobogan(3,1, 0, 0)


# print("RR coord: " + str(redRunner.coord.x) + " " + str(redRunner.coord.y))
# hill.moveATobogan(redRunner)
# print("RR coord: " + str(redRunner.coord.x) + " " + str(redRunner.coord.y))
while not hill.wouldAMoveMovePastBottom(redRunner):
	print("movement")
	hill.moveATobogan(redRunner)

print(redRunner.numberOfCollisions)

print(len(hill.topography[0])-1)
print(len(hill.topography)-1)

testT = Tobogan(3,1,28, 0)
hill.moveATobogan(testT)
print("new position: " + str(testT.coord.x) + "," + str(testT.coord.y))