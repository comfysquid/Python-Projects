name = input("What is your name?: ")
print("Hello", name)

hours = float(input("How many hours did you work?: "))
rate = float(input("What is your hourly rate: "))

pay = round((hours*rate), 2)

print("Your pay is", pay)


pizzaSale = ''
slicePrice = 1.50
pizza = 8

pizzaSale = input("Did you want a slice of pizza? Yes or No? ")
if pizzaSale.capitalize() == "Yes":
    slices = int(input("How many slices did you want?: "), 0)
    if slices <= 8:
        salePrice = (slices*slicePrice)
        print("The cost will be", round((salePrice), 2))
        if (pay >= salePrice):
            print("There are {} slices left".format(pizza-slices))
            print("Your remaining pay is ", float((pay-salePrice)))
        else:
            print("You too broke")
    else:
        print("We've only got 8 slices")

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
