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

I muri orizzontali sono '-', i verticali '|', gli incroci '+': caratteri
ASCII presenti in qualsiasi terminale e con qualsiasi font. Ogni cella
occupa 2 colonne: un labirinto 20x15 e' largo 41 caratteri.
"""

from mazegen import N, S, W, MazeGenerator

RED: str = "\033[31m"
GREEN: str = "\033[32m"
BLUE: str = "\033[34m"
MAGENTA: str = "\033[35m"
CYAN: str = "\033[36m"
BLACK: str = "\033[30m"
WHITE_BG: str = "\033[47m"
RESET: str = "\033[0m"
CLEAR: str = "\033[2J\033[H"

# colori dei muri ciclabili con 'c' (leggibili su sfondo chiaro;
# il verde NON c'e': e' riservato alla linea del percorso)
WALL_COLORS: list[str] = [BLACK, RED, BLUE, MAGENTA, CYAN]


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
	"""Disegna il labirinto in ASCII classico su sfondo chiaro.

	Muri: '-' e '|', incroci '+', passaggi = spazi. Il pattern "42" e'
	una silhouette nera compatta (resta nera anche cambiando il colore
	dei muri). I = entrata, O = uscita, percorso = linea verde continua
	di 'o' che attraversa anche le aperture tra le celle.
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

	print(WHITE_BG + wall_color)
	for y in range(gen.height):
		top = "+"
		for x in range(gen.width):
			if (gen.grid[y][x] & N) != 0:
				if (x, y) in gen.forty_two or (x, y - 1) in gen.forty_two:
					top = top + BLACK + "-" + wall_color
				else:
					top = top + "-"
			else:
				if (x, y) in path_h:
					top = top + GREEN + "-" + wall_color
				else:
					top = top + " "
			if (x, y) in gen.forty_two or (x + 1, y) in gen.forty_two:
				top = top + BLACK + "+" + wall_color
			else:
				top = top + "+"
		print(top)

		middle = ""
		for x in range(gen.width):
			if (gen.grid[y][x] & W) != 0:
				if (x, y) in gen.forty_two or (x - 1, y) in gen.forty_two:
					middle = middle + BLACK + "|" + wall_color
				else:
					middle = middle + "|"
			else:
				if (x, y) in path_v:
					middle = middle + GREEN + "|" + wall_color
				else:
					middle = middle + " "
			if (x, y) in gen.forty_two:
				middle = middle + BLACK + "#" + wall_color
			elif (x, y) == gen.entry:
				middle = middle + BLACK + "I" + wall_color
			elif (x, y) == gen.exit:
				middle = middle + BLACK + "O" + wall_color
			elif (x, y) in path:
				middle = middle + GREEN + "o" + wall_color
			else:
				middle = middle + " "
		middle = middle + "|"
		print(middle)

	bottom = "+"
	for x in range(gen.width):
		if (gen.grid[gen.height - 1][x] & S) != 0:
			if (x, gen.height - 1) in gen.forty_two or (x, gen.height - 2) in gen.forty_two:
				bottom = bottom + BLACK + "-" + wall_color
			else:
				bottom = bottom + "-"
		else:
			bottom = bottom + " "
		if (x, gen.height - 1) in gen.forty_two or (x + 1, gen.height - 1) in gen.forty_two:
			bottom = bottom + BLACK + "+" + wall_color
		else:
			bottom = bottom + "+"
	print(bottom)
	print(RESET)
