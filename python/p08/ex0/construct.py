# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    construct.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import site
import sys


def main() -> None:
	in_venv = sys.prefix != sys.base_prefix

	if in_venv:
		print("MATRIX STATUS: Welcome to the construct")
	else:
		print("MATRIX STATUS: You're still plugged in")

	print(f"Current Python: {sys.executable}")

	if in_venv:
		print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
		print(f"Environment Path: {sys.prefix}")
		print("SUCCESS: You're in an isolated environment!")
		print("Safe to install packages without affecting")
		print("the global system.")
		print("Package installation path:")
		print(site.getsitepackages()[0])
	else:
		print("Virtual Environment: None detected")
		print("WARNING: You're in the global environment!")
		print("The machines can see everything you install.")
		print("To enter the construct, run:")
		print("python -m venv matrix_env")
		print("source matrix_env/bin/activate # On Unix")
		print("matrix_env\\Scripts\\activate # On Windows")
		print("Then run this program again.")


if __name__ == "__main__":
	main()
