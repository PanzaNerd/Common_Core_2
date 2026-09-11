# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                    :+:      :+:    :+:    #
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
	print("=== Cyber Archives Recovery ===")
	if len(sys.argv) != 2:
		print("Usage: ft_ancient_text.py <file>")
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


if __name__ == "__main__":
	main()
