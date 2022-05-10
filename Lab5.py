import random

def montecarlo(foo, foo2, fx, lx, eps):
    start = foo2(lx)-foo2(fx)
    result = 0
    points = 1000
    count = 0
    min = foo(fx)
    max = foo(lx)
    randoms = []

    while(abs(result-start) > eps):
        points += 1000

        for i in range(1000):
            x = random.uniform(fx, lx)
            y = random.uniform(min, max)

            randoms.append((x, y))
            result = foo(x)

            if(y <= result):
                count += 1

        wyn = (lx-fx)*(max-min)*(count/points)

    return wyn


def foo2(x):
    return x**2/2


def foo(x):
    return x

print(montecarlo(foo, foo2, 0, 1, 0.05))
