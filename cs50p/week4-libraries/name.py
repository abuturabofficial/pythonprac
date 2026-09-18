import sys

# try:
#     print("Hello, my name is", sys.argv[1].capitalize())
# except IndexError:
#     print("Too few arguments")

# # Let's check for exceptions ourselves
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello! my name is", sys.argv[1].capitalize())


# # More better approach (allegedly)
# if len(sys.argv) <2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) >2:
#     sys.exit("Too many arguments")
#
# print("Hello! my name is", sys.argv[1].capitalize())


# Multiple arguments
if len(sys.argv) <2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: #Don't print [0] program name, start from first arg
    print("Hello! my name is", arg)
