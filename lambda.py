#  lambda :-





# x=lambda p,q,r : print (p+q+r) 
# # x(10,20,30)
# # print(x(10,20,30))
# # z=x(10,20,30)
# # print(z)
# x(10,20,30)

# x=lambda p,q :p if p>q else q
# print(x(10,20))



# map with lambda


# l=[1,2,3,4,5]
# print(list(map(lambda n:n*n,l)))


# l=[1,2,3,4,5]
# print(list(map( lambda n: 'even' if n%2==0  else 'odd' ,l)))





# filter with lambda


# / even
# l=[1,2,3,4,5]
# print(list(map(lambda n: n if n%2==0 else None,l)))


# odd
# l=[1,2,3,4,5]
# print(list(map(lambda n: n if n%2!=0 else None,l)))




# reduce wirth lambda

from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y: x+y,l))






from functools import reduce

l = [-1,1, 2, 3, 4, 5]
n = int(input("Enter which largest number you want: "))

if n <= len(l):
    for _ in range(n):
        x = reduce(lambda x, y: x if x > y else y, l)
        l.remove(x)
    print(f"{n} maximum digit is {x}")
else:
    print("Please enter valid option")
