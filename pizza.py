name = input("What is your name?: ")
# Has to be a word, need to enforce this
print("Hello", name)


def saleTime():
    print("The cost will be", round((salePrice), 2))
    if (x >= salePrice):
        print(f"There are {pizza-slices} slices left in this pizza")
        print("Your remaining pay is $", float(round((x-salePrice), 2)))
    else:
        print("You too broke")


try:
    hours = float(input("How many hours did you work?: "))
    rate = float(input("What is your hourly rate: $"))
    if hours <= 40 and hours > 0:
        def computepay(hours, rate):
            wages = hours*rate
            return wages
        x = computepay(hours, rate)
        print("Pay: $", round((x), 2))
    else:
        overhours = hours - 40

        def computepay(overhours, rate):
            wages = ((overhours * rate) * 1.5) + (40 * rate)
            return wages
        x = computepay(overhours, rate)
        print("Pay: $", round((x), 2))
except:
    print("Please enter a number")


pizzaSale = ''
slicePrice = 1
pizzaPrice = (slicePrice * 7)
pizza = 8

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
