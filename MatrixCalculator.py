from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
import sys
import functools

fp = functools.partial

num_of_rows = 0
num_of_columns = 0
entries = []

def setup_normal_matrix():
	for i in range(1, num_of_rows + 1):
		if i == 1:
			top_left_corner_label = Label(middle_eqt_frame, text="/ ")
			top_left_corner_label.grid(row=0, column=0)

			top_right_corner_label = Label(middle_eqt_frame, text=" \\")
			top_right_corner_label.grid(row=0, column=2 * num_of_columns)

		elif i == num_of_rows:
			bottom_left_corner_label = Label(middle_eqt_frame, text="\\ ")
			bottom_left_corner_label.grid(row=i - 1, column=0)

			bottom_right_corner_label = Label(middle_eqt_frame, text=" /")
			bottom_right_corner_label.grid(row=i - 1, column=2 * num_of_columns)

		else:
			right_label = Label(middle_eqt_frame, text="| ")
			right_label.grid(row=i - 1, column=0)

			left_label = Label(middle_eqt_frame, text=" |")
			left_label.grid(row=i - 1, column=2 * num_of_columns)

		for j in range(1, num_of_columns + 1):
			exec(f"entry_{i}_{j} = Entry(middle_eqt_frame, width=5)")
			exec(f"entry_{i}_{j}.bind('<Return>', on_eqt_submit_press)")
			exec(f"entries.append(entry_{i}_{j})")
			exec(f"entry_{i}_{j}.grid(row={i - 1}, column={2 * j - 1})")

			if j != num_of_columns:
				space_label = Label(middle_eqt_frame, text=" ")
				space_label.grid(row=i - 1, column=2 * j)

