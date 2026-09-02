# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/01 17:47:59 by matthias          #+#    #+#              #
#    Updated: 2026/09/01 18:38:29 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations(operation_number: int) -> None:
	if operation_number == 0:
			int("abc")
	elif operation_number == 1:
			result = 1 / 0
	elif operation_number == 2:
			open("/non/existent/file")
	elif operation_number == 3:
			result = "garden" + 42

def test_error_types() -> None:
	print("=== Garden Error Types Demo ===")

	print("Testing operation 0...")
	try:
			garden_operations(0)
	except ValueError as e:
			print(f"Caught ValueError: {e}")

	print("Testing operation 1...")
	try:
			garden_operations(1)
	except ZeroDivisionError as e:
			print(f"Caught ZeroDivisionError: {e}")

	print("Testing operation 2...")
	try:
			garden_operations(2)
	except FileNotFoundError as e:
			print(f"Caught FileNotFoundError: {e}")

	print("Testing operation 3...")
	try:
			garden_operations(3)
	except TypeError as e:
			print(f"Caught TypeError: {e}")

	print("Testing operation 4...")
	try:
			garden_operations(4)
	except Exception as e:
			print(f"Caught error: {e}")
	else:
			print("Operation completed successfully")

	print("All error types tested successfully!")


if __name__ == "__main__":
	test_error_types()
