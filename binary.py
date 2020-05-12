"""
This function will take value from user
"""
def insert_val():
    val = int(input("Enter a number\n"))
    num = val
    bine = []
    while num > 0:
        if num % 2 == 0:
            bine.insert(0, 0)
            num = num // 2
        elif num % 2 != 0:
            bine.insert(0, 1)
            num = num //2

    while len(bine) != 8:
        bine.insert(0, 0)

    res = "".join(str(san) for san in bine)

    val1 = int(input("Enter a number\n"))
    num1 = val1
    bine1 = []
    while num1 > 0:
        if num1 % 2 == 0:
            bine1.insert(0, 0)
            num1 = num1 // 2
        elif num1 % 2 != 0:
            bine1.insert(0, 1)
            num1 = num1 //2

    while len(bine1) != 8:
        bine1.insert(0, 0)

    return bine, bine1