def setup_matrix():
	global num_of_rows, num_of_columns, entries

	entries = []

	try:
		num_of_rows = int(num_of_rows_entry.get())
		num_of_columns = int(num_of_columns_entry.get())

	except:
		messagebox.showwarning("Invalid input", "Please input positive integers.")
		return

	if num_of_rows == 0 or num_of_columns == 0:
		messagebox.showwarning("Invalid input", "Please input positive integers.")
		return

	if (mode_combobox.get() == "Determinant" or mode_combobox.get() == "Inverse") and num_of_rows != num_of_columns:
		messagebox.showwarning("Invalid input", "Number of rows should be the same as number of columns.")
		return

	for widget in middle_eqt_frame.winfo_children():
		widget.destroy()

	if mode_combobox.get() == "RREF - A. Matrix":
		for i in range(1, num_of_rows + 1):
			if i == 1:
				top_left_corner_label = Label(middle_eqt_frame, text="/ ")
				top_left_corner_label.grid(row=0, column=0)

				top_right_corner_label = Label(middle_eqt_frame, text=" \\")
				top_right_corner_label.grid(row=0, column=2 * num_of_columns + 1)

			elif i == num_of_rows:
				bottom_left_corner_label = Label(middle_eqt_frame, text="\\ ")
				bottom_left_corner_label.grid(row=i - 1, column=0)

				bottom_right_corner_label = Label(middle_eqt_frame, text=" /")
				bottom_right_corner_label.grid(row=i - 1, column=2 * num_of_columns + 1)

			else:
				right_label = Label(middle_eqt_frame, text="| ")
				right_label.grid(row=i - 1, column=0)

				left_label = Label(middle_eqt_frame, text=" |")
				left_label.grid(row=i - 1, column=2 * num_of_columns + 1)

			for j in range(1, 2 * num_of_columns + 1):
				if j <= 2 * num_of_columns - 2:
					if j % 2 != 0:
						exec(f"entry_{i}_{int((j + 1) / 2)} = Entry(middle_eqt_frame, width=5)")
						exec(f"entry_{i}_{int((j + 1) / 2)}.bind('<Return>', on_eqt_submit_press)")
						exec(f"entries.append(entry_{i}_{int((j + 1) / 2)})")
						exec(f"entry_{i}_{int((j + 1) / 2)}.grid(row={i - 1}, column={j})")

					else:
						space_label = Label(middle_eqt_frame, text=" ")
						space_label.grid(row=i - 1, column=j)

				elif j == 2 * num_of_columns - 1:
					space_label = Label(middle_eqt_frame, text="|   ")
					space_label.grid(row=i - 1, column=j)

				else:
					exec(f"entry_{i}_{int(j / 2)} = Entry(middle_eqt_frame, width=5)")
					exec(f"entry_{i}_{int(j / 2)}.bind('<Return>', on_eqt_submit_press)")
					exec(f"entries.append(entry_{i}_{int(j / 2)})")
					exec(f"entry_{i}_{int(j / 2)}.grid(row={i - 1}, column={j})")

	elif mode_combobox.get() == "RREF - Matrix":
		setup_normal_matrix()

	elif mode_combobox.get() == "Echelon Form - A. Matrix":
		for i in range(1, num_of_rows + 1):
			if i == 1:
				top_left_corner_label = Label(middle_eqt_frame, text="/ ")
				top_left_corner_label.grid(row=0, column=0)

				top_right_corner_label = Label(middle_eqt_frame, text=" \\")
				top_right_corner_label.grid(row=0, column=2 * num_of_columns + 1)

			elif i == num_of_rows:
				bottom_left_corner_label = Label(middle_eqt_frame, text="\\ ")
				bottom_left_corner_label.grid(row=i - 1, column=0)

				bottom_right_corner_label = Label(middle_eqt_frame, text=" /")
				bottom_right_corner_label.grid(row=i - 1, column=2 * num_of_columns + 1)

			else:
				right_label = Label(middle_eqt_frame, text="| ")
				right_label.grid(row=i - 1, column=0)

				left_label = Label(middle_eqt_frame, text=" |")
				left_label.grid(row=i - 1, column=2 * num_of_columns + 1)

			for j in range(1, 2 * num_of_columns + 1):
				if j <= 2 * num_of_columns - 2:
					if j % 2 != 0:
						exec(f"entry_{i}_{int((j + 1) / 2)} = Entry(middle_eqt_frame, width=5)")
						exec(f"entry_{i}_{int((j + 1) / 2)}.bind('<Return>', on_eqt_submit_press)")
						exec(f"entries.append(entry_{i}_{int((j + 1) / 2)})")
						exec(f"entry_{i}_{int((j + 1) / 2)}.grid(row={i - 1}, column={j})")

					else:
						space_label = Label(middle_eqt_frame, text=" ")
						space_label.grid(row=i - 1, column=j)

				elif j == 2 * num_of_columns - 1:
					space_label = Label(middle_eqt_frame, text="|   ")
					space_label.grid(row=i - 1, column=j)

				else:
					exec(f"entry_{i}_{int(j / 2)} = Entry(middle_eqt_frame, width=5)")
					exec(f"entry_{i}_{int(j / 2)}.bind('<Return>', on_eqt_submit_press)")
					exec(f"entries.append(entry_{i}_{int(j / 2)})")
					exec(f"entry_{i}_{int(j / 2)}.grid(row={i - 1}, column={j})")

	elif mode_combobox.get() == "Echelon Form - Matrix":
		setup_normal_matrix()

	elif mode_combobox.get() == "Determinant":
		for i in range(1, num_of_rows + 1):
			right_label = Label(middle_eqt_frame, text="| ")
			right_label.grid(row=i - 1, column=0)

			left_label = Label(middle_eqt_frame, text=" |")
			left_label.grid(row=i - 1, column=2 * num_of_columns)

			for j in range(1, num_of_columns + 1):
				exec(f"entry_{i}_{j} = Entry(middle_eqt_frame, width=5)")
				exec(f"entry_{i}_{j}.bind('<Return>', on_eqt_submit_press)")
				exec(f"entries.append(entry_{i}_{j})")
				exec(f"entry_{i}_{j}.grid(row={i - 1}, column={2 * j - 1})")

				if j != num_of_columns:
					space_label = Label(middle_eqt_frame, text=" ")
					space_label.grid(row=i - 1, column=2 * j)

	elif mode_combobox.get() == "Transpose":
		setup_normal_matrix()

	else:
		setup_normal_matrix()

	eqt_submit_button.configure(state=NORMAL)

