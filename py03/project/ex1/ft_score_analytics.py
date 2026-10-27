import sys


def show_analytics(scores: list[int]) -> None:
    players = len(scores)
    total = sum(scores)
    max_score = max(scores)
    min_score = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {total}")
    print(f"Average score: {(total / players):.1f}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


def process_score(score: str) -> int | None:
    try:
        return int(score)
    except Exception:
        print(f"Invalid parameter: '{score}'")
        return None


def main() -> None:
    program_name = sys.argv[0]

    print("=== Player Score Analytics ===")
    scores = [process_score(score) for score in sys.argv[1:]]
    valid_scores = [score for score in scores if score]
    if len(valid_scores):
        show_analytics(valid_scores)
    else:
        print(
            f"No scores provided. "
            f"Usage: python3 {program_name} <score1> <score2>..."
        )
    print()


if __name__ == "__main__":
    main()
