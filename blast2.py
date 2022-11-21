def blastoff(n):
    if (n == 0):
        print("Blast off")
    else:
        print(n)
        blastoff(n - 1)


blastoff(5)
