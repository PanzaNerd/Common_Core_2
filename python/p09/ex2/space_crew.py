# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    space_crew.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
	CADET = "cadet"
	OFFICER = "officer"
	LIEUTENANT = "lieutenant"
	CAPTAIN = "captain"
	COMMANDER = "commander"


class CrewMember(BaseModel):
	member_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=2, max_length=50)
	rank: Rank
	age: int = Field(ge=18, le=80)
	specialization: str = Field(min_length=3, max_length=30)
	years_experience: int = Field(ge=0, le=50)
	is_active: bool = True


class SpaceMission(BaseModel):
	mission_id: str = Field(min_length=5, max_length=15)
	mission_name: str = Field(min_length=3, max_length=100)
	destination: str = Field(min_length=3, max_length=50)
	launch_date: datetime
	duration_days: int = Field(ge=1, le=3650)
	crew: List[CrewMember] = Field(min_length=1, max_length=12)
	mission_status: str = "planned"
	budget_millions: float = Field(ge=1.0, le=10000.0)

	@model_validator(mode="after")
	def check_mission_rules(self) -> "SpaceMission":
		if not self.mission_id.startswith("M"):
			raise ValueError("Mission ID must start with 'M'")
		leaders = [m for m in self.crew if m.rank in (Rank.CAPTAIN, Rank.COMMANDER)]
		if len(leaders) == 0:
			raise ValueError("Must have at least one Commander or Captain")
		experienced = [m for m in self.crew if m.years_experience >= 5]
		if self.duration_days > 365 and len(experienced) < len(self.crew) / 2:
			raise ValueError("Long missions need 50% experienced crew")
		if not all(m.is_active for m in self.crew):
			raise ValueError("All crew members must be active")
		return self


def main() -> None:
	print("Space Crew Management")
	print("=" * 38)

	crew = [
		CrewMember(member_id="CR001", name="Alex Vega", rank=Rank.COMMANDER, age=45,
				specialization="Navigation", years_experience=20),
		CrewMember(member_id="CR002", name="Sam Reed", rank=Rank.OFFICER, age=32,
				specialization="Engineering", years_experience=8),
	]
	mission = SpaceMission(
		mission_id="M2024_001",
		mission_name="Voyage to Europa",
		destination="Europa",
		launch_date=datetime(2024, 9, 1, 8, 0),
		duration_days=400,
		crew=crew,
		budget_millions=250.5,
	)
	print("Valid mission created:")
	print(f"Mission: {mission.mission_name}")
	print(f"Destination: {mission.destination}")
	print(f"Crew members: {len(mission.crew)}")
	print(f"Duration: {mission.duration_days} days")
	print("=" * 38)

	print("Expected validation error:")
	try:
		bad_crew = [
			CrewMember(member_id="CR003", name="No Lead", rank=Rank.OFFICER, age=30,
					specialization="Botany", years_experience=3),
		]
		SpaceMission(
			mission_id="M2024_002",
			mission_name="Doomed Mission",
			destination="Mars",
			launch_date=datetime(2024, 10, 1, 8, 0),
			duration_days=30,
			crew=bad_crew,
			budget_millions=10.0,
		)
	except ValidationError as e:
		first_error = e.errors()[0]
		print(first_error["msg"])


if __name__ == "__main__":
	main()
