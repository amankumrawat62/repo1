# class c1:
#     def m1(self):
#         print("i am aryan ")
# class c2:
#     def m2(self):
#         c1.m1(self)

# obj=c2()
# obj.m2()

'''classs ka object bnte constructor automatic call ho jata he '''
'''we __init__ for  defining constructor method a class can have a single constructor 
if you create two constructor in a class then the cons. 
which is near to the object will be consider'''

'''why we use constructor
we use cons. for variable initiallization
create the environment automatically for running your application
it will also use for doing for database configration automatically'''

# class c1:
#     def __init__(self):
#         print("hello")
# obj=c1()
# obj.__init__()


# class c1:
#     def __init__(self,a):
#         self.instance=a
# obj=c1(10)
# print(obj.instance)

# class c1:
#     def __init__(self):
#         print("i am first cons.")
#     def __init__(self):
#         print("i am second cons.")

# obj=c1()


'''encapsulation :- private- double "__"  
                    protected - single " _"
security , wrapping,binding and hiding data and methods '''


# class c1:
#     def m1(self,a,b):
#         self.__a=a   #private
#         self._b=b  #protected
# obj=c1()
# obj.m1(10,100)
# print(obj.__a)
# print(obj._b)


# class c1:
#     __data=22
#     def m1(self,a,b):
#         self.__a=a   #private
#         self._b=b  #protected
#     def display(self):
#         print(self.__a,self._b,c1.__data)

# obj=c1()
# obj.m1(10,10)
# obj.display()



# class c1:
#     __data=22
#     def m1(self,a,b):
#         self._a=a   #protected
#         self.__b=b  #private
#     def __display(self):
#         print(self._a,self.__b,c1.__data)
#     def getter(self):
#         c1.__display(self)
# obj=c1()
# obj.m1(10,10)
# obj.getter()


# class c1:

#     def m1(self,a,b):
#             self.__add=a+b
       
#     def __display(self):
#         print(self.__add)
#     def getter(self):
#         c1.__display(self)
# obj=c1()
# obj.m1(10,10)
# obj.getter()



# class c1:
#     __data=17
#     def m1(self,a,b):
#             self.__add=a+b
       
#     def __display(self):
#         print(self.__add,c1.__data)
#     def getter(self):
#         c1.__display(self)
# obj=c1()
# obj.m1(10,10)
# obj.getter()


'''serlf is an instance of class which is use to do following operation in class
1.declaring and accessing and modifying instance variable
2.self is use to call the methods of your class
3.we can access instance variable with the help of object'''

from abc import ABC,abstractmethod    #ABC :- abstract base class

# class car(ABC):
#     @abstractmethod           #decorator lagage ke hi method bnani he 
#     def engine(self):         #is class me mene engine naam se method bnai he 
#         pass                  # agr me is class ko scor wali class me inherit krunga to error aayegi 
#     @abstractmethod         # error tab tk aayegi jab tak me is class ki method mtlb engine() ko scor wali class nhi bnau 
#     def fuel(self):
#         pass
# class scor(car): 
#     def engine(self):
#         power='112'
#     def start(self):
#         print(" car started \n brooooom......brooooom.....")
#     def fuel(self):
#         pass
# obj=scor()
# obj.start()


# class shape(ABC):
#     @abstractmethod
#     def calculate(self):
#         pass
# class rectangle(shape):
#     def calculate(self,a,b):
#         print(a*b)
#     def triangle(self,a,b):
#         print(a*b)
# obj=rectangle()
# obj.triangle(10,25)



'''inheritance'''
'''it is a concept in which we inherit the attributes and method of parent classs in to the child class'''



# class parent:
#     data=100
#     def m1(self):
#         print("rathod")
# class child1(parent):
#     def m1(self):
#         print("hello")
#         super().m1()
# obj = child1()
# obj.m1()


# class parent:
#     data=100
#     def m1(self):
#         print("rathod")
# class child1(parent):
#     def m1(self):
#         print("hello")
#         super().m1()
# class child(child1):
#     def m1(self):
#         print("i am aryan")
#         super().m1()
# obj = child()
# obj.m1()



# class parent:
#     data=100
#     def m1(self):
#         print("rathod")
# class child1(parent):
#     def m1(self):
#         print("hello")
#         super().m1()
# class child2(parent):
#     def m1(self):
#         print("i am ar")
#         super().m1()
# class c1(child2):
#     def m1(self):
#         print("i am aryan")
#         super().m1()
# class c2:
#     def m1(self):
#         print("i am devashis")
#         super().m1()
# class parent2(c2,c1):
#     def m1(self):
#         print("i am amey")
#         super().m1()
# obj=parent2()
# obj.m1()

'''constructor kabhi  return hold nhi krta'''


# class c1:
#     def m1(self):
        
#         print("1000")
        
# class c2:
#     def m1(self):
        
#         print("900")
# class c3(c1):
   
#     def m1(self):
#         print("345")
        
# obj=c3()
# obj.m1()




