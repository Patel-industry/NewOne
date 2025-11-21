# with the use of (yield and next) for loop use nahi karna hai 



# x=range(1000)
# print(list(x))


# def gen(n):
#     i=1
#     while i<=n:
#         yield i
#         i=i+1
    
# n=int(input("enter a number = "))
# var =gen(n)
# print (var)
# # print(list (var))
# el1=next(var)
# print(el1)
# print("hello")
# print("wellcome")
# el2=next(var)
# print(el2)



# l=list(range(1,10))
# x=iter(l)
# # print(x)
# # print(next(x))
# # print ("hello")
# # print (next(x))


# for i in x:
#     print(i)
# print(next(x))


# l=list(range(1,10))
# x=iter(l)
# for i in range(15):
#     try:
#         print(next(x))
#     except StopIteration:
#         print("itration is emty")
#         break


# x=1
# y=0
# try:
#     z=x/y
#     print(z)
# except ZeroDivisionError:
#     print("please enter non zero value")