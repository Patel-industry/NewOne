'''list = collection of elements [homogeneos,hetrogenous]
represted by [ ]with comma(,)seprated elements
sequential / orederd sopported
slicing supported
duplicates are allowed
mutable in nature

Ex: my_list=[10,20,30,40,50,60,'python','java']
print(my_list,type(my_list))






#python in-built function
1. len()
2. type()
3. id()
4. sum()
5. min()
6. max()
7. print()






l=[10,20,30,40,50,60,'python','java']
print(len(l))

l=[10,20,30,40,50,60,'python','java']
print(type(l))

l=[10,20,30,40,50,60,'python','java']
print(id(l))

l=[10,20,30,40,50,60,'python','java']
print(l)

l=[10,20,30,40,50,60,'python','java']
print(max(l))

l=[10,20,30,40,50,60,'python','java']
print(min(l))

l=[10,20,30,40,50,60,'python','java']
print(sum(l))












# l=['python','java','PHP']
# print(max(l))


# l=['python','java','PHP']
# print(min(l))


# l=['python','java','PHP']
# print(sum(l))                   error


l=[10,20,30.0,40.0,10.8]
print(max(l))


l=[10,20,30.0,40.0,10.8]
print(min(l))


# l=[10,20,30.0,40.0,10.8]
# print(sum(l))













l=[10,20,30.0,40.0,10.8j]
 print(sum(l))
 
 
l=[10,20,30.0,40.0,10.8j]      error
 print(max(l))



l=[10,20,30.0,40.0,10.8j] error
 print(min(l))








#methods in list

1.copy()    = creaate new object with same elements
2.clear()   = remove all elements from given list
3.append()  = add single elements at last positin
4.extend()  = add multiple elements at last postion 
5.pop()     = remove index targeted elements by difault index is -1 i.e it remove last elements
6.remove()  = remove targeted elements from list 
7.index()   = return index number against given elements
8.count()   = find frequency/occurence of any elements
9.sort()    = arrange in assending order
10.reverse()= reverse out all the elements all the elements
11.insert() = add elements in targeted position



explain all the menthods 

1.copy():-

#li=[2,3,'python']
# l1=l.copy()
# print(id(l),id(l1))


# 2.clear:-
# t=[2,3,'python']
# t.clear()
# print(t)
# del t 
# print(t)

# s='python' error
# print(s)
# del s
# print(s)


# 3.append():-

# l=[2,3,4,5,'pytthon','java']
# l.append('cpp')
# print(l)

# l=[2,3,4,5,'pytthon','java']
# l.append([1,2,3,4])
# print(l)



#  4.extend()
 
# l=[2,3,4,5,'pytthon','java']
# l.extend('python')
# print(l)



# 5.insert() :- list.insert(postion,elements)
 
 
l=[1,2,3,3]
l.insert(0,100)
print(l)

 
#  * interview
 
 
# l=[1,2,3,3]
# l.insert(100,'python')
# print(l)


# l=[1,2,3,4]
# l.insert(2,[100,500,600])
# print(l)


# 6.pop():- list.pop() work on index

# l=[2,3,4,5,'python']
# print(l.pop())
# print(l)

# l=[2,3,4,5,'python']
# print(l.pop(0))
# print(l)

# l=[2,3,4,5,'python']          error
# print(l.pop(8))
# print(l)


# 7.remove():- sytx:-list.remove()

# l=[2,3,4,5,'python']          
# l.remove(4)
# print(l)



# 8.index():- Sytx:- list.index()

# l=[2,3,4,5,'python']          
# print(l.index(2))

# l=[2,3,4,5,2,'python'] 
# print(l.index(2,(l.index(2)+1)))    


#9.count():- syt:-list.count('element')

# l=[1,2,3,4,5,3,2,1,1]
# print(l.count(3))

# l=[1,2,3,4,5,3,2,1,1]
# print(l.count(100))

# l=[]
# print(l.count())  //error



# 10.sort():-sytx:-

# l=[2,1,3,5,2]
# l.sort()
# print(l)


# 11.reverse():-

# l=[2,1,3,5,2]
# l.reverse()
# print(l)


'''


