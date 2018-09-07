def validateInput(val, low, high):
    if checkSent(val) is True:
        return True
    else:
        if checkInt(val) is True and checkRange(val, low, high) is True:
            return True
        else:
            return False


def checkSent(val):
    return val == "q" or "Q"


def checkInt(val):
    return val.isdigit() is True


def checkRange(val, low, high):
    if int(val) - 1 in range(low - 1, high):
        return True
    else:
        return False


def getValue(low, high):
    val = input("Please enter a number between {} and {}, or q to stop: ".format(low, high))
    while 1:
        if checkSent(val) is True:
            return -1
        if checkInt(val) is True and checkRange(val, low, high) is True:
            return int(val) - 1

        val = input("Invalid input. Please enter a number between {} and {}, or q to stop: ".format(low, high))


def testValue(val, low, high):
    while 1:
        if checkSent(val) is True:
            return -1
        if checkInt(val) is True and checkRange(val, low, high) is True:
            return int(val) - 1
        return 0
