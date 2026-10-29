import random
import typing


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str]]:
    while events:
        idx = random.randint(0, len(events) - 1)
        event = events[idx]
        del events[idx]
        yield event


def gen_event(
        players: list[str], actions: list[str]
        ) -> typing.Generator[tuple[str, str]]:
    while True:
        player_idx = random.randint(0, len(players) - 1)
        action_idx = random.randint(0, len(actions) - 1)

        yield (players[player_idx], actions[action_idx])


def main() -> None:
    print("=== Game Data Stream Processor ===")
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "move", "grab", "use", "climb", "release",
        "run", "swim", "eat", "sleep"
    ]

    generator = gen_event(players, actions)
    for i in range(0, 1000):
        player, action = next(generator)
        print(f"Event {i}: Player {player} did action {action}")

    events = [next(generator) for _ in range(0, 10)]
    print(f"Build list of 10 events: {events}")

    consumer = consume_event(events)
    for event in consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
