def simplify_fraction(fraction: list) -> list:
	hcf = 1
	x, y = fraction[0], fraction[1]

	while y:
		x, y = y, x % y

	hcf = x

	return [fraction[0] / hcf, fraction[1] / hcf]

def convert_decimal_to_fraction(decimal: float) -> list:
	tmp_fraction = [decimal, 1.0]
	
	while int(tmp_fraction[0]) != int(str(tmp_fraction[0]).split(".")[0]):
		tmp_fraction[0], tmp_fraction[1] = tmp_fraction[0] * 10, tmp_fraction[1] * 10
		
	return simplify_fraction(tmp_fraction)

def calculate_fraction(fraction: list) -> float:
	return fraction[0] / fraction[1]

def fraction_addition(fraction_1: list, fraction_2: list) -> list:
	return simplify_fraction([fraction_1[0] * fraction_2[1] + fraction_1[1] * fraction_2[0], fraction_1[1] * fraction_2[1]])

def fraction_multiplication(fraction_1: list, fraction_2: list) -> list:
	return simplify_fraction([fraction_1[0] * fraction_2[0], fraction_1[1] * fraction_2[1]])

def fraction_division(fraction_1: list, fraction_2: list) -> list:
	return simplify_fraction([fraction_1[0] * fraction_2[1], fraction_1[1] * fraction_2[0]])

def check_leading_zero(eqt_1: list, eqt_2: list) -> int:
	eqt_1_zero, eqt_2_zero = 0, 0

	for i in eqt_1:
		if calculate_fraction(i) == 0:
			eqt_1_zero += 1

		else:
			break

	for j in eqt_2:
		if calculate_fraction(j) == 0:
			eqt_2_zero += 1

		else:
			break

	return 0 if eqt_1_zero > eqt_2_zero else 1

def rearrange(matrix: list):
	for i in range(len(matrix)):
		for j in range(i + 1, len(matrix)):
			if not check_leading_zero(matrix[i], matrix[j]):
				matrix[i], matrix[j] = matrix[j], matrix[i]

def first_nonzero(row: list) -> list:
	for i in row:
		if calculate_fraction(i) != 0:
			return i

	return [1, 1]

def rref(matrix: list):
	rearrange(matrix)

	for i in range(len(matrix)):
		for j in range(i + 1, len(matrix)):
			n = i
			print(i, j)

			while True:
				if calculate_fraction(matrix[i][n]) == 0:
					n += 1
					continue

				break

			matrix[j] = [fraction_addition(fraction_multiplication(fraction_division([-matrix[j][n][0], matrix[j][n][1]], matrix[i][n]), matrix[i][entry]), matrix[j][entry]) for entry in range(len(matrix[i]))]
			print(matrix)

		rearrange(matrix)

	for eqt in range(len(matrix)):
		matrix[eqt] = [fraction_division(matrix[eqt][entry], first_nonzero(matrix[eqt][:-1])) for entry in range(len(matrix[eqt]))]

	for k in range(len(matrix) - 1, -1, -1):
		try:
			idx = matrix[k][:-1].index([1.0, 1.0])

			for w in range(k - 1, -1, -1):
				matrix[w] = [fraction_addition(fraction_multiplication([-matrix[w][idx][0], matrix[w][idx][1]], matrix[k][entry]), matrix[w][entry])for entry in range(len(matrix[k]))]

		except:
			continue

matrix =	[["1", "2", "3", "0"],
			 ["4", "5", "6", "0"],
			 ["7", "8", "9", "0"],]

int_matrix = []
for eqt in matrix:
	tmp_eqt = []

	for entry in eqt:
		if "/" in entry:
			tmp_eqt.append([float(num) for num in entry.split("/")])

		elif "." in entry:
			tmp_eqt.append(convert_decimal_to_fraction(float(entry)))

		else:
			tmp_eqt.append([float(entry), 1.0])

	int_matrix.append(tmp_eqt)

print(int_matrix)

for eqt in int_matrix:
	print(eqt)

print()
rref(int_matrix)

reduced_matrix = []

for eqt in int_matrix:
	reduced_matrix.append([str(int(entry[0])) if int(entry[1]) == 1 else f"{str(int(entry[0]))}/{str(int(entry[1]))}" for entry in eqt])

for eqt in reduced_matrix:
	print(eqt)
