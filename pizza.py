name = input("What is your name?: ")
# Has to be a word, need to enforce this
print("Hello", name)

try:
    hours = float(input("How many hours did you work?: "))
    rate = float(input("What is your hourly rate: $"))
    if hours > 40:
        pay = round((hours*(rate*1.5)), 2)
    elif hours <= 0:
        pay = 0
    else:
        pay = round((hours*rate), 2)
    print("Your pay is $", pay)
except:
    print("Please enter a number")


pizzaSale = ''
slicePrice = 1
pizzaPrice = (slicePrice * 7)
pizza = 8


def saleTime():
    print("The cost will be", round((salePrice), 2))
    if (pay >= salePrice):
        print(f"There are {pizza-slices} slices left in this pizza")
        print("Your remaining pay is $", float((pay-salePrice)))
    else:
        print("You too broke")


pizzaSale = input("Did you want some pizza? Yes or No? ")
if pizzaSale.capitalize() == "Yes":
    print("A slice is $", slicePrice, "and a whole pizza is $", pizzaPrice)
    slices = int(input("How many slices did you want?: "), 0)
    if slices < 8 and slices > 0:
        salePrice = (slices*slicePrice)
        saleTime()
    elif slices == 8:
        salePrice = pizzaPrice
        saleTime()
    else:
        print("Slices or a whole pizza are your only options.")

elif pizzaSale.capitalize() == "No":
    print("Who hates pizza? What is wrong with you?")

else:
    print("It's a Yes or No question...")


# width = 17
# height = 12

# test1 = width//2
# test2 = width/2.0
# test3 = height/3
# test4 = 1 + 2 * 5

# print(test1, test2, test3, test4)
