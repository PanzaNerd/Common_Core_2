# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def secure_archive(filename: str, action: str = "read", content: str = "") -> tuple[bool, str]:
	if action == "write":
		try:
			with open(filename, "w") as f:
				f.write(content)
			return (True, "Content successfully written to file")
		except OSError as e:
			return (False, str(e))
	try:
		with open(filename, "r") as f:
			return (True, f.read())
	except OSError as e:
		return (False, str(e))


def main() -> None:
	print("=== Cyber Archives Security ===")

	print("Using 'secure_archive' to read from a nonexistent file:")
	ok, msg = secure_archive("/not/existing/file")
	print(f'({ok}, "{msg}")')

	print("Using 'secure_archive' to read from an inaccessible file:")
	ok, msg = secure_archive("/etc/master.passwd")
	print(f'({ok}, "{msg}")')

	print("Using 'secure_archive' to read from a regular file:")
	ok, msg = secure_archive("ancient_fragment.txt")
	print(f'({ok}, "{msg}")')

	print("Using 'secure_archive' to write previous content to a new file:")
	if ok:
		ok, msg = secure_archive("new_fragment.txt", "write", msg)
		print(f'({ok}, "{msg}")')


if __name__ == "__main__":
	main()
