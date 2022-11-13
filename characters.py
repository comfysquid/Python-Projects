# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

# fruit = input("Enter your favourite fruit: ")
# index = len(fruit) - 1
# while index >= 0:
#     letter = fruit[index]
#     print(letter)
#     index -= 1

# Exercise 3: Encapsulate this code in a function named count, and
# generalize it so that it accepts the string and the letter as arguments.


def counter(s, l):
    string = str(s)
    letter = str(l)
    count = 0
    for i in string:
        if i == letter:
            count = count + 1
        print(count)


counter('banana', 'a')

counter('paypal', 'p')
