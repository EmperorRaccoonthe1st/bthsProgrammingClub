# You can import a module of other peoples code, or from files you have made

# "import {name}"


import random

# A module to generate a semirandom number

for i in range(random.randint(0, 1000)):
    print(f"Hello {str(i)}")

# I can also import a specific funtion from that module

# "from {module name} import {function name}"

from random import randrange

# Generate a random even number between 2 and 20
even_number = random.randrange(2, 21, 2)
print(even_number)
























