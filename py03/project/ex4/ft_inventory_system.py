import sys


def create_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for param in sys.argv[1:]:
        try:
            (name, qty) = parse_parameter(param, inventory)
            inventory.update({name: qty})
        except Exception as e:
            print(e)
    return inventory


def parse_parameter(param: str, inventory: dict[str, int]) -> tuple[str, int]:
    splitted = param.split(":")
    if len(splitted) != 2:
        raise Exception(f"Error - invalid parameter '{param}'")
    name = splitted[0]
    if name in inventory:
        raise Exception(f"Redundant item '{name}' - discarding")
    qty_str = splitted[1]
    try:
        qty = int(qty_str)
    except Exception as e:
        raise Exception(f"Quantity error for '{name}': {e}")
    return (name, qty)


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = create_inventory()

    item_names = list(inventory.keys())
    item_values = inventory.values()
    distinct_values = len(item_names)
    total_values = sum(item_values)

    most_abundant = max(inventory, key=lambda k: inventory[k])
    least_abundant = min(inventory, key=lambda k: inventory[k])

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_names}")
    print(f"Total quantity of the {distinct_values} items: {total_values}")

    for name in inventory:
        value = inventory[name]
        percent = (value * 100) / total_values
        print(f"Item {name} represents {percent:.1f}%")

    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}"
    )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
