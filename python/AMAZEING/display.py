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

"""Visualizzazione del labirinto nel terminale (ASCII classico, interattivo).

Muri spessi e continui: '###' orizzontali, '#' verticali, ogni angolo
marcato con '+'. Solo caratteri ASCII di base: identici in qualsiasi
terminale e con qualsiasi font. Ogni cella occupa 3 colonne: un
labirinto 20x15 e' largo 61 caratteri.
"""

from mazegen import N, S, W, MazeGenerator

RED: str = "\033[31m"
GREEN: str = "\033[32m"
BLUE: str = "\033[34m"
MAGENTA: str = "\033[35m"
CYAN: str = "\033[36m"
NORMAL: str = ""
BRICK: str = "█"
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
	"""Disegna il labirinto in ASCII classico con muri spessi.

	Muri orizzontali '###', verticali '#', angoli '+'. Il pattern "42"
	e' un blocco pieno di mattoncini '█' nel colore di default del
	terminale (resta tale anche cambiando il colore dei muri). I =
	entrata, O = uscita, percorso = catena di 'x' verdi.
	"""
	path: list[tuple[int, int]] = []
	if show_path:
		path = gen.solve()

	path_h: list[tuple[int, int]] = []
	path_v: list[tuple[int, int]] = []
	for i in range(len(path) - 1):
		x1, y1 = path[i]
		x2, y2 = path[i + 1]
		if y2 == y1 - 1:
			path_h.append((x1, y1))
		elif y2 == y1 + 1:
			path_h.append((x2, y2))
		elif x2 == x1 + 1:
			path_v.append((x2, y2))
		else:
			path_v.append((x1, y1))

	for y in range(gen.height):
		top = ""
		for x in range(gen.width):
			if (gen.grid[y][x] & N) != 0:
				if (x, y) in gen.forty_two or (x, y - 1) in gen.forty_two:
					top = top + NORMAL + BRICK + BRICK + BRICK + wall_color
				else:
					top = top + "+##"
			else:
				if (x, y) in path_h:
					top = top + "+" + GREEN + "xx" + wall_color
				else:
					top = top + "+  "
		print(wall_color + top + "+")

		middle = ""
		for x in range(gen.width):
			if (gen.grid[y][x] & W) != 0:
				if (x, y) in gen.forty_two or (x - 1, y) in gen.forty_two:
					middle = middle + NORMAL + BRICK + wall_color
				else:
					middle = middle + "#"
			else:
				if (x, y) in path_v:
					middle = middle + GREEN + "x" + wall_color
				else:
					middle = middle + " "
			if (x, y) in gen.forty_two:
				middle = middle + NORMAL + BRICK + BRICK + wall_color
			elif (x, y) == gen.entry:
				middle = middle + NORMAL + "I " + wall_color
			elif (x, y) == gen.exit:
				middle = middle + NORMAL + "O " + wall_color
			elif (x, y) in path:
				middle = middle + GREEN + "xx" + wall_color
			else:
				middle = middle + "  "
		if (gen.width - 1, y) in gen.forty_two:
			middle = middle + NORMAL + BRICK + wall_color
		else:
			middle = middle + "#"
		print(wall_color + middle)

	bottom = ""
	for x in range(gen.width):
		if (gen.grid[gen.height - 1][x] & S) != 0:
			if (x, gen.height - 1) in gen.forty_two or (x, gen.height - 2) in gen.forty_two:
				bottom = bottom + NORMAL + BRICK + BRICK + BRICK + wall_color
			else:
				bottom = bottom + "+##"
		else:
			bottom = bottom + "+  "
	print(wall_color + bottom + "+")
	print(RESET)
