#!/usr/bin/env python3

import os
import site
import sys


def im_inside_venv() -> bool:
    return sys.prefix != sys.base_prefix


def working_in_the_open() -> None:
    python_path = sys.executable

    print()
    print("LABORATORY STATUS: You are working in the open")
    print()
    print(f"Current Python: {python_path}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print("To seal the laboratory, run:")
    print("$> python3 -m venv lab_env")
    print("$> source lab_env/bin/activate")
    print()
    print("The run this program again.")
    print()


def working_in_the_lab() -> None:
    python_path = sys.executable
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)
    installation_path = site.getsitepackages()[0]

    print()
    print("LABORATORY STATUS: The laboratory is sealed")
    print()
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")
    print()
    print("Reagent installation path:")
    print(installation_path)
    print()


def main() -> None:
    if im_inside_venv():
        working_in_the_lab()
    else:
        working_in_the_open()


if __name__ == "__main__":
    main()
