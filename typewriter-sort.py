# Works only for positive numbers, because, we only have positive numbers in the universe

import random

def typewriter_sort(lst):
    length = 0
    while True:
        length += 1
        num_count = 0

        while True: 
            random_list = [random.randint(0, num_count) for _ in range(length)]
            print(random_list)
            num_count += 1

            if random_list == sorted(lst):
                return random_list