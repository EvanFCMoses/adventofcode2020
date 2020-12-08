import string

class PassportReader:
	def __init__(self):
		self.listOfPassports = self.readFile('input.txt')
		self.amountOfValidPassports = 0


	def readFile(self, fileName):
		file = open(fileName,'r')
		array=[]
		passport = {}

		for row in file:
			row = row[:-1]
			if row == "":
				array.append(passport)
				passport = {}

			else:
				items = row.split(" ")
				for item in items:
					passport[item.split(":")[0]] = item.split(":")[1]
		array.append(passport)

		file.close()

		return array

	def validatePassports(self):
		for passport in self.listOfPassports:
			if self.validateBYR(passport) and self.validateIYR(passport) and self.validateEYR(passport) and self.validateHGT(passport) and self.validateHCL(passport) and self.validateECL(passport) and self.validatePID(passport):
				self.amountOfValidPassports = self.amountOfValidPassports + 1

	def validateBYR(self, passport):
		if 'byr' in passport:
			return int(passport['byr']) > 1919 and int(passport['byr']) < 2003
		else:
			return False

	def validateIYR(self, passport):
		if 'iyr' in passport:
			return int(passport['iyr']) > 2009 and int(passport['iyr']) < 2021
		else:
			return False

	def validateEYR(self, passport):
		if 'eyr' in passport:
			return int(passport['eyr']) > 2019 and int(passport['eyr']) < 2031
		else:
			return False

	def validateHGT(self, passport):
		if 'hgt' in passport:
			if passport['hgt'][-2:] == 'cm':
				return int(passport['hgt'][0:-2]) > 149 and int(passport['hgt'][0:-2]) < 194
			elif passport['hgt'][-2:] == 'in':
				return int(passport['hgt'][0:-2]) > 58 and int(passport['hgt'][0:-2]) < 77
			else:
				return False
		else:
			return False

	def validateHCL(self, passport):
		if 'hcl' in passport:
			if passport['hcl'][0:1] == '#':
				for char in passport['hcl'][1:]:
					if char.isdigit():
						if (not int(char) > -1) or (not int(char) < 10):
							return False
					elif char.isalpha():
						if (not string.ascii_lowercase.index(char) > -1) or (not string.ascii_lowercase.index(char) < 6):
							return False
				return True;
			else:
				return False
		else:
			return False

	def validateECL(self, passport):
		if 'ecl' in passport:
			# print('color: ' + passport['ecl'])
			color = passport['ecl']
			return color == 'amb' or color == 'blu' or color == 'brn' or color == 'gry' or color == 'grn' or color == 'hzl' or color == 'oth'
		else:
			return False

	def validatePID(self, passport):
		if 'pid' in passport:
			characterCount = 0
			for char in passport['pid']:
				if char.isdigit():
					characterCount = characterCount + 1
				else:
					return False
			if characterCount == 9:
				return True
			else:
				return False
		else:
			return False


passportReader = PassportReader()
passportReader.validatePassports()
# for passport in passportReader.listOfPassports:
# 	print(passport)
print(passportReader.amountOfValidPassports)