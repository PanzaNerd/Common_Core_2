ALLOWED = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    lower = ingredients.lower()
    for word in ALLOWED:
        if word in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
