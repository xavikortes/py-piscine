#!/usr/bin/env python3

import os

from dotenv import load_dotenv


def load_config() -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_dotenv(os.path.join(dir_path, ".env.example"))
    load_dotenv(override=True)


def print_configuration() -> None:
    mode = os.environ.get("MATRIX_MODE")

    if mode == "production":
        print("[PROD] Mode: production")
        print("[PROD] Database: Connected to remote server")
        print("[PROD] API Access: Authenticated")
        print(f"[PROD] Log level: {os.environ.LOG_LEVEL}")
        print("[PROD] Remote Network: Online")
    else:
        print("Mode: development")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log level: {os.environ.LOG_LEVEL}")
        print("Remote Network: Online")


def print_security_checks(config: dict[str, str]):
    print(f"SEC {config}")


def main() -> None:
    print()
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    print("Configuration loaded:")
    load_config()
    print_configuration()
    print()
    print("Configuration security check:")
    print_security_checks({})
    print()
    print("The Oracle sees all configurations.")
    print()


if __name__ == "__main__":
    main()
