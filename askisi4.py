roman = []
integer = input ("Type a number between 1 and 1000000:")
piece = 0
if integer>1000000 or  integer<=0 :
    print ("Give me a number between 1 and 1000000")

elif integer == 1000000:
    print ("The roman number is -M")

else:
    if integer >= 100000:
        piece = integer / 100000
        if piece == 9:
            roman.append("-C-M")
        elif piece >=5:
            roman.append("-D")
            for i in range (piece - 5):
                roman.append("-C")
        elif piece == 4:
            roman.append("-C-D")
        elif piece >=1 :
            for i in range (piece):
                roman.append("-C")
        integer = integer % 100000
    if integer >= 10000:
        piece = integer/10000
        if piece == 9:
            roman.append("-X-C")
        elif piece >= 5 :
            roman.append("-L")
            for i in range (piece - 5):
                roman.append("-X")
        elif piece == 4:
            roman.append("-X-L")
        elif piece >= 1:
            for i in range (piece):
                roman.append("-X")
        integer = integer % 10000
    if integer >= 1000:
        piece = integer/1000
        if piece == 9:
            roman.append("-I-X")
        elif piece >=5:
            roman.append("-V")
            for i in range (piece - 5):
                roman.append("-I")
        elif piece == 4:
            roman.append("-I-V")
        elif piece >=1:
            for i in range (piece):
                roman.append("M")
        integer = integer % 1000
    if integer >= 100:
        piece = integer / 100
        if piece == 9:
            roman.append("CM")
        elif piece >= 5:
            roman.append("D")
            for i in range (piece - 5):
                roman.append("C")
        elif piece == 4:
            roman.append("CD")
        elif piece >= 1:
            for i in range(piece):
                roman.append("C")
        integer = integer % 100
    if integer >= 10 :
        piece = integer / 10
        if piece == 9 :
            roman.append("XC")
        elif piece >= 5 :
            roman.append("L")
            for i in range (piece - 5):
                roman.append("X")
        elif piece == 4:
            roman.append("XL")
        elif piece >=1 :
            for i in range (piece):
                roman.append("X")
        integer = integer % 10
    if integer >=1 :
        piece = integer
        if piece == 9:
            roman.append("IX")
        elif piece >=5 :
            roman.append("V")
            for i in range (piece - 5):
                roman.append("I")
        elif piece == 4:
            roman.append("IV")
        elif piece >= 1:
            for i in range (piece):
                roman.append("I")
    print("The roman number is: ")
    print "".join(roman)
