# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_processor.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

	def __init__(self, name: str) -> None:
		self.name = name
		self._data: list[tuple[int, str]] = []
		self._rank = 0
		self._total = 0

	def _store(self, pieces: list[str]) -> None:
		for piece in pieces:
			self._data.append((self._rank, piece))
			self._rank += 1
			self._total += 1

	@abstractmethod
	def validate(self, data: Any) -> bool:
		...

	@abstractmethod
	def ingest(self, data: Any) -> None:
		...

	def output(self) -> tuple[int, str]:
		return self._data.pop(0)


class NumericProcessor(DataProcessor):

	def __init__(self) -> None:
		super().__init__("Numeric Processor")

	def validate(self, data: Any) -> bool:
		if isinstance(data, (int, float)):
			return True
		if isinstance(data, list):
			return all(isinstance(item, (int, float)) for item in data)
		return False

	def ingest(self, data: int | float | list[int | float]) -> None:
		if not self.validate(data):
			raise TypeError("Improper numeric data")
		if isinstance(data, list):
			self._store([str(item) for item in data])
		else:
			self._store([str(data)])


class TextProcessor(DataProcessor):

	def __init__(self) -> None:
		super().__init__("Text Processor")

	def validate(self, data: Any) -> bool:
		if isinstance(data, str):
			return True
		if isinstance(data, list):
			return all(isinstance(item, str) for item in data)
		return False

	def ingest(self, data: str | list[str]) -> None:
		if not self.validate(data):
			raise TypeError("Improper text data")
		if isinstance(data, list):
			self._store(list(data))
		else:
			self._store([data])


class LogProcessor(DataProcessor):

	def __init__(self) -> None:
		super().__init__("Log Processor")

	def validate(self, data: Any) -> bool:
		if isinstance(data, dict):
			return all(isinstance(k, str) and isinstance(v, str) for k, v in data.items())
		if isinstance(data, list):
			return all(isinstance(item, dict) for item in data)
		return False

	def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
		if not self.validate(data):
			raise TypeError("Improper log data")
		if isinstance(data, list):
			entries = data
		else:
			entries = [data]
		pieces = [f"{entry['log_level']}: {entry['log_message']}" for entry in entries]
		self._store(pieces)


def main() -> None:
	print("=== Code Nexus - Data Processor ===")

	print("Testing Numeric Processor...")
	numeric = NumericProcessor()
	print("Trying to validate input '42':", numeric.validate(42))
	print("Trying to validate input 'Hello':", numeric.validate("Hello"))
	print("Test invalid ingestion of string 'foo' without prior validation:")
	try:
		numeric.ingest("foo")
	except TypeError as e:
		print(f"Got exception: {e}")

	print("Processing data: [1, 2, 3, 4, 5]")
	numeric.ingest([1, 2, 3, 4, 5])
	print("Extracting 3 values...")
	for i in range(3):
		rank, value = numeric.output()
		print(f"Numeric value {i}: {value}")

	print("Testing Text Processor...")
	text = TextProcessor()
	print("Trying to validate input '42':", text.validate(42))
	print("Processing data: ['Hello', 'Nexus', 'World']")
	text.ingest(["Hello", "Nexus", "World"])
	print("Extracting 1 value...")
	rank, value = text.output()
	print(f"Text value 0: {value}")

	print("Testing Log Processor...")
	log = LogProcessor()
	print("Trying to validate input 'Hello':", log.validate("Hello"))
	logs = [
		{"log_level": "NOTICE", "log_message": "Connection to server"},
		{"log_level": "ERROR", "log_message": "Unauthorized access!!"},
	]
	print(f"Processing data: {logs}")
	log.ingest(logs)
	print("Extracting 2 values...")
	for i in range(2):
		rank, value = log.output()
		print(f"Log entry {i}: {value}")


if __name__ == "__main__":
	main()