def on_settings_submit_press(event):
	setup_matrix()

def simplify_fraction(fraction: list) -> list:
	hcf = 1
	x, y = fraction[0], fraction[1]

	while y:
		x, y = y, x % y

	hcf = x

	return [fraction[0] / hcf, fraction[1] / hcf]

def convert_decimal_to_fraction(decimal: float) -> list:
	tmp_fraction = [decimal, 1.0]
	
	while int(str(tmp_fraction[0]).split(".")[1]) != 0:
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

def print_matrix(matrix: list):
	reduced_matrix = []

	for eqt in matrix:
		reduced_matrix.append([str(int(entry[0])) if int(entry[1]) == 1 else f"{str(int(entry[0]))}/{str(int(entry[1]))}" for entry in eqt])

	highest_length = 0
	
	for eqt in reduced_matrix:
		for entry in eqt:
			if len(entry) > highest_length:
				highest_length = len(entry)

	for i in range(len(reduced_matrix)):
		for j in range(len(reduced_matrix[i])):
			reduced_matrix[i][j] = f"{reduced_matrix[i][j]}{' ' * (highest_length + 2 - len(reduced_matrix[i][j]))}"

	for i in range(len(reduced_matrix)):
		if mode_combobox.get() == "RREF - A. Matrix" or mode_combobox.get() == "Echelon Form - A. Matrix":
			if i == 0:
				print(f"/{' ' * (highest_length + 1)}{''.join(reduced_matrix[i][:-1])}|{' ' * (highest_length + 1)}{reduced_matrix[i][-1]}\\")

			elif i == len(reduced_matrix) - 1:
				print(f"\\{' ' * (highest_length + 1)}{''.join(reduced_matrix[i][:-1])}|{' ' * (highest_length + 1)}{reduced_matrix[i][-1]}/")

			else:
				print(f"|{' ' * (highest_length + 1)}{''.join(reduced_matrix[i][:-1])}|{' ' * (highest_length + 1)}{reduced_matrix[i][-1]}|")

		else:
			if i == 0:
				print(f"/{' ' * (highest_length + 1)}{''.join(reduced_matrix[i])}\\")

			elif i == len(reduced_matrix) - 1:
				print(f"\\{' ' * (highest_length + 1)}{''.join(reduced_matrix[i])}/")

			else:
				print(f"|{' ' * (highest_length + 1)}{''.join(reduced_matrix[i])}|")

	print()

def get_int_matrix() -> list:
	str_matrix = []

	for entry in entries:
		if entry.get() == "":
			str_matrix.append("0")

		else:
			str_matrix.append(entry.get())

	matrix = []

	while len(str_matrix) != 0:
		matrix.append(str_matrix[:num_of_columns])
		str_matrix = str_matrix[num_of_columns:]

	int_matrix = []

	for eqt in matrix:
		tmp_eqt = []

		for entry in eqt:
			try:
				if "/" in entry:
					tmp_eqt.append(simplify_fraction([float(num) for num in entry.split("/")]))

				elif "." in entry:
					tmp_eqt.append(convert_decimal_to_fraction(float(entry)))

				else:
					tmp_eqt.append([float(entry), 1.0])

			except:
				messagebox.showwarning("Invalid input", "Please input rational numbers.")
				return

		int_matrix.append(tmp_eqt)

	return int_matrix

