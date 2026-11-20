import sys

type = sys.argv[1]

if type == "t2.micro":
    print(" ok we will charge 2 dollars per hour ")
elif type == "t2.small":
    print(" ok we will charge 4 dollars per hour ")
elif type == "t2.medium":
    print(" ok we will charge 8 dollars per hour ")
else:
    print(" sorry we don't have this type of instance ")