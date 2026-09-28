# This is a calculator program
import math

while (1):
	
	operation = input("Enter the operation addition(+), subtraction(-), division(/), multiplication(*) or exit(e): ")
	if operation == "e":
			print("Goodbye")
			exit()
	try:
		_num1 = float(input("Enter the first number: "))
		_num2 = float(input("Enter the second number: "))

		match operation:
			case "+":
				print(f"The sum is {round((_num1 + _num1), 3)}")
			case "-":
				print(f"The subtraction is {round((_num1 - _num2), 3)}")
			case "/":
				print(f"The division is {round((_num1 / _num2), 3)}")
			case "*":
				print(f"The multiplication is {round((_num1 * _num2), 3)}")

			case _:
				print("Please enter a valid operation")
	except (TypeError, ValueError):
		print("PLEASE ENTER A VALID NUMBER")
		continue