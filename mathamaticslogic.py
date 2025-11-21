# 1.natural number


# n=10
# for i in range(1,n+1):
#     print (i)


# 2.even number 

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if i %2 ==0:
#         print(i)


# 3. odd number 

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i)


# 4.factor of given number

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# 5.factorial number

# n=int(input("enter a number = "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)


# 6.armstronge

# n=int(input("enter a number"))
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum+=digit **3
#     temp//=10
# if sum == n:
#     print("armstronge")
# else:
#     print("not armstronge")



# # 7.palendrome in string

# n= input("enter a number")
# if n == n[::-1]:
#     print ("palendrome")
# else:
#     print ("not a palrendrome")
    
    
#  7.palendrome in number

# n= input("enter a number")
# s=str(n)
# if n == n[::-1]:
#     print ("palendrome")
# else:
#     print ("not a palrendrome")


# 8.hcf
# a=4
# b=6
# gcd=1
# if a>b:
#     i=1
#     while i<=a:
#         if a%i==0 and b%i==0:
#             gcd=i
#         i=i+1
# else:
#     i=1
#     while i<=b:
#         if a%i==0 and b%i==0:
#             gcd=i
#         i=i+1 
# print(gcd)          





# 9.lcm
# a=4
# b=6
# gcd=1
# lcm=1
# if a>b:
#     i=1
#     while i<=a:
#         if a%i==0 and b%i==0:
#             gcd=i
#         i=i+1
# else:
#     i=1
#     while i<=b:
#         if a%i==0 and b%i==0:
#             gcd=i
#         i=i+1 

# print(gcd)          
# lcm=a*b//gcd
# print(lcm)


# 10.Fibonacci:--

# n=5
# s=0
# ne=1
# ss=1
# for i in range(1,n+1):
#     s=ne
#     ne=ss
#     ss=s+ne
#     print (s)
    
    
# 11.anagram 



# a=input("words")
# b=input("words")
# if sorted(a) == sorted(b):
#     print ("anagram")
# else:
#     print("not a anagram")



# 12.neon number

# n=9
# sq=n*n
# sum=0
# while sq > 0:
#     summ=sq%10
#     sum=sum+summ
#     sq=sq//10

# if sum==n:
#     print("neon")
# else:
#     print("not neon")
    
    
# 13.leaf year      
# n=int(input("enter a year"))
# i=1
# while 0<=8n:
#     if (i%400==0) or (i%4==0 and i%100!=0):
#         print("leaf year",i)
#     else:
#         print ("not a leaf year",i)
#     i=i+1    

n = int(input("enter a year"))
i = 1

while i <= n:
    if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        print("leap year", i)
    else:
        print("not a leap year", i)
    i = i + 1
