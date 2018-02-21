def interpret(code):
    pinakas = [0]
    position = 0
    i = 0
    c = 0
    print(code)
    while i < len(code):
        if code[i] == '<':
            if position > 0:
                position -= 1
        elif code[i] == '>':
            position += 1
            if len(pinakas) <= position:
                array.append(0)
        elif code[i] == '+':
            pinakas[position] += 1
        elif code[i] == '-':
            if pinakas[position] > 0:
                pinakas[position] -= 1
        elif code[i] == '.':
            print(pinakas[position], chr(pinakas[position]))
        elif code[i] == ',':
            x = input("Input:")
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            pinakas[position] = y
        elif code[i] == '[':
            if pinakas[position] == 0:
                open_braces = 1
                while open_braces > 0:
                    i += 1
                    if code[i] == '[':
                        open_braces += 1
                    elif code[i] == ']':
                        open_braces -= 1
                    elif code[i] == ']':
                        # you don't need to check array[position] because the matching '[' will skip behind this instruction if array[position] is zero
                        open_braces = 1
                while open_braces > 0:
                    i -= 1
                    if code[i] == '[':
                        open_braces -= 1
                    elif code[i] == ']':
                        open_braces += 1
                        i -= 1
        i += 1
interpret("""
            Edw mpainei o kwdikas brainfuck
""")
