# oops:-
# class
# object
#        syntex:- class class_name
                    #  "doc string"
                    
                    
                    # variable  :-
                    
                    # 1.instance variable                    (object dependent)=obj dependent self se instance hote hai  Ex.(self.n) isko likhne se khud hi ho jata hai 
                    # 2.class variable/ static variable      (object independent) = isse class me ham kahi bhi use kar sakte hai
                    # 3.local variable                       (object local scope delaration) =local sirf function ke ander use kar sakte hai 
                                
                                
                    # constrctor methods:-
                    
                    # 1.instance methods   (first parameter is self) =
                    # 2.class methods      (first parameter is cls) (@staticmethods)= class name se access kar sakte hai 
                    # 3.static methods     (we canituse either self cls)  bina self ki help se 
                
# class Student:
#     '''Student object'''
#     school_name="Cybrom"
#     def __init__(self):
#         print("contuctor called")
#         print(id(Student))
# print(Student.school_name)


# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student
# print(id(obj2))


# class Student:
#     '''this is oop's class'''
#     x=10
#     y=20
#     z=30
#     def shows():
#         print("this is oop's class")
        
# print(dir(Student))
# print(Student.__doc__)
# print(Student.__module__)
# print(Student.__dict__)
# print(Student.__init__)                    # in built contractor =class ko object banane ke liye contractor ka use hota hai 



# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student()
# print(id(obj2))


# class Student:
#     school="Shss"
#     def __init__(self):
#         print("called")
#         print(id(self))
# print(id(Student))
# obj=Student()
# print(id(obj))
# obj1=Student()
# print(id(obj1))




# class Student:
#     def __init__(self,name,rolln):
#         self.n =name
#         self.r= rolln
# obj=Student('paras',22)
# obj.c='12345'
    
    
    
# class Student:
#     def __init__(self,name, rollno):
#         self.n=name
#         self.r=rollno
# def addnew(self,contct):
#     self.c=contct
# obj=Student("paras",101)
# obj=addnew(12345)
# obj.school='cybrom'
        
        
# class Student:
#     def _init_(self,name, roll):
#         self.n=name
#         self.r=roll
#         print(self.n,self.r)
#     def addshow(self,contect):
#         self.c=contect
#         print(self.c,self.r,self.n)

# obj=Student('jgiui',12)  
# obj.addshow(12345) 
# obj.school="ghsk" 

# print(obj.n,obj.r,obj.c)
# print(id(obj.n))
# print(id(obj.r))
# print(id(obj.c))



# class variable

# class Student:
#     school='ShSS'
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
# obj1=Student('paras',1)
# obj2=Student('vikash',2)
# obj3=Student('sumit',3)
# print(obj1.school,obj2.school,obj3.school)


# class Student:
#     school='SHSS'
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#         Student.p='python'
#     def addnew(self):
#         Student.school_city='bhopal'
#     @classmethod   
#     def update_or_create(cls):
#         cls.school_code=1101
# obj=Student('paras',101)
# obj.addnew()
# obj.update_or_create()



# class Student:
#     school='SHSS'   # declation
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#         print(Student.school)#calling
#         Student.principal="python"   # declation
#     def addnew(self):
#         Student.school_code=101
#     def show(self):
#             print(Student.principal,Student.school,Student.school_code) #calling
#     @classmethod
#     def create_or_update(cls):
#         cls.x=10
#         print(Student.school,Student.principal,Student.school_city) #calling
# obj=Student("paras",45)
# obj.addnew()
# obj.show()
# Student.school_city="bhopal"
# obj.create_or_update()
# print(Student.school)











# 3. / local variable

# class Student:
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#         x=10
#         print(x)
#     def show(self):
#         y=10
#         print(y)
#         print(x)
# obj=Student("Paras",45)
# obj.show()#error
        


# class Book:
#     price=100
#     def __init__(self,title,branch):
#         self.t=title
#         self.b=branch
# obj1=Book("pythonbook","IT")
# print(obj1.price)
# obj2=Book('python','IT')




# class Book:
#     price=100
#     def __init__(self,title,branch):
#         self.t=title
#         self.b=branch
# @classmethod
# def update_price(cls,newprice):
#     cls.price=newprice
# obj=Book('python','It')
# print(obj.price)
# x=float("enter new price : ")
# obj.update_price(x)
# print(obj.price)




# 3.staticmethod


# class Student:
#     x=10
#     def __init__(self,name):
#         self.n=name
#     @staticmethod
#     def show ():
#         print(Student.x)
# obj=Student("paras")
# obj.show()        



# class Student:
#     x=10
#     def __init__(self,name):
#         self.n=name
#     @staticmethod
#     def great(name):
#         print(f'welcome : {name}')
# obj=Student('paras')
# x=obj.n
# obj.great(x)


















# property of oops


# 1.Abstraction      | data sequre
# 2.Encapsulation    | ----//-----

# 3.Inheritnece       |code reusablity
# 4.Polymorphism      |-----//--------



# 1.Inheritance=parent child relation

#  Stx=class Parent :
#     variable
#     method 
# class Child(Parent):
#     pass





# class Parent:
#     city='bhopal'
#     def car(self):
#         print(("can from parent"))
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.city,obj.car())























# Types
# 1.Single level inheritance
# 2.multi-level
# 3.multiple
# 4.hierarchical
# 5.hybrid




#  1.Single level inheritance      parent ----->child
#  2.multi-level                   grant-parent ----> parent ----->child
# 3.multiple                       
                                #   father           mother
                                    # |                |
                                    # |________________|
                                         #     |
                                        #   child



















# 1.single level =  parent or child dono me same nam ke methods use hoti  hai bo (override) hota hai usko (super()) ki help se solve kiya jata hai 



# class Parent:
#     car='nexon'
#     def home(self):
#         print("home from parent")
# class Child(Parent):
#     car='aura'
#     car2=Parent.car
#     def home(self):
#         super().home()
        
        
#         print("home form child")
# obj=Child()
# print(obj.car)
# obj.home()
# print(obj.car2)



# 2.multi-level



class Grandparent:
    car='nexton'
    def home(self):
        print("home from grandparent")
class Parent:
    bank='ICICI'
    def land(self):
        print("land from parent")
class Child(Parent):
    pass
obj=Child()
print(obj.car,obj.bank)
obj.land()
obj.home()



class Grad:
    car ="nexso"
    def home(self):
        print("home form a GP")

class Prent(Grad):
    bank="ISBT"
    def land(self):
        print("this is a grad")
class child(Prent):
    pass
obj=child()
print(obj.car,obj.bank)
obj.land()
obj.home()
        
    











































































































































































































































        



