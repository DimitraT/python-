def miden(numbers,l):

    f = 0
    for i in range(0,len(numbers)-2):
        sum = numbers[i]
        for j in range(i+1,len(numbers)-1):
            for k in range(j+1,len(numbers)):
                if (numbers[i] + numbers[j] + numbers[k] == 0):
                    print(numbers[i],numbers[j],numbers[k])
                    f = 1

    if (f == 0):
        print("Den yparxoun syndyasmoi!")


import random
numbers = random.sample(xrange(-30,30),30)
l = len(numbers)
print("Oi syndyasmoi einai oi akolouthoi: ",numbers)
miden(numbers,l)
