# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release", "use"]


def gen_event() -> Generator[tuple[str, str], None, None]:
	while True:
		name = random.choice(PLAYERS)
		action = random.choice(ACTIONS)
		yield (name, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
	while len(events) > 0:
		event = random.choice(events)
		events.remove(event)
		yield event


def main() -> None:
	print("=== Game Data Stream Processor ===")

	stream = gen_event()
	for i in range(1000):
		name, action = next(stream)
		print(f"Event {i}: Player {name} did action {action}")

	event_list = []
	for _ in range(10):
		name, action = next(stream)
		event_list.append((name, action))
	print(f"Built list of 10 events: {event_list}")

	for event in consume_event(event_list):
		print(f"Got event from list: {event}")
		print(f"Remains in list: {event_list}")


if __name__ == "__main__":
	main()
