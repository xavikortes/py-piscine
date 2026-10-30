#!/usr/bin/env python3

def secure_archive(
        filename: str,
        mode: str | None = None,
        content: str | None = None
        ) -> tuple[bool, str]:
    if mode is None:
        mode = "r"
    if mode != "r" and mode != "w":
        return (False, "Error. Incompatible mode. Try 'r' or 'w'")
    if mode == "w" and content is None:
        return (False, "Error. Can't write without content")

    new_content = None
    try:
        with open(filename, mode) as f:
            if mode == "w":
                f.write(content)
                new_content = "Content successfully written to file"
            elif mode == "r":
                new_content = f.read()
    except Exception as e:
        return (False, str(e))
    return (True, new_content or "")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a noexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow", "r"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("ancient_fragment.txt", "r")
    print(content)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", content[1]))
    print()


if __name__ == '__main__':
    main()
