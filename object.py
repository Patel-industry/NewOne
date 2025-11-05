'''
Immutable                             Muntetable

1.int,                                 1.list,
2.float,                               2.dict,
3.complex,                             3.set.
4.string,
5.tiple,
6.frozenset,
7.boolean
8.None.





x=10
y=20
print(id(x),id(y))


a=12.2
b=23.33
print(id(a),id(b))


c="paras"
d="paras"
print(id(c),id(d))


a=[10,20,30,"paras"]
b=[10,20,30,"paras"]
print(id(a),id(b))

set=> mutable


a={10,20,"paras"}

b={10,20,"paras"}
print(id(a),id(b))


frozenset:- mutable

a=({10,20,"paras"})

b=({10,20,"paras"})
print(id(a),id(b))

dis:-mutable

x={"name":"paras",
"age":20,
"place":"bhopal"}
y={"name":"paras","age":20,"place":"bhopal"}

print(id(x),id(y))

x=True
y=False
print(id(x),id(y))



x=None
y=None
print(id(x),id(y))'''