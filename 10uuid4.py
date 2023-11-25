# I user uuid4 for database ids instead of int
# when testing new project need uuid4s

from uuid import uuid4

for number in range(1,11):
    print(uuid4())
