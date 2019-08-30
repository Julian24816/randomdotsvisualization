from helpers import fill
from random import random

def weighted_choice(*weights):
    def choice(seq):
        w = fill(weights, len(seq), 1)
        c = random() * sum(w)
        acc = 0
        for index, item in enumerate(seq):
            acc += w[index]
            if acc > c:
                return item
    return choice

def alwayscolor(color):
    lambda i, d: color

def randomcolor(*colors):
    return lambda i, d: random_choice(colors)

def vertexcolor(*colors):
    return lambda i, d: colors[i]

def depthcolor(*colors):
    return lambda i, d: colors[min(len(colors) - 1, d)]
