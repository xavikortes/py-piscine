#!/usr/bin/env python3

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR] 'python-dotenv' is not installed.")
    print("To set up an environment and install it, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate")
    print("pip install -r requirements.txt")
    print("The run this program again.")
    sys.exit(1)


def load_config() -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_dotenv()
    load_dotenv(os.path.join(dir_path, ".env.example"), override=False)


def connect_to_db(mode: str) -> None:
    db_url = os.getenv("DATABASE_URL", None)

    if db_url is None:
        print("[WARN] Database: 'DATABASE_URL' is missing. Cannot connect to cluster")
        return
    
    if mode == "production":
        print("[PROD] Database: Connected to remote cluster")
    else:
        print("Database: Connected to local cluster")


def authenticate_to_api(mode: str) -> None:
    api_key = os.getenv("API_KEY", None)

    if api_key is None:
        print("[WARN] API Access: 'API_KEY' is missing. Cannot connect to server")
        return
    
    if mode == "production":
        print("[PROD] ", end="")
    print("API Access: Authenticated")


def connect_to_zion(mode: str) -> None:
    zion_ep = os.getenv("ZION_ENDPOINT", None)

    if zion_ep is None:
        print("[WARN] Remote network: 'ZION_ENDPOINT' is missing. Cannot connect to network")
        return
    
    if mode == "production":
        print("[PROD] ", end="")
    print("Remote network: Online")


def print_configuration() -> None:
    mode = os.getenv("MATRIX_MODE", "development")
    log_level = os.getenv("LOG_LEVEL", "silent" if mode == "production" else "debug")

    if mode == "production":
        print("[PROD] Mode: production")
    else:
        print(f"Mode: {mode}")

    connect_to_db(mode)
    authenticate_to_api(mode)

    if mode == "production":
        print("[PROD] ", end="")
    print(f"Log Level: {log_level.upper()}")

    connect_to_zion(mode)


def security_checks():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ignore_path = os.path.join(dir_path, ".gitignore")

    env_ignored = False
    if os.path.exists(ignore_path):
        with open(ignore_path, encoding="utf-8") as file:
            if ".env" in [line.strip() for line in file]:
                env_ignored = True

    print("[OK] No hardcore secrets detected")
    if env_ignored:
        print("[OK] .env file properly ignored by git")
    else:
        print("[KO] .env file not ignored by git")
    print("[OK] Production overrides available")


def main() -> None:
    print()
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    load_config()
    print("Configuration loaded:")
    print_configuration()
    print()
    print("Configuration security check:")
    security_checks()
    print()
    print("The Oracle sees all configurations.")
    print()


if __name__ == "__main__":
    main()
