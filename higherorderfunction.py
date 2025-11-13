# higher ortder funtion
# 1.map()
# 2.filter()
# 3.reduce()
# 4.decoraters()


# 1.map()
# syntax:-collection/iterable
# def funtion_name(m1,n2,n3,...)
# print(list(n))


# l=[1,2,3,4,5]
# l1=[6,7,8,9]
# l2=[11]
# def sqare(x,y,z):
#     return (x+y+z)
# res=map(sqare,l,l1,l2)
# print(tuple(res))

# l1,l2,l3=[1,2,3],[1,2,3,4],[1,2,3,4,5]
# def add(x,y,z):
#     return x+y+z
# prin(list(map(add,l1,l2,l3)))





# 2.filter:-iterable 


# s=[50,60,79,56,30,90,100]
# def first_div(n):
#     if n>=60:
#         return n
# print(list(filter(first_div,s)))



# c=input("enter a name : ")
# def char(n):
#    if n in ('a','e','i','o','u','A','E','I','O','U'):
#     return n 

# res=list(filter(char,c))
# print(''.join(res))

# s=input("enter a number")
# s1=''
# for i in s:
#     if i in ('a','e','i','o','u','A','E','I','O','U'):
#         s1=''.join([s1,i])
# print(s1)

# s=input("enter a string")
# v=c=0
# for i in s:
#     if i  in ('a','e','i','o','u','A','E','I','O','U'):
#         v=v+1
#     elif i=='':
#         pass
#     else:
#         c=c+1







# 3.reduce():-
# syt :- 

import functools

# l=[1,2,3,4,5,6,7]

# def sum(x,y):
#     print(x,y)
#     return x+y
# res= functools.reduce(sum,l)
# print(res)




# que max

# l=[10,203,303,404,505]
# def maxdigit(x,y):
#     if x>y:
#         return x
#     else: return y
# res=functools.reduce(maxdigit,l)
# print(res) 



# # que min

# l=[10,203,303,404,505]
# def mindigit(x,y):
#     if x<y:
#         return x
#     else: return y
# res=functools.reduce(mindigit,l)
# print(res) 




