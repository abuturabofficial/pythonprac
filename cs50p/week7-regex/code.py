import re


def main():
    code = input("Hexadecimal Color Code: ")
    pattern = r"^#[A-Fa-f0-9]{6}$"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid")


main()
