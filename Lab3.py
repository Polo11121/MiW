import math
import numpy as np

tab = []

with open('australian.dat', 'r') as file:
    for line in file:
        tmp = line.split(sep=" ")
        tmp = list(map(lambda e: float(e), tmp))
        tab.append(tmp)


def euclideanMetric(l1, l2):
    sum = 0

    for i in range(max(len(l1),len(l2))-1):
        sum += (( l1[i] - l2[i])**2)

    return math.sqrt(sum)


def euclideanMetricW(l1, l2):  
    w1 = np.array(l1[:-1])
    w2 = np.array(l2[:-1])
    x = w1 - w2
    
    return math.sqrt(np.dot(x, x))

print(euclideanMetricW(tab[0], tab[1]) == euclideanMetric(tab[0], tab[1]))

def listDivision(x, matrix):
    tab = []

    for i in matrix:
        odl = euclideanMetric(x, i)
        tab.append((i[-1], odl))

    return tab

result = listDivision([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], tab)

def createDict(tab):
    dictionary = dict()

    for i in tab:
        key = i[0]

        if key not in dictionary.keys():
            dictionary[key] = []

        dictionary[key].append(i[1])

    return dictionary

dictionary = createDict(result)

def k_nn(dictionary, k):
    groups = dict()

    for key in dictionary:
        sortedDict1 = sorted(dictionary[key])
        sortedDict = sortedDict1[:k]
        result = sum(sortedDict)
        groups[key] = result

    return groups

groups = k_nn(dictionary, 5)

def decision(who, tab, k):
    grouped = listDivision(who, tab)
    groupedDict = createDict(grouped)
    smallest = k_nn(groupedDict, k)
    keys = list(smallest.keys())
    classDecisionResult = keys[0]
    count = 1

    for i in range(1, len(keys)):
        if smallest[keys[i]] == smallest[classDecisionResult]:
            count += 1

        elif smallest[keys[i]] < smallest[classDecisionResult]:
            classDecisionResult = keys[i]
            count == 1

    if count > 1:
        return

    else:
        return classDecisionResult

decision([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], tab, 5)

def grouped(tab, who, index):
    result = dict()
    y = tab[who]

    for i in range(1, len(tab)):
        decision = tab[i][index]

        if decision in result.keys():
            result[decision].append(euclideanMetric(y, tab[i]))

        else:
            result[decision] = [euclideanMetric(y, tab[i])]

    return result

print(grouped(tab, 0, 3))
