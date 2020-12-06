import unittest
from sled import Tobogan, Hillside

class ToboganTest(unittest.TestCase):

	def setUp(self):
		self.inputText = open('input.txt','r')
		self.sled = Tobogan(3, 1, 25, 0)
		self.hill = Hillside(self.inputText)


	def testWrap(self):
		self.assertEqual(self.sled.coord.x, 25)
		self.hill.moveATobogan(self.sled)
		self.assertEqual(self.sled.coord.x, 28)
		self.hill.moveATobogan(self.sled)
		self.assertEqual(self.sled.coord.x, 0)
		self.assertEqual(self.sled.coord.y, 2)
		self.hill.moveATobogan(self.sled)
		self.assertEqual(self.sled.coord.x, 3)


	def steepTobogan(self):
		sTobogan = Tobogan(1,2,0,0)
		self.hill.moveATobogan(sTobogan)
		self.assertEqual(sTobogan.coord.x, 1)
		self.assertEqual(sTobogan.coord.y, 2)
		self.hill.moveATobogan(sTobogan)
		self.assertEqual(sTobogan.coord.x, 2)
		self.assertEqual(sTobogan.coord.y, 4)

	def steepToboganWrap(self):
		sTobogan = Tobogan(1,2, 29, 1)
		self.hill.moveATobogan(sTobogan)
		self.assertEqual(sTobogan.coord.x, 30)
		self.assertEqual(sTobogan.coord.y, 2)
		self.hill.moveATobogan(sTobogan)
		self.assertEqual(sTobogan.coord.x, 0)
		self.assertEqual(sTobogan.coord.y, 4)
		self.hill.moveATobogan(sTobogan)
		self.assertEqual(sTobogan.coord.x, 1)
		self.assertEqual(sTobogan.coord.y, 6)

	def testWhenToboganAtTheBottom(self):
		bTobogan = Tobogan(1, 2, 0, 320)
		self.assertTrue(not self.hill.wouldAMoveMovePastBottom(bTobogan))
		self.hill.moveATobogan(bTobogan)
		self.assertTrue(self.hill.wouldAMoveMovePastBottom(bTobogan))

	def tearDown(self):
		self.inputText.close()


if __name__ == '__main__':
    unittest.main()