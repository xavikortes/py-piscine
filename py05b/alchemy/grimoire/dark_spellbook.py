from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eye-ball"]
    
def dark_spell_record(spell_name: str, ingredients: str) -> str:

    validated_ingredients = validate_ingredients(ingredients)
    if "INVALID" in validated_ingredients:
        return f"Spell rejected: {spell_name} ({validated_ingredients})"

    return f"Spell recorded: {spell_name} ({validated_ingredients})"
