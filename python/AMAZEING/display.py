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

"""Visualizzazione del labirinto nel terminale (a blocchi, interattivo).

Ogni cella occupa 2 colonne di caratteri e i muri sono disegnati con il
carattere blocco '█': il labirinto 20x15 occupa 41 colonne, cosi' entra
in qualsiasi terminale senza andare a capo.
"""

from mazegen import N, W, MazeGenerator

RED: str = "\033[31m"
GREEN: str = "\033[32m"
YELLOW: str = "\033[33m"
BLUE: str = "\033[34m"
MAGENTA: str = "\033[35m"
CYAN: str = "\033[36m"
FORTY_TWO: str = "\033[97m"
RESET: str = "\033[0m"
CLEAR: str = "\033[2J\033[H"

WALL_COLORS: list[str] = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]


def run(gen: MazeGenerator) -> None:
	"""Loop interattivo: mostra il labirinto e reagisce ai tasti.

	Tasti: r = rigenera, p = mostra/nascondi percorso, c = cambia colore
	dei muri, q = esci.
	"""
	show_path = False
	color_index = 0
	while True:
		print(CLEAR)
		_print_maze(gen, show_path, WALL_COLORS[color_index])
		print("r = rigenera | p = percorso on/off | c = colore | q = esci")
		cmd = input("> ").strip().lower()
		if cmd == "r":
			gen.generate(perfect=gen.perfect, entry=gen.entry,
			             exit=gen.exit, with_42=True)
			show_path = False
		elif cmd == "p":
			show_path = not show_path
		elif cmd == "c":
			color_index = (color_index + 1) % len(WALL_COLORS)
		elif cmd == "q":
			break


def _print_maze(gen: MazeGenerator, show_path: bool, wall_color: str) -> None:
	"""Disegna il labirinto con il carattere blocco '█'.

	I muri sono blocchi pieni, i passaggi spazi vuoti. Le celle del
	pattern "42" sono riempite con un blocco bianco brillante (cosi'
	il 42 e' ben visibile come silhouette piena). I = entrata,
	O = uscita, . = percorso.
	"""
	path: list[tuple[int, int]] = []
	if show_path:
		path = gen.solve()

	print(wall_color)
	for y in range(gen.height):
		top = "█"
		for x in range(gen.width):
			if (gen.grid[y][x] & N) != 0:
				top = top + "██"
			else:
				top = top + " █"
		print(top)

		middle = ""
		for x in range(gen.width):
			if (gen.grid[y][x] & W) != 0:
				middle = middle + "█"
			else:
				middle = middle + " "
			if (x, y) in gen.forty_two:
				middle = middle + FORTY_TWO + "█" + wall_color
			elif (x, y) == gen.entry:
				middle = middle + YELLOW + "I" + wall_color
			elif (x, y) == gen.exit:
				middle = middle + YELLOW + "O" + wall_color
			elif (x, y) in path:
				middle = middle + GREEN + "." + wall_color
			else:
				middle = middle + " "
		middle = middle + "█"
		print(middle)

	bottom = "█" + "██" * gen.width
	print(bottom)
	print(RESET)
