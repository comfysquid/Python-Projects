try:
    score = float(input("Enter score: "))
except:
    print("Bad score, Enter a valid score")
    quit()

if score > 1.0 or score < 0.0:
    print("Bad score, enter a valid score")
    quit()

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= (0.6):
    print("D")
elif score < 0.6:
    print("F")
