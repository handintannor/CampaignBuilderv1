from random import randint


def roll(sides, num=1):
    rolls = []
    total = 0
    for n in range(0, num):
        x = randint(1, sides)
        rolls.append(x)
        total += x

    # for n in rolls:
    #    print(n)

    return total


def rollstat():
    rolls = []
    total = 0
    for x in range(0, 4):
        rolls.append(roll(6))

    rolls.sort(reverse=True)

    # for n in rolls:
    #    print(n)

    for n in range(0, 3):
        total += rolls[n]

    # print(total)
    return int(total)

# def rollStats():
#    total = 0
#    rolls = []
#    for n in range(0,6):
#        rolls.append((rollstat())
#    return rolls

# def test():
#    total = 0
#    for n in range(1,6):
#        a = rollstat()
#        print(a)
#        total += a
#    total = int(total/6)
#    #print(total)
#    return total

# def test10k():
#    total = 0
#    for x in range(1,10000):
#        var = test()
#        total += var

#    print (total/10000)
#    return total/10000
