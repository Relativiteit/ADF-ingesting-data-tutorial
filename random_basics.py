import random
import string

print(string.ascii_lowercase)

input = random.randint(1, 99)
print(random.choices(string.ascii_lowercase, k=random.randint(1, 15)))

output = random.randint(1, 20)
print(output)
