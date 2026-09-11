# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import importlib.metadata


def check_dependency(name: str) -> str:
	try:
		version = importlib.metadata.version(name)
		return f"[OK] {name} ({version})"
	except importlib.metadata.PackageNotFoundError:
		return f"[MISSING] {name}"


def main() -> None:
	print("LOADING STATUS: Loading programs...")
	print("Checking dependencies:")
	deps = ["pandas", "numpy", "requests", "matplotlib"]
	missing = []
	for dep in deps:
		line = check_dependency(dep)
		print(line)
		if "[MISSING]" in line:
			missing.append(dep)

	if missing:
		print()
		print("Some dependencies are missing!")
		print("Install with pip:")
		print("    pip install -r requirements.txt")
		print("Or with Poetry:")
		print("    poetry install")
		print("    poetry run python loading.py")
		return

	print("Analyzing Matrix data...")
	import numpy as np

	data = np.random.randint(1, 100, size=1000)
	print(f"Processing {len(data)} data points...")
	print(f"Mean: {data.mean():.2f}")
	print(f"Std: {data.std():.2f}")

	print("Generating visualization...")
	import matplotlib
	matplotlib.use("Agg")
	import matplotlib.pyplot as plt

	plt.hist(data, bins=30)
	plt.title("Matrix data distribution")
	plt.savefig("matrix_analysis.png")
	print("Analysis complete!")
	print("Results saved to: matrix_analysis.png")

	print()
	print("Package manager comparison:")
	print("pip: requirements.txt -> pip install -r requirements.txt")
	print("Poetry: pyproject.toml -> poetry install")


if __name__ == "__main__":
	main()
