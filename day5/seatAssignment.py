
class SeatAssignments:
	def __init__(self):
		self.listOfSeatAssignments = self.readInputFile('input.txt')



	def readInputFile(self, fileName):
		file = open(fileName, 'r')
		seats = {}

		for line in file:
			seatRow = line[0:7].replace("F","0").replace("B","1")
			seatNumber = line[7:-1].replace("L","0").replace("R","1")
			seat = Seat(int(seatRow,2), int(seatNumber,2))
			seats[seat.seatId] = seat


		file.close()
		return seats

class Seat:
	def __init__(self, rowNumber, seatNumber):
		self.rowNumber = rowNumber
		self.seatNumber = seatNumber
		self.seatId = (self.rowNumber*8)+self.seatNumber



assignments = SeatAssignments()
largestId = 0
comprehensiveSeats = {}
for seat in assignments.listOfSeatAssignments:
	# print(str(assignments.listOfSeatAssignments[seat].rowNumber) + ", " + str(assignments.listOfSeatAssignments[seat].seatNumber) + "    " + str(assignments.listOfSeatAssignments[seat].seatId))
	if assignments.listOfSeatAssignments[seat].seatId > largestId:
		largestId = assignments.listOfSeatAssignments[seat].seatId

for x in range(1,122):
	for y in range(0, 8):
		if (x*8)+y not in assignments.listOfSeatAssignments:
			print((x*8)+y)


