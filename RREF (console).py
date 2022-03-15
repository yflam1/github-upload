def check_leading_zero(eqt_1: list, eqt_2: list) -> int:
	eqt_1_zero, eqt_2_zero = 0, 0

	for i in eqt_1:
		if i == 0:
			eqt_1_zero += 1

		else:
			break

	for j in eqt_2:
		if j == 0:
			eqt_2_zero += 1

		else:
			break

	return 0 if eqt_1_zero > eqt_2_zero else 1

def rearrange(matrix: list):
	for i in range(len(matrix)):
		for j in range(i + 1, len(matrix)):
			if not check_leading_zero(matrix[i], matrix[j]):
				matrix[i], matrix[j] = matrix[j], matrix[i]

def first_nonzero(row: list) -> float:
	for i in row:
		if i != 0:
			return i

	return 1.0

def rref(matrix: list):
	rearrange(matrix)

	for i in range(len(matrix)):
		for j in range(i + 1, len(matrix)):
			n = i

			while True:
				if matrix[i][n] == 0:
					n += 1
					continue

				break

			matrix[j] = [round(-matrix[j][n] / matrix[i][n] * matrix[i][entry] + matrix[j][entry], 6) for entry in range(len(matrix[i]))]
			# print(matrix)

		rearrange(matrix)
	# 	for row in matrix:
	# 		print(row)
			
	# 	print()

	for eqt in range(len(matrix)):
		matrix[eqt] = [round(matrix[eqt][entry] / first_nonzero(matrix[eqt][:-1]), 6) for entry in range(len(matrix[eqt]))]
	# 	# print(matrix)
		
	# for row in matrix:
	# 	print(row)
			
	# print()

	for k in range(len(matrix) - 1, -1, -1):
		try:
			idx = matrix[k][:-1].index(1.0)
			for w in range(k - 1, -1, -1):
				matrix[w] = [round(-matrix[w][idx] * matrix[k][entry] + matrix[w][entry], 6) for entry in range(len(matrix[k]))]
				# print(matrix)

		except:
			continue
		
	# 	for row in matrix:
	# 		print(row)
			
	# 	print()

matrix =    [[2, 3.5, -1, 3, 6],
             [0, 0, -4, -2, -1],
             [0, 7, -6, 4, 11]]

for row in matrix:
	print(row)

print()
rref(matrix)

print()
for row in matrix:
	print(row)