def rref() -> list:
	int_matrix = get_int_matrix()

	if int_matrix == None:
		return

	rearrange(int_matrix)

	for i in range(len(int_matrix)):
		for j in range(i + 1, len(int_matrix)):
			n = i

			while True:
				try:
					if calculate_fraction(int_matrix[i][n]) == 0:
						n += 1
						continue

					break

				except:
					for eqt in range(len(int_matrix)):
						# if mode_combobox.get() == "RREF - A. Matrix":
						# 	int_matrix[eqt] = [fraction_division(int_matrix[eqt][entry], first_nonzero(int_matrix[eqt][:-1])) for entry in range(len(int_matrix[eqt]))]

						# else:
						# 	int_matrix[eqt] = [fraction_division(int_matrix[eqt][entry], first_nonzero(int_matrix[eqt])) for entry in range(len(int_matrix[eqt]))]
						int_matrix[eqt] = [fraction_division(int_matrix[eqt][entry], first_nonzero(int_matrix[eqt])) for entry in range(len(int_matrix[eqt]))]

					for k in range(len(int_matrix) - 1, -1, -1):
						try:
							# if mode_combobox.get() == "RREF - A. Matrix":
							# 	idx = int_matrix[k][:-1].index([1.0, 1.0])

							# else:
							# 	idx = int_matrix[k].index([1.0, 1.0])
							idx = int_matrix[k].index([1.0, 1.0])

							for w in range(k - 1, -1, -1):
								int_matrix[w] = [fraction_addition(fraction_multiplication([-int_matrix[w][idx][0], int_matrix[w][idx][1]], int_matrix[k][entry]), int_matrix[w][entry])for entry in range(len(int_matrix[k]))]

						except:
							continue
					
					return int_matrix

			int_matrix[j] = [fraction_addition(fraction_multiplication(fraction_division([-int_matrix[j][n][0], int_matrix[j][n][1]], int_matrix[i][n]), int_matrix[i][entry]), int_matrix[j][entry]) for entry in range(len(int_matrix[i]))]

		rearrange(int_matrix)

	for eqt in range(len(int_matrix)):
		# if mode_combobox.get() == "RREF - A. Matrix":
		# 	int_matrix[eqt] = [fraction_division(int_matrix[eqt][entry], first_nonzero(int_matrix[eqt][:-1])) for entry in range(len(int_matrix[eqt]))]

		# else:
		# 	int_matrix[eqt] = [fraction_division(int_matrix[eqt][entry], first_nonzero(int_matrix[eqt])) for entry in range(len(int_matrix[eqt]))]
		int_matrix[eqt] = [fraction_division(int_matrix[eqt][entry], first_nonzero(int_matrix[eqt])) for entry in range(len(int_matrix[eqt]))]

	for k in range(len(int_matrix) - 1, -1, -1):
		try:
			# if mode_combobox.get() == "RREF - A. Matrix":
			# 	idx = int_matrix[k][:-1].index([1.0, 1.0])

			# else:
			# 	idx = int_matrix[k].index([1.0, 1.0])
			idx = int_matrix[k].index([1.0, 1.0])

			for w in range(k - 1, -1, -1):
				int_matrix[w] = [fraction_addition(fraction_multiplication([-int_matrix[w][idx][0], int_matrix[w][idx][1]], int_matrix[k][entry]), int_matrix[w][entry])for entry in range(len(int_matrix[k]))]

		except:
			continue
	
	return int_matrix

def echelon_form() -> list:
	int_matrix = get_int_matrix()

	if int_matrix == None:
		return

	rearrange(int_matrix)

	for i in range(len(int_matrix)):
		for j in range(i + 1, len(int_matrix)):
			n = i

			while True:
				try:
					if calculate_fraction(int_matrix[i][n]) == 0:
						n += 1
						continue

					break

				except:					
					return int_matrix

			int_matrix[j] = [fraction_addition(fraction_multiplication(fraction_division([-int_matrix[j][n][0], int_matrix[j][n][1]], int_matrix[i][n]), int_matrix[i][entry]), int_matrix[j][entry]) for entry in range(len(int_matrix[i]))]

		rearrange(int_matrix)
	
	return int_matrix

def calculate_determinant(square_matrix: list) -> list:
	if len(square_matrix) == 1:
		return square_matrix[0][0]

	else:
		tmp_determinant = [0.0, 1.0]
		for i in range(len(square_matrix[0])):
			cofactor_list = []
			
			for row in square_matrix[1:]:
				for j in range(len(row)):
					if j != i:
						cofactor_list.append(row[j])

			cofactor = []

			while len(cofactor_list) != 0:
				cofactor.append(cofactor_list[:len(square_matrix[0]) - 1])
				cofactor_list = cofactor_list[len(square_matrix[0]) - 1:]

			tmp_determinant = fraction_addition(tmp_determinant, fraction_multiplication([(-1) ** i * square_matrix[0][i][0], square_matrix[0][i][1]], calculate_determinant(cofactor)))

		return tmp_determinant

