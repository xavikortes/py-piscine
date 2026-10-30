#!/usr/bin/env python3

import importlib.metadata


def print_dependencies() -> bool:
    all_deps = True
    try:
        version = importlib.metadata.version("pandas")
        print(f"[OK] pandas ({version}) - Data manipulation ready")
    except Exception:
        print("[KO] pandas - not installed")
        all_deps = False
    try:
        version = importlib.metadata.version("numpy")
        print(f"[OK] numpy ({version}) - Numerical computation ready")
    except Exception:
        print("[KO] numpy - not installed")
        all_deps = False
    return all_deps


def main() -> None:
    has_all_reagents = False

    print()
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    has_all_reagents = print_dependencies()
    print()
    print("pip vs Poetry:")
    print(" requirements.txt declares what to install; pip resolves it at install time.")
    print(" pyproject.toml declares the same constraints, and Poetry pins the resolved")
    print(" versions in poetry.lock so every install is identical.")
    print()
    if has_all_reagents:
        print("All reagents present and accounted for.")
    else:
        print("Not all reagents present. Please install it with 'pip install' or 'poetry install'.")
    print()


if __name__ == "__main__":
    main()
