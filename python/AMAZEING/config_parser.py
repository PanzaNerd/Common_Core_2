# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config_parser.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 10:00:00 by mpanzani         #+#    #+#              #
#    Updated: 2026/09/05 10:00:00 by mpanzani        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Parsing del file di configurazione del labirinto.

Legge un file di righe KEY=VALUE e restituisce un oggetto Config con i
parametri validati del labirinto.
"""

from dataclasses import dataclass


class ConfigError(Exception):
	"""Errore nel contenuto del file di configurazione."""

	def __init__(self, message: str) -> None:
		super().__init__(message)


@dataclass(frozen=True)
class Config:
	"""Parametri validati del labirinto.

	Attributes:
		width: larghezza del labirinto in celle.
		height: altezza del labirinto in celle.
		entry: coordinate (x, y) dell'entrata.
		exit: coordinate (x, y) dell'uscita.
		output_file: nome del file di output.
		perfect: True se il labirinto deve essere perfetto.
		seed: seme per la riproducibilita' (None = casuale).
	"""

	width: int
	height: int
	entry: tuple[int, int]
	exit: tuple[int, int]
	output_file: str
	perfect: bool
	seed: int | None


REQUIRED_KEYS: set[str] = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}


def _parse_int(raw: str, key: str) -> int:
	"""Converte raw in intero o solleva ConfigError con messaggio chiaro."""
	try:
		return int(raw)
	except ValueError:
		raise ConfigError(f"'{key}' must be an integer, got '{raw}'") from None


def _parse_bool(raw: str, key: str) -> bool:
	"""Converte 'True'/'False' in bool o solleva ConfigError."""
	if raw == "True":
		return True
	if raw == "False":
		return False
	raise ConfigError(f"'{key}' must be True or False, got '{raw}'")


def _parse_coords(raw: str, key: str) -> tuple[int, int]:
	"""Converte 'x,y' in una coppia di interi o solleva ConfigError."""
	parts = raw.split(",")
	if len(parts) != 2:
		raise ConfigError(f"'{key}' must be 'x,y', got '{raw}'")
	x = _parse_int(parts[0].strip(), key)
	y = _parse_int(parts[1].strip(), key)
	return (x, y)


def _check_bounds(point: tuple[int, int], width: int, height: int, key: str) -> None:
	"""Controlla che il punto stia dentro la griglia."""
	x, y = point
	if not (0 <= x < width and 0 <= y < height):
		raise ConfigError(f"'{key}' {point} is outside the maze ({width}x{height})")


def parse_config(path: str) -> Config:
	"""Legge e valida il file di configurazione.

	Args:
		path: percorso del file con righe KEY=VALUE.

	Returns:
		Config con i parametri validati.

	Raises:
		ConfigError: chiave mancante o duplicata, valore non valido.
		OSError: file inesistente o illeggibile (propaga al chiamante).
	"""
	values: dict[str, str] = {}
	with open(path, "r", encoding="utf-8") as f:
		for line_no, line in enumerate(f, start=1):
			stripped = line.strip()
			if stripped == "" or stripped.startswith("#"):
				continue
			if "=" not in stripped:
				raise ConfigError(
					f"line {line_no}: expected 'KEY=VALUE', got '{stripped}'")
			key, value = stripped.split("=", 1)
			key = key.strip()
			value = value.strip()
			if key in values:
				raise ConfigError(f"line {line_no}: duplicate key '{key}'")
			values[key] = value

	missing = REQUIRED_KEYS - set(values)
	if missing:
		raise ConfigError(f"missing mandatory keys: {', '.join(sorted(missing))}")

	width = _parse_int(values["WIDTH"], "WIDTH")
	height = _parse_int(values["HEIGHT"], "HEIGHT")
	if width < 2 or height < 2:
		raise ConfigError(
			f"WIDTH and HEIGHT must be at least 2 (got {width}x{height})")

	entry = _parse_coords(values["ENTRY"], "ENTRY")
	exit_ = _parse_coords(values["EXIT"], "EXIT")
	_check_bounds(entry, width, height, "ENTRY")
	_check_bounds(exit_, width, height, "EXIT")
	if entry == exit_:
		raise ConfigError(f"ENTRY and EXIT must be different (both are {entry})")

	perfect = _parse_bool(values["PERFECT"], "PERFECT")

	output_file = values["OUTPUT_FILE"]
	if output_file == "":
		raise ConfigError("OUTPUT_FILE must not be empty")

	seed: int | None = None
	if "SEED" in values:
		seed = _parse_int(values["SEED"], "SEED")

	return Config(width, height, entry, exit_, output_file, perfect, seed)
