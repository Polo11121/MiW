import math

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


def astrGroup(tab, index,who):
    result = dict()
    y = tab[who]

    for i in range(1, len(tab)):
        dec = tab[i][index]

        if dec in result.keys():
            result[dec].append(euclideanMetric(y, tab[i]))
        else:
            result[dec] = [euclideanMetric(y, tab[i])]

    return result

tmp = astrGroup(tab, 0, 14)
print(tmp)


