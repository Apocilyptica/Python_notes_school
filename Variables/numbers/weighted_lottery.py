"""
weights = {
    'winning': 1,
    'losing': 1000
}

weighted_lottery(weights)

other_weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3
}

weighted_lottery(other_weights)
"""

# My Solution

import random

weights = ['winning'] * 1 + ['break_even'] * 2 + ['losing'] * 3
choice = random.choice(weights)

print(choice)

# JH Solution

import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

other_weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3
}

print(weighted_lottery(other_weights))
