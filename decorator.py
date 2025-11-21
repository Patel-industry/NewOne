# def outer_fun(var):
#     def inner_fun(x,y):
#         x=x+5
#         y=y+5
#         var(x,y)
#     return inner_fun
# @outer_fun
# def add(p,q):
#     print(p+q)
    
# x=int(input("enter x"))
# y=int(input("enter  y"))
# add(5,5)




def outer_fun(var):
    def inner_fun(x):
        var(x)
        value=range(1,n+1,2)
    
        return list(value)
    return inner_fun
@outer_fun
def add(n):
    x=range(2,n+1,2)
    return list(x)
n=int(input("enter x = "))
res=add(n)
print(res)