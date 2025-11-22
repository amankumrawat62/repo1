# class car:
#     model='2025'
#     color='red'
#     def start(self):
#         print("car started")
#     def stop(self):
#         print("car stopped")
# c1=car()
# print('alto color = ',c1.color)
# c1.color='purple'
# print('ferrari color = ',c1.color)
# bmw=car()
# bmw.color='blue'
# print('bmw color = ',bmw.color)



# '''types of attributes'''
# 1. class variable 
# 2. instance variable 
# class student:
#     def records(self, name, subject, marks):
#         self.name = name
#         self.subject = subject
#         self.marks = marks

# mohan = student()
# mohan.records("mohan", "hindi", 90)

# sohan = student()
# sohan.records("sohan", "hindi", 80)
# mohan.marks=40
# data = f'''hello! my name is {mohan.name}
# in {mohan.subject} i scored {mohan.marks} marks

# '''

# print(data)



# class student:
#     def records(self, name, subject, marks):
#         self.name = name
#         self.subject = subject
#         self.marks = marks

# # list to store all students
# students = []

# # adding multiple students
# mohan = student()
# mohan.records("mohan", "hindi", 90)
# students.append(mohan)

# sohan = student()
# sohan.records("sohan", "hindi", 80)
# students.append(sohan)

# rohan = student()
# rohan.records("rohan", "english", 85)
# students.append(rohan)

# # print all records using loop
# print("Student Records:\n----------------")
# for s in students:
#     print(f"Name: {s.name}")
#     print(f"Subject: {s.subject}")
#     print(f"Marks: {s.marks}")
#     print("----------------")



# class college:
#     def management(self, name, subject, branch):
#         self.b1 = name
#         self.b2 = subject
#         self.b3 = branch

# hod= college()
# hod.management("kamlesh patidar ", "computer science", 'whole cs branch')

# newhod = college()
# newhod.management("yunush khan", "computer science", 'aiml and ds branch')

# data = f'''hello! our  {hod.b2} hod is {hod.b1} he is a hod of {hod.b3} but
# mr.{newhod.b1} sir is replaced as a hod of{newhod.b2} brach but he is only hod of {newhod.b3}

# '''

# print(data)


# class college:
#     avg='10 lpa'
#     course=['btech','mtech','bca','mca']
#     def hackthon(self):
#         pass
#     def timing(self):
#         pass
#     def exam(self):
#         print("exam started")
# c1=college()
# a=c1.exam()
# print(a)


# class c1:
#     data=90
#     def m1(self):
#         pass

'''if there is no class variablenamed by your class name.variable'''
# c1.new_obj=40
# obj1=c1()
# obj1.data=30
# print(obj1.data,c1.data,c1.new_obj)

'''inside the method '''

# class c1:
#     a=10
#     def m1(self):
#         print(self.a)        #accessing class variable
#         c1.b=100           #declaring class variable
#         self.a+=10           # modifying class variable
#         print(self.a)
#         c1.b+=100
#         print(c1.b)
#         self.a+=10
#         print(self.a)
# obj=c1()
# obj.m1()



# class c1:
#     alpha=10

# c1.alpha=2000
# obj=c1()
# print(obj.alpha)


'''using classmethod decorator'''
# class c1:
#     a=10
#     @classmethod
#     def m1(cls):
#         print(cls.a)
# obj=c1()
# obj.m1()

# class c1:
#     a=10
#     @classmethod
#     def m1(self):
#         self.a+=1
#         print(self.a)
# obj=c1()
# obj.m1()


class c1:
    a=10
    @staticmethod
    def m1():
        c1.a=90
        data=810
        print(data)
obj=c1()
obj.m1()
print(c1.a)


'''magic methods'''

""" constructor__init__"""# jaise hi class ka object bnta he constructor automatically execute ho jata he ,jaise hi class object bnayenge

# class c1:
#     def __init__(self):
#         print("hello ! i am constructor...")#super power kisis bhi bhi 

# obj=c1()


# class c1:
#     data=90
#     c=33
#     def m1(self):
#         print("i am m1")

# obj=c1()
# del obj.data
# print(c1.c)



# class c1:
#     data=90
#     c=33
#     def m1(self,a):
#         print("i am m1")
#         print(a)
# obj=c1()
# del obj.data
# obj.m1(44)


# class c1:
#     def m1(self):
#         print("hello jit")
# class c2:
#     def m2(self):
#         print("before")
#         c1.m1(self)
# obj=c2()
# obj.m2()


'''encapsulation :- binding an attributes and method '''

#partially encapsulate
# class c1:
#     def m1(self):
#         _data=90
    

# obj=c1()
# obj.m1()



# class c1:
#     __data=635
#     def display(self,a,b):
#         self.__a=a
#         self.__b=b
#         print(self.__a,self.__b,c1.__data,self.__data)
# obj=c1()
# obj.display(6,77)



# class c1:
#     def __init__(self,a,b):
#         self.__a=a
#         self.__b=b
#     def __display(self):
#          print(self.__a,self.__b)
#     def gatter(self):
#         c1.__display(self)
#     def setter (self,n1,n2):
#         self.__a=n1
#         self.__b=n2
# obj=c1(2,8)
# c1.gatter(self=7)
