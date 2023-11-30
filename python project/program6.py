#WAP to find smallest and largest number in list.
def find_max_min(l1):
    max_n= l1[0]
    min_n= l1[0]
    for i in l1:
        if max_n < i: max_n= i
        if min_n > i: min_n= i  
    return max_n,min_n    

mylist = [3,44,4443,567,34567,-2973,-475575]
max_num,min_num = find_max_min(mylist)
print(f"The maximium element is:{max_num}")
print(f"The minium element is:{min_num}")