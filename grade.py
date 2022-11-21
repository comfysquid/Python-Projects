score = input("Please type a score between 0.0 and 1.0: ")
try:
    def computegrade():
        if float(score) < 0 or float(score) > 1.0:
            print("fuck you")
        elif float(score) >= 0.9:
            print("A")
        elif float(score) >= 0.8:
            print("B")
        elif float(score) >= 0.7:
            print("C")
        elif float(score) >= 0.6:
            print("D")
        elif float(score) > 0:
            print("F")
    computegrade()
except:
    print("Bad score.  Please run the program again.")
