'''
# collection of 'key':'value' pair
# 2.key must be unique
# 3.value may be dupilcate
# 4.reprented by { }with comma (,) seperated elements
# 5.maped data type 
# 6. indexing not suppported
# 7. slicing not suppported
# 8.mutable in nature
# 9.both key and value are either homogenous or hetrogenous

# Ex:-

# d={ 'name':'paras','age':20}
# print(d,type(d))


python  in-built function:-
 
 1.len():-print(len(t))
 2.type():-print(tpye(t))
 3.print():-print(t)
 4.id():-print(id(t))
 5.max():-print(max(t))
 6.min():-print(min(t))
 7.sum():-print(sum(t))
 

# d={ 'name':'paras','age':20}
# print(d,len(d))


# d={ 'name':'paras','age':20}
# print(d,type(d))

# d={ 'name':'paras','age':20}
# print(d,id(d))

# d={ 'name':'paras','age':20}
# print(d)

# d={ 'name':'paras','age':20}
# print(d,max(d))

# d={ 'name':'paras','age':20}
# print(d,min(d))

# d={ 'name':'paras','age':20}     #error
# print(d,sum(d))


# d={ 4:'paras',4:20}
# print(d,max(d))

# d={ 4:'paras',5:20}
# print(d,min(d))

# d={ 4:'paras',5:20}    
# print(d,sum(d))



# methods:-


1.clear():-
2.copy():-
3.formkey():-
4.get():-
5.items():-
6.keys():-
7.pop():-
8.popitem():-
9.setdefault():-
10.update():-
11.values:-

'''


# 1.copy:-

# d={'name':'Paras','age':20}
# d1=d.copy()
# print(d,d1)
# print(id(d),id(d1))



# 2.clear():-


# d={'name':'Paras','age':20}
# d.clear()
# print(d)
# del d
#  print(d)                            //delete d
 

 
# 3. get():-dict.get('key',''defualt value)

 
# d={'name':'Paras','age':20}
# print(d.get('name','guest'))

 
# d={'name':'Paras','age':20}
# print(d.get('name'))                         //paras



# d={'name':'Paras','age':20}
# print(d.get('Name','guest))                  //guest



# 4.keys()
# d={'name':'Paras','age':20}
# print(d.keys())



# 5.values()

# d={'name':'Paras','age':20}
# print(d.values())


# 6.items():-

# d={'name':'Paras','age':20}
# print(d.items())



# 7.update():-


# d={'name':'Paras','age':20}
# d2={'x':10,'age':5}
# d.update(d2)
# print(d)


# 8.setdifulat():-



# d={'name':'Paras','age':20}
# print(d.setdefault('name','ayush'))
# print(d)



# 9.fromkeys():-





# 10. pop():-



# d={'name':'Paras','age':20}
# d.pop('age')
# print(d)



# 11.popitem():-

# d={'name':'Paras','age':20}
# d.popitem()
# print(d)








