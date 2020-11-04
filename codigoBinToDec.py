def binToDec(binarystring):
    sum = 0
    base = 1
    for i in reversed(list(str(binarystring))):
        sum = sum + (base * int(i))
        base = base * 2
    print(sum)

#binToDec()