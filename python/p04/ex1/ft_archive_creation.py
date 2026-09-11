# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_archive_creation.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import IO


def main() -> None:
	print("=== Cyber Archives Recovery & Preservation ===")
	if len(sys.argv) != 2:
		print("Usage: ft_archive_creation.py <file>")
		return
	filename = sys.argv[1]
	print(f"Accessing file '{filename}'")
	try:
		f: IO = open(filename, "r")
	except OSError as e:
		print(f"Error opening file '{filename}': {e}")
		return
	content = f.read()
	f.close()
	print("--" + content, end="")
	if not content.endswith("\n"):
		print()
	print(f"--File '{filename}' closed.")

	lines = content.splitlines()
	new_lines = [line + "#" for line in lines]
	print("Transform data:")
	print("--" + new_lines[0])
	for line in new_lines[1:]:
		print(line)

	name = input("--Enter new file name (or empty): ")
	if name == "":
		print("Not saving data.")
		return
	print(f"Saving data to '{name}'")
	try:
		out: IO = open(name, "w")
	except OSError as e:
		print(f"Error opening file '{name}': {e}")
		print("Data not saved.")
		return
	out.write("\n".join(new_lines) + "\n")
	out.close()
	print(f"Data saved in file '{name}'.")


if __name__ == "__main__":
	main()
