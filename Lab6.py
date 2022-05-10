import math as m
import numpy as np

tab = []

with open("australian.dat", "r") as file:
    tab = [list(map(lambda a: float(a), line.split())) for line in file]

tab = [x[:14] for x in tab]

def arithmeticAverage(tab):
    ones = np.ones((len(tab), 1))
    return float(1/len(tab))*np.dot(np.array(tab), ones)[0]

print(arithmeticAverage(tab[0]))

def varianceTab(tab):
    average = arithmeticAverage(tab)
    ones = np.ones((1, len(tab)))*average
    minus = np.array(tab) - ones
    return float(1/len(tab))*np.dot(minus[0], minus[0].T)

print(varianceTab(tab[0]))

def deviationStandardTab(tab):
    return m.sqrt(varianceTab(tab))

print(deviationStandardTab(tab[0]))
