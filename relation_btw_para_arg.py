# def arg(a=0,s=0,c=0):
#     pass
#     print(a,s,c)

# arg(1,2,34,4)


# def ad(*args):
#     print(args)
#     print(type(args))
    
# ad(1,2,3,3,4,"python",[1,2,3])

# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#         print("sum",sum)
        
# add(10,20,390,40,)  
# x=(10)
# y=5
# print(type(x), type(y))

# p=10,
# print(type(p))

# q=(10,)
# print(type(q))

# def add(* n):
#  print(n)
#  print(type(n))
# x=eval(input("enter tuple values"))
# add()


# def add(*n):
#     sum=0
#     for i in n:
#         for j in i:
#             sum=sum+j
#     print("sum",sum)
    

# x=eval(input("enter a any tuple value"))
# add(*x)

# def add(x,y=0,*z):
#     print(x)
#     print(y)
#     print(z)
    
# add(1,2,3,4,5,5,6,6,6)

# def add(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# add(y=555,j=5,z=23)

# def add(x,y,z):
#     print(x,y,z)
# add(x=10,y=20,z=30)

def add(**n):
    print(n,type(n))
add(x=10,y=20,z=30)