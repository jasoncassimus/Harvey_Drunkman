from walk import Harvey, Direction, Map, simulate
import random
from functools import reduce


def run_sim(times):
    i = 0
    while i < times:
        yield simulate()
        i += 1


SIMULATIONS = 3500

sims = [simulate() for _ in range(0, SIMULATIONS)]
sums = map(lambda result: result[0], sims)
outcomes = map(lambda result: result[0], sims)

pos_outcomes = 0
neg_outcomes = 0
for i in outcomes:
    if i:
        neg_outcomes += 1
    else:
        pos_outcomes += 1

flower_cost = map(lambda cost: cost * 3.00, sums)
avg_cost = sum(flower_cost) / SIMULATIONS
print("Average flower price: " + format(avg_cost, 'f'))
print('Times Harvey stumbled home: ' + str(pos_outcomes))
print("Times Harvey Drowned: " + str(neg_outcomes))


