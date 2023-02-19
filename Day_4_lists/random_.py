import random
import mymod

random_int = random.randint(1, 10)
print(random_int)
print(mymod.pi)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f'Love score: {love_score}')

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

print(random.randint(0,1))