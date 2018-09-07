from dice import *
from stats import *
from verify import *


def main():
    a = Stats()
    a.rollStats()
    a.assignStats()

    for n in a.attributes:
        print(n.name, n.value)

    a.rollStats()
    a.assignStats()

    for n in a.attributes:
        print(n.name, n.value)

    return


main()
