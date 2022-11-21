# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

fruit = input("Enter your favourite fruit: ")
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1

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

# Exercise 4: There is a string method called count that is similar to
# the function in the previous exercise. Read the documentation of this
# method at:
# https://docs.python.org/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter a occurs
# in “banana”.

line = "banana"
count = line.count("a")
print(count)

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'

start = str.find(':')
print(start)
end = len(str)
print(end)
number = str[start+1:end]
print(number)
fpnumber = float(number)
print(fpnumber)
