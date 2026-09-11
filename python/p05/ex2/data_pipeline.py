# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_pipeline.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):

	def process_output(self, data: list[tuple[int, str]]) -> None:
		...


class CsvPlugin:

	def process_output(self, data: list[tuple[int, str]]) -> None:
		values = [piece for _, piece in data]
		print("CSV Output:")
		print(",".join(values))


class JsonPlugin:

	def process_output(self, data: list[tuple[int, str]]) -> None:
		items = [f'"item_{rank}": "{piece}"' for rank, piece in data]
		print("JSON Output:")
		print("{" + ", ".join(items) + "}")


class DataStream:

	def __init__(self) -> None:
		self._processors: list[DataProcessor] = []

	def register_processor(self, proc: DataProcessor) -> None:
		self._processors.append(proc)

	def process_stream(self, stream: list[Any]) -> None:
		for element in stream:
			handled = False
			for proc in self._processors:
				if proc.validate(element):
					proc.ingest(element)
					handled = True
					break
			if not handled:
				print(f"DataStream error - Can't process element in stream: {element}")

	def print_processors_stats(self) -> None:
		print("== DataStream statistics ==")
		if len(self._processors) == 0:
			print("No processor found, no data")
			return
		for proc in self._processors:
			print(f"{proc.name}: total {proc._total} items processed, remaining {len(proc._data)} on processor")

	def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
		for proc in self._processors:
			data: list[tuple[int, str]] = []
			for _ in range(nb):
				if len(proc._data) == 0:
					break
				data.append(proc.output())
			plugin.process_output(data)


def main() -> None:
	print("=== Code Nexus - Data Pipeline ===")
	print("Initialize Data Stream...")
	stream = DataStream()
	stream.print_processors_stats()

	print("Registering Processors")
	stream.register_processor(NumericProcessor())
	stream.register_processor(TextProcessor())
	stream.register_processor(LogProcessor())

	batch = [
		"Hello world",
		[3.14, -1, 2.71],
		[
			{"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
			{"log_level": "INFO", "log_message": "User wil is connected"},
		],
		42,
		["Hi", "five"],
	]
	print(f"Send first batch of data on stream: {batch}")
	stream.process_stream(batch)
	stream.print_processors_stats()

	print("Send 3 processed data from each processor to a CSV plugin:")
	stream.output_pipeline(3, CsvPlugin())
	stream.print_processors_stats()

	batch2 = [
		21,
		["I love AI", "LLMs are wonderful", "Stay healthy"],
		[
			{"log_level": "ERROR", "log_message": "500 server crash"},
			{"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"},
		],
		[32, 42, 64, 84, 128, 168],
		"World hello",
	]
	print(f"Send another batch of data: {batch2}")
	stream.process_stream(batch2)
	stream.print_processors_stats()

	print("Send 5 processed data from each processor to a JSON plugin:")
	stream.output_pipeline(5, JsonPlugin())
	stream.print_processors_stats()


if __name__ == "__main__":
	main()
