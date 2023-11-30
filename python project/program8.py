#make a list of first 10 letter of alphabet then use the slicing to do the following operation
# print the first 3 letter of the list
# print any 3 letter from the middle
# print the letter from any particular index to the end of list
from random import randint

list1 =list("abcdefghij")

rand = randint(0,9)

print(f"The first 3 letter of the list are:{list1[:3]}")
print(f"Any 3 letter from the middle are:{list1[4:7]}")
print(f"the letter from any particular index {rand} to the end of list are :{list1[rand:]}")
