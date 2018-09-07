from dice import *
from stats import *
from verify import *


def main():
    for x in range(0, 31):
        Str = Attribute("Str", x)
        print(x, (Str.calcMod()))

main()