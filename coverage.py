#!/usr/bin/python3
import random
import itertools

#data preparation
sets = []
for i in range(100):
    rand_set = set()
    random_numbers = random.randint(0,5)
    for j in range(random_numbers):
        rand_set.add(random.randint(0,300))
    sets.append(rand_set)

def random_coverage(n, s):
    cover = []
    covered = set()
    for i in range(n):
        r = s.pop(random.randint(0,len(s)-1))
        cover.append(r)
        covered |= r
    return cover, covered

def greedy_max_coverage(n, s):
    covered = set()
    cover = []
    for i in range(n):
        max_subset = max(s, key = lambda x: len(x - covered))
        cover.append(max_subset)
        covered |= max_subset
    return cover, covered

if __name__ == "__main__":
    universe = list(set(itertools.chain(*sets)))
    print("unique: " + str(len(universe)))

    cover, covered = greedy_max_coverage(10, sets)
    print(cover, len(covered))

    cover, covered = random_coverage(10, sets)
    print(cover, len(covered))
