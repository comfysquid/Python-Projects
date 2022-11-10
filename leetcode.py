# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

count = 0
total = 0
avg = 0

# while True:
#     line = input("Enter a number: \n")
#     try:
#         line = float(line)
#         count = count + 1
#         total = total + line
#         avg = total / count
#     except:
#         if line == "done":
#             break
#         else:
#             print("Invalid input)")
#             continue
# print(count, total, avg)

# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.


largest = None

while True:
    line = input("Enter a number: \n")
    for i in line:
        if largest is None or i > largest:
            largest == i
        print("Loop: ", i, largest)
        print("Largest: ", largest)
    try:
        line = float(line)
        count = count + 1
        total = total + line
    except:
        if line == "done":
            break
        else:
            print("Invalid input)")
            continue
print({"Count": count, "Total": total, "Minimum": min(line), "Maximum": max(line)})
