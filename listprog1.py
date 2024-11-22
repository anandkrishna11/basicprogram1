'''author:Anand Krishna M A
description:program to merge 2 list such that in the merge list, all even numbers occur first followed by odd numbers.both the even numbers and odd numbers should be in sorted order
date-22/11/24'''

lst1=[2,9,88,3,99]
lst2=[11,65,99,6]
print(f"given list 1={lst1} and list 2={lst2}" )
lst3=lst1+lst2
even_lst=[]
odd_lst=[]
for i in lst3:
    if i % 2 == 0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(f"even_list={even_lst} and odd list={odd_lst}")
even_lst.sort()
odd_lst.sort()
print(f"list after sort={even_lst} and {odd_lst}")
print(f"final list={even_lst+odd_lst}")
