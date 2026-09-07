# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 10:00:00 by mpanzani         #+#    #+#              #
#    Updated: 2026/09/05 10:00:00 by mpanzani        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Visualizzazione del labirinto nel terminale (ASCII minimale, interattivo).

Ogni cella occupa UN carattere e ogni muro UN carattere '#' (solo
ASCII di base: identico in qualsiasi terminale). Un labirinto 20x15 e'
largo 41 caratteri.
"""

from mazegen import E, N, S, MazeGenerator

RED: str = "\033[31m"
GREEN: str = "\033[32m"
BLUE: str = "\033[34m"
MAGENTA: str = "\033[35m"
CYAN: str = "\033[36m"
NORMAL: str = ""
BRICK: str = "█"
DOT: str = "·"
RESET: str = "\033[0m"
CLEAR: str = "\033[2J\033[H"

# colori dei muri ciclabili con '3' (visibili su sfondo chiaro e scuro;
# il verde NON c'e': e' riservato alla catena del percorso)
WALL_COLORS: list[str] = [RED, BLUE, MAGENTA, CYAN]


def run(gen: MazeGenerator) -> None:
	"""Mostra il labirinto con un menu numerato.

	1 = regenerate maze, 2 = show/hide path, 3 = change wall colour,
	q = quit.
	"""
	show_path = False
	color_index = 0
	while True:
		print(CLEAR)
		print("===== A-MAZE-ING =====")
		_print_maze(gen, show_path, WALL_COLORS[color_index])
		print("+--------------------------------------+")
		print("| 1) Regenerate maze                   |")
		print("| 2) Show/hide path                    |")
		print("| 3) Change wall colour                |")
		print("| q) Quit                              |")
		print("+--------------------------------------+")
		cmd = input("Choice > ").strip().lower()
		if cmd == "1":
			gen.generate(perfect=gen.perfect, entry=gen.entry,
			             exit=gen.exit, with_42=True)
			show_path = False
		elif cmd == "2":
			show_path = not show_path
		elif cmd == "3":
			color_index = (color_index + 1) % len(WALL_COLORS)
		elif cmd == "q":
			break


def _print_maze(gen: MazeGenerator, show_path: bool, wall_color: str) -> None:
	"""Disegna il labirinto minimale: 1 cella = 1 carattere.

	Muri '#' di un solo carattere. Il pattern "42" e' una griglia di
	mattoncini '█' nel colore di default del terminale (resta tale
	anche cambiando il colore dei muri). I = entrata, O = uscita,
	percorso = catena di punti '·' verdi.
	"""
	path: list[tuple[int, int]] = []
	if show_path:
		path = gen.solve()

	path_n: list[tuple[int, int]] = []
	path_e: list[tuple[int, int]] = []
	for i in range(len(path) - 1):
		x1, y1 = path[i]
		x2, y2 = path[i + 1]
		if y2 == y1 - 1:
			path_n.append((x1, y1))
		elif y2 == y1 + 1:
			path_n.append((x2, y2))
		elif x2 == x1 + 1:
			path_e.append((x1, y1))
		else:
			path_e.append((x2, y2))

	for y in range(gen.height):
		wall = "#"
		for x in range(gen.width):
			if (gen.grid[y][x] & N) != 0:
				wall = wall + "#"
			else:
				if (x, y) in path_n:
					wall = wall + GREEN + DOT + wall_color
				else:
					wall = wall + " "
			wall = wall + "#"
		print(wall_color + wall)

		line = "#"
		for x in range(gen.width):
			if (x, y) in gen.forty_two:
				line = line + NORMAL + BRICK + wall_color
			elif (x, y) == gen.entry:
				line = line + NORMAL + "I" + wall_color
			elif (x, y) == gen.exit:
				line = line + NORMAL + "O" + wall_color
			elif (x, y) in path:
				line = line + GREEN + DOT + wall_color
			else:
				line = line + " "
			if (gen.grid[y][x] & E) != 0:
				line = line + "#"
			else:
				if (x, y) in path_e:
					line = line + GREEN + DOT + wall_color
				else:
					line = line + " "
		print(wall_color + line)

	bottom = "#"
	for x in range(gen.width):
		if (gen.grid[gen.height - 1][x] & S) != 0:
			bottom = bottom + "#"
		else:
			bottom = bottom + " "
		bottom = bottom + "#"
	print(wall_color + bottom)
	print(RESET)
