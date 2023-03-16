# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(lst):
    del lst[0], lst[-1]


chop([1, 2, 3])


def middle(lst):
    return lst[1:-1]


my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)
print(chop_list)

middle_list = middle(my_list2)
print(my_list2)
print(middle_list)
