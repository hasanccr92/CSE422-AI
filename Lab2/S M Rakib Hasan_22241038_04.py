from random import randint

f = open('F://Summer 23/CSE422/Labs/Lab1/Lab2inp1.txt', 'r')
loops = 0
file = []
players = []
plrun = []
bool = 0

for i in f:
    file.append(i.replace('\n', ''))

pname, tgt = file[0].split()
pname, tgt = int(pname), int(tgt)

for i in file[1:]:
    player, prun = i.split()
    players.append(player)
    plrun.append(prun)

print(players)


def populate(n):

    par1 = [0] * n
    par2 = [0] * n

    for i in range(n):
        par1[i] = randint(0, 1)
        par2[i] = randint(0, 1)

    return par1, par2


def crossover(par1, par2):
    a = len(par1) // 2
    child1 = par1[:a] + par2[a:]
    child2 = par2[:a] + par1[a:]

    return child1, child2


def mutation(par1, par2):
    a = randint(0, len(par1) - 1)

    if par1[a] == 0:
        par1[a] = 1
    else:
        par1[a] = 0

    if par2[a] == 0:
        par1[a] = 1
    else:
        par2[a] = 0

    return par1, par2


def fitness(par1, par2):
    runpar1 = 0
    runpar2 = 0

    for i in range(pname):
        if par1[i] == 1:
            runpar1 += int(plrun[i])

        if par2[i] == 1:
            runpar2 += int(plrun[i])

    if tgt == runpar1:
        r1 = runpar1
    else:
        r1 = -1

    if tgt == runpar2:
        r2 = runpar2
    else:
        r2 = -1

    return r1, r2


def check(x, y, par1, par2):  # function for checking
    if x == -1 and y == -1:
        return False

    elif x == tgt:
        for i in par1:
            print(i,end='')
        return True

    elif y == tgt:
        for i in par2:
            print(i,end='')
        return True

    else:
        return False


while not bool:
    par1, par2 = populate(pname)
    r1, r2 = fitness(par1, par2)

    if r1 == -1 or r2 == -1:
        continue
    else:
        child1, child2 = crossover(par1, par2)
        child1, child2 = mutation(child1, child2)
        x, y = fitness(child1, child2)
        bool = check(x, y, child1, child2)

    loops += 1
    if loops == 50000:
        print(-1)
        break