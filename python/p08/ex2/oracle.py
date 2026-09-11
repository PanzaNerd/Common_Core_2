# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    oracle.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from dotenv import load_dotenv


def main() -> None:
	load_dotenv()

	mode = os.getenv("MATRIX_MODE")
	db_url = os.getenv("DATABASE_URL")
	api_key = os.getenv("API_KEY")
	log_level = os.getenv("LOG_LEVEL")
	zion = os.getenv("ZION_ENDPOINT")

	print("=== The Oracle ===")
	if mode is None:
		print("WARNING: MATRIX_MODE not set. Copy .env.example to .env")
		print("         and fill in your values.")
		return

	print(f"MATRIX_MODE: {mode}")
	if mode == "development":
		print("Running in DEVELOPMENT mode:")
		print("  - verbose logs enabled")
		print("  - local database")
		print(f"  - DATABASE_URL: {db_url or 'not set'}")
		print(f"  - LOG_LEVEL: {log_level or 'DEBUG'}")
		print(f"  - ZION_ENDPOINT: {zion or 'localhost:8080'}")
	elif mode == "production":
		print("Running in PRODUCTION mode:")
		print("  - minimal logs")
		print("  - production database")
		print(f"  - DATABASE_URL: {db_url or 'MISSING - production needs a database!'}")
		if api_key is None:
			print("WARNING: API_KEY missing! Production requires an API_KEY.")
		else:
			print(f"  - API_KEY: {'*' * len(api_key)} (hidden)")
		print(f"  - ZION_ENDPOINT: {zion or 'MISSING - production needs Zion!'}")
	else:
		print(f"Error: unknown MATRIX_MODE '{mode}'")


if __name__ == "__main__":
	main()
