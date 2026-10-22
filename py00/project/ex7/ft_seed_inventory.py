def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_str = seed_type.capitalize()

    match unit:
        case "packets":
            print(f"{seed_type_str} seeds: {quantity} packets available")
        case "grams":
            print(f"{seed_type_str} seeds: {quantity} grams total")
        case "area":
            print(f"{seed_type_str} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type")
