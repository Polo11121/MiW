from doctest import master
import math
from random import randint

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


def massCenter(index: list, tab: list):
    distance = []
    tmp = 0

    for i in index:
        for j in index:
            tmp += euclideanMetric(tab[i], tab[j])

        distance.append(tmp)
        tmp = 0

    min = 0

    for i in range(1, len(distance)):
        if distance[min] > distance[i]:
            min = i

    return min


def randomDecision(tab):
    for i in range(len(tab)):
        tab[i][len(tab[i])-1] = float(randint(0, 1))

    return tab


def colors(tab):
    newRandomTab = randomDecision(tab)
    changes = True

    while(changes):
        changes = False
        groups = dict()

        for i in range(len(newRandomTab)):
            decision = newRandomTab[i][-1]

            if decision in groups.keys():
                groups[decision].append(i)
            else:
                groups[decision] = [i]

        newTab = []

        for ele in groups.values():
            newTab += ele

        centers = []

        for tab in groups.values():
            centers.append(tab[massCenter(tab, newRandomTab)])

        distances = []

        for ele in newTab:
            for sr in centers:
                distances.append(euclideanMetric(
                    newRandomTab[ele], newRandomTab[sr]))

            min = 0
            count = 1

            for i in range(1, len(distances)):
                if distances[min] > distances[i]:
                    min = i
                    count = 1

                elif distances[min] == distances[i]:
                    count = count+1

            if count == 1:
                if newRandomTab[ele][-1] != newRandomTab[centers[min]][-1]:
                    newRandomTab[ele][-1] = newRandomTab[centers[min]][-1]
                    changes = True

            elif count > 1:
                newRandomTab[ele][-1] = None
                changes = True

            distances = []

    return newRandomTab

new_matrix = colors(tab)
groups = dict()

for i in new_matrix:
    decision = i[14]

    if decision in groups.keys():
        groups[decision].append(i)
    else:
        groups[decision] = [i]

for key in groups.keys():
    print("{0}: {1}".format(key, len(groups[key])))