def print_determinant():
	int_matrix = get_int_matrix()

	if int_matrix == None:
		return

	determinant_numerator, determinant_denominator = calculate_determinant(int_matrix)
	determinant = str(int(determinant_numerator)) if int(determinant_denominator) == 1 else f"{int(determinant_numerator)}/{int(determinant_denominator)}"
	print(f"Determinant = {determinant}\n")

def transpose(matrix: list = []) -> list:
	int_matrix = matrix

	if len(matrix) == 0:
		int_matrix = get_int_matrix()

	if int_matrix == None:
		return
		
	transpose_list = [int_matrix[j][i] for i in range(num_of_columns) for j in range(num_of_rows)]
	transpose = []

	while len(transpose_list) != 0:
		transpose.append(transpose_list[:num_of_rows])
		transpose_list = transpose_list[num_of_rows:]

	return transpose

def scalar_multiplication(scalar: list, matrix: list) -> list:
	int_matrix = matrix

	for i in range(len(int_matrix)):
		for j in range(len(int_matrix[i])):
			int_matrix[i][j] = fraction_multiplication(scalar, int_matrix[i][j])

	return int_matrix

def inverse() -> list:
	int_matrix = get_int_matrix()

	if int_matrix == None:
		return

	determinant = calculate_determinant(int_matrix)

	if calculate_fraction(determinant) == 0:
		print("The inverse of this matrix does not exist.\n")
		return

	cofactor_matrix = []

	for i in range(num_of_rows):
		tmp_cofactor_matrix = []

		for j in range(num_of_columns):
			cofactor_list = []

			for k in range(num_of_rows):
				for w in range(num_of_columns):
					if k != i and w != j:
						cofactor_list.append(int_matrix[k][w])

			cofactor = []

			while len(cofactor_list) != 0:
				cofactor.append(cofactor_list[:num_of_rows - 1])
				cofactor_list = cofactor_list[num_of_rows - 1:]

			if j % 2 == 0:
				if i % 2 == 0:
					tmp_cofactor_matrix.append(calculate_determinant(cofactor))

				else:
					tmp_cofactor_matrix.append([-1 * calculate_determinant(cofactor)[0], calculate_determinant(cofactor)[1]])

			else:
				if i % 2 == 0:
					tmp_cofactor_matrix.append([-1 * calculate_determinant(cofactor)[0], calculate_determinant(cofactor)[1]])

				else:
					tmp_cofactor_matrix.append(calculate_determinant(cofactor))

		cofactor_matrix.append(tmp_cofactor_matrix)

	adjugate_matrix = transpose(cofactor_matrix)
	inverse = scalar_multiplication(fraction_division([1.0, 1.0], determinant), adjugate_matrix)

	return inverse

def decide_function():
	if "RREF" in mode_combobox.get():
		matrix = rref()

		if matrix == None:
			return

		print("RREF =\n")
		print_matrix(matrix)

	elif "Echelon Form" in mode_combobox.get():
		matrix = echelon_form()

		if matrix == None:
			return

		print("Echelon Form =\n")
		print_matrix(matrix)

	elif mode_combobox.get() == "Determinant":
		print_determinant()

	elif mode_combobox.get() == "Transpose":
		matrix = transpose()

		if matrix == None:
			return

		print("Transpose =\n")
		print_matrix(matrix)

	else:
		matrix = inverse()

		if matrix == None:
			return

		print("Inverse =\n")
		print_matrix(matrix)

def on_eqt_submit_press(event):
	decide_function()

########## Linux ##########

# def on_mousewheel(event, scroll):
# 	canvas.yview_scroll(int(scroll), "units")

# def bind_to_mousewheel(event):
# 	canvas.bind_all("<Button-4>", fp(on_mousewheel, scroll=-1))
# 	canvas.bind_all("<Button-5>", fp(on_mousewheel, scroll=1))

