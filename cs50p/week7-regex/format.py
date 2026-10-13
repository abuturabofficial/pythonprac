import re
name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(",")
#     name = f"{first.strip()} {last.strip()}"

matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    # last, first = matches.groups()
    # name = f"{first} {last}"
    # # OR
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    # OR
    name = (matches.group(2) + " " + matches.group(1)).title()

print(f"hello, {name}")
