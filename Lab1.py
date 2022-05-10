name = input("Name: ")
print(f'Hello: {name}')

x = "string"
number = 8
float = 3.16

print(f'{x} type: {type(x)}, {float} type: {type(float)}, {number} type: {type(number)}')

tab = ['x', 'x', 'x']
print(tab)

haszTab = '#'.join(tab)
print(haszTab)

tab2 = ['a', 'b', 'c']

text = "Metody Inżynierii Wiedzy Są Najlepsze"
print(f'{text}, length: {len(text)}')

textLowerCase = text.lower()
print(f'{textLowerCase}')

txtDelete = text.replace('ż', 'z')
txtDelete = text.replace('ą', 'a')
txtDelete = text.replace(' ', '')

print(f'{txtDelete}, length: {len(txtDelete)}')

set(txtDelete)

print(f'{txtDelete}, length: {len(txtDelete)}')

x = (1, 2, 3)
y = ('one', 'two', 'three')

print(f'{x} type {type(x)}')
print(f'{y} type {type(y)}')

languages = ['python', 'java', 'javaScript', 'C++', 'C']

print(f'{languages}, length: {len(languages)}')
print(languages.index('python'))

tab3 = tab+tab2

print(tab)
print(tab2)
print(tab3)

tab.extend(tab3)
print(tab)


dictionary = {"Litwa": "Wilno", "Rosja": "Moskwa", "Niemcy": "Berlin", "Ukraina": "Kijów", "Czechy": "Praga", "Białoruś": "Mińsk", "Słowacja": "Bratysława"}

print(dictionary)
print(dictionary.values())
print(sorted(dictionary))

text = "Ala ma kota a kot no jest kotem i ma ale"
setText = set(text)

if len(setText) > 15:
    print('more')
else:
    print("no")

if text[0] == 'J':
    print('ok')
else:
    print("no")

for i in range(10):
    print(i)

haszTab = str(haszTab)
result = ""

for i in range(len(haszTab)):
    if haszTab[i] != '#':
        result += haszTab[i]

print(result)

def passwd(x):
    length = len(x)
    wl = 0
    ml = 0
    wy = 0

    for i in x:
        if('A' < i < 'Z'):
            wl = wl + 1
        elif('a' < i < 'z'):
            ml = ml + 1
        elif(i == "!"):
            wy = wy + 1

    if(length > 10 and wl > 0 and ml > 0 and wy > 0):
        print("strong password")
    else:
        print("weak password")
    
passwd("Michal1231!")

def foo():
    tab = [4,6,99,2,7]

    for x in tab:
        if(x == 99):
            continue

        print(x) 

foo()

def foo1(number):
    tab = [3,4,6,7,6,3,2]
    dl = 0
    result = False

    while dl < len(tab):
        if(number == tab[dl]):
            result = True
            break

        dl = dl + 1

    return result

print(foo1(1))

def foo2():
    with open("plik.txt", "r") as f:
        for x in f:
            print(x, end="")

foo2()

def foo3():
    tab = ["Angielski", "Niemiecki", "Polski"]

    with open("plik.txt", "w") as f:
        for x in tab:
            print(x, file=f)

foo3()

def foo4():
    tab = ['Olsztyn', 'Warszawa', 'Kraków', 'Łódź']

    print(list(map(lambda x: x[:3] ,tab))) 

foo4()

def foo5(roz):
    tab = ['zad.txt', 'zad.py', 'zad.js', 'zad.doc', 'zad1.txt']

    for i in tab:
        if i.endswith(roz):
            yield i

x = list(foo5('.txt'))
print(x)
