def get_number(prompt):
	"""Read a numeric value from the user with validation."""
	while True:
		value = input(prompt).strip()
		try:
			return float(value)
		except ValueError:
			print("Invalid input. Please enter a valid number.")


def calculate(first, second, operator):
	"""Perform a calculation for the selected operator."""
	if operator == "+":
		return first + second
	if operator == "-":
		return first - second
	if operator == "*":
		return first * second
	if operator == "/":
		if second == 0:
			raise ZeroDivisionError("Division by zero is not allowed.")
		return first / second
	if operator == "//":
		if second == 0:
			raise ZeroDivisionError("Floor division by zero is not allowed.")
		return first // second
	if operator == "%":
		if second == 0:
			raise ZeroDivisionError("Modulus by zero is not allowed.")
		return first % second
	if operator == "**":
		return first**second
	raise ValueError("Unsupported operator selected.")


def show_menu():
	"""Display available calculator operations."""
	print("\nCalculator Operations")
	print("+   : Addition")
	print("-   : Subtraction")
	print("*   : Multiplication")
	print("/   : Division")
	print("//  : Floor Division")
	print("%   : Modulus")
	print("**  : Exponent")
	print("Type q to quit")


def main():
	print("Simple Calculator App")
	while True:
		show_menu()
		operator = input("Choose an operator: ").strip()

		if operator.lower() in {"q", "quit", "exit"}:
			print("Calculator closed.")
			break

		if operator not in {"+", "-", "*", "/", "//", "%", "**"}:
			print("Invalid operator. Please choose from the menu.")
			continue

		first_number = get_number("Enter first number: ")
		second_number = get_number("Enter second number: ")

		try:
			result = calculate(first_number, second_number, operator)
			print(f"Result: {first_number} {operator} {second_number} = {result}")
		except ZeroDivisionError as error:
			print(error)


if __name__ == "__main__":
	main()