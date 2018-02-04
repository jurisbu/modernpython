"""
2.1 Analyzing Data Using Simulations and Resampling
"""

from collections import *
from random import *
from statistics import *


def model_american_roulette(spins):
    """Model six roulete wheel spins

    American roulette has 18 red, 18 black and 2 green"""

    # Variant 1.
    population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
    # print(f'population = {population}')
    print(Counter(choices(population, k=spins)))

    # Variant 2.
    print(Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=spins)))

if __name__ == '__main__':
    model_american_roulette(6)