from random import sample
def makelist(size):
    a = []
    f = open(f"ordered{size}.txt", "x")
    for i in range(1, size+1):
        a.append(i)
        f.write(f"{i}\n")
    f.close()
    f = open(f"reverse{size}.txt", "x")
    for i in range(size, 0, -1):
        f.write(f"{i}\n")
    f.close()
    b = sample(a, size)
    c = sample(b, size)
    f = open(f"random{size}one.txt", "x")
    for i in range(size):
        f.write(f"{b[i]}\n")
    f.close()
    f = open(f"random{size}two.txt", "x")
    for i in range(size):
        f.write(f"{c[i]}\n")
    f.close()

def makeRandList(size, l):
    temp = list(range(size))
    for i in l:
        temp = sample(temp, size)
        f = open(f"./Data/Random/{size}/random{size}_{i}.txt", "x")
        for n in temp:
            f.write(f"{n}\n")
        f.close()


l = list(range(1, 11))

sizes = [64, 256, 512, 1024, 4096, 8192, 32768, 1048576, 33554432]


makeRandList(536870912, l)

