a = "7"
b = "2"
c = "15"
d = "50"
choice = input(("What is 5*3, Is it",
                a & "\n",
                b + "\n",
                c + "\n",
                d + "\n",
                ))
if choice.capitalize == a:
    print("Incorrect1")
elif choice.capitalize == b:
    print("Incorrect2")
elif choice.capitalize == c:
    print("Correct")
elif choice.capitalize == d:
    print("Incorrect3")

choice = input(
    "What is the capital of Australia, Is it\na) Canberra \nb) Sydney\nc) Brisbane\nd) Uluru\n")
if choice.capitalize == "a" or "Canberra":
    print("Correct")
elif choice.capitalize == "b" or "Sydney":
    print("Incorrect")
elif choice.capitalize == "c" or "Brisbane":
    print("Incorrect")
elif choice.capitalize == "d" or "Uluru":
    print("Incorrect")


choice = input(
    "What car does Lincoln own?, Is it\na) CRV\nb) Mazda3\nc) S660\nd) MX5\n")
if choice.capitalize == "a" or "CRV":
    print("Incorrect")
elif choice.capitalize == "b" or "Mazda3":
    print("Correct")
elif choice.capitalize == "c" or "S660":
    print("Incorrect")
elif choice.capitalize == "d" or "MX5":
    print("Correct")