# def unbind_fron_mousewheel(event):
# 	canvas.unbind_all("<Button-4>")
# 	canvas.unbind_all("<Button-5>")

########## Windows ##########

def on_mousewheel(event):
	canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def bind_to_mousewheel(event):
	canvas.bind_all("<MouseWheel>", on_mousewheel)

def unbind_fron_mousewheel(event):
	canvas.unbind_all("<MouseWheel>")

root = Tk()
root.title("Virtual Assistant - Matrix Calculator")
root.geometry("560x280")
root.resizable(0, 0)
try:
	########## Linux ##########
	# root.iconbitmap(f"@{os.path.dirname(os.path.realpath(__file__))}/matrix_calculator.xbm")

	########## Windows ##########
	root.iconbitmap(f"{os.path.dirname(os.path.realpath(__file__))}/matrix_calculator.ico")

except Exception as e:
	messagebox.showerror("Error", e)
	sys.exit()

top_frame = Frame(root)
top_frame.pack(fill=X, pady=10)

top_left_frame = Frame(top_frame)
top_left_frame.pack(side=LEFT, padx=5)

top_middle_frame = Frame(top_frame)
top_middle_frame.pack(side=LEFT)

top_right_frame = Frame(top_frame)
top_right_frame.pack(side=RIGHT, padx=20)

bottom_frame = Frame(root)
bottom_frame.pack(padx=10, fill=BOTH, expand=True)

mode_label = Label(top_left_frame, text="Mode:")
mode_label.grid(row=0, column=0)

mode_combobox = Combobox(top_left_frame, values=["Determinant", "Echelon Form - A. Matrix", "Echelon Form - Matrix", "Inverse", "RREF - A. Matrix", "RREF - Matrix", "Transpose"], state="readonly")
mode_combobox.current(5)
mode_combobox.grid(row=0, column=1)

rows_label = Label(top_middle_frame, text="Number of rows:")
rows_label.grid(row=0, column=0, sticky="E", padx=5)

num_of_rows_entry = Entry(top_middle_frame, width=5)
num_of_rows_entry.bind("<Return>", on_settings_submit_press)
num_of_rows_entry.grid(row=0, column=1)

num_of_columns_label = Label(top_middle_frame, text="Number of columns:")
num_of_columns_label.grid(row=1, column=0, sticky="E", padx=5)

num_of_columns_entry = Entry(top_middle_frame, width=5)
num_of_columns_entry.bind("<Return>", on_settings_submit_press)
num_of_columns_entry.grid(row=1, column=1)

settings_submit_button = Button(top_right_frame, text="Submit", command=setup_matrix)
settings_submit_button.pack()

canvas = Canvas(bottom_frame)
canvas.bind("<Enter>", bind_to_mousewheel)
canvas.bind("<Leave>", unbind_fron_mousewheel)
canvas.grid(row=0, column=0, sticky="nesw")

canvas_vscrollbar = Scrollbar(bottom_frame)
canvas_vscrollbar.grid(row=0, column=1, sticky="nes")
canvas_vscrollbar.configure(command=canvas.yview)

canvas_hscrollbar = Scrollbar(bottom_frame, orient="horizontal")
canvas_hscrollbar.grid(row=1, column=0, sticky="esw")
canvas_hscrollbar.configure(command=canvas.xview)

canvas.configure(xscrollcommand=canvas_hscrollbar.set, yscrollcommand=canvas_vscrollbar.set)

middle_eqt_frame = Frame(canvas)
middle_eqt_frame.pack(fill=BOTH, expand=True)

middle_eqt_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=middle_eqt_frame, anchor="nw")

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

bottom_submit_frame = Frame(bottom_frame)
bottom_submit_frame.grid(row=2, column=0, columnspan=2, sticky="nesw")

eqt_submit_button = Button(bottom_submit_frame, text="Submit", state=DISABLED, command=decide_function)
eqt_submit_button.pack(side=RIGHT, padx=10, pady=10)

root.mainloop()
