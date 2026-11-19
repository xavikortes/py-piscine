from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    lower_ingredients = ingredients.lower()

    if (any(ingredient in lower_ingredients for ingredient in light_spell_allowed_ingredients())):
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
