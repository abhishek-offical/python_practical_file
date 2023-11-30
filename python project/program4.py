# WAP to swap a two strings.
def Swap_string(s1,s2):
    print("Before swap value:")
    print("str1 :",s1)
    print("str2 :",s2)

    s1,s2 = s2,s1

    print("\nAfter swap value:")
    print("str1 :",s1)
    print("str2 :",s2)

str1 ="Hello"
str2 ="World"
Swap_string(str1,str2)