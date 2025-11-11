'''yield'''
# def f1():
#     print("hello dosto !")
#     yield 6
#     print("stg")
#     yield 3
    
# a=f1()
# print(next(a))


# def f1():
#     for i in range(3):
#         yield i
# a=f1()
# print(next(f1()))
# print(next(f1()))
# print(next(a))
# print(next(a))

# def c(n):
#     while n>0:
#         yield n
#         n-=1
# for x in c(3):
#     print(x,end=' ')


# def f1(n):
#     for i in range(n):
#         yield i
# for i in f1(3):
#     print(i,end=" ")
'''high order fuction :- dusre function as an high order le '''
'''wrapper paranthecis logic'''
'''decorator'''
# def d(n):
#     def wrapper():
#         print("before function")
#         n()
#         print("aftere function")
#     return wrapper
# @d  # main =d(main)
# def main():
#     print("i am main function")
# main()
# def mul(x, y):             
#     def decorator(func):    
#         def wrapper(a, b):  
#             print(x * y)
#             func(a, b)
#         return wrapper
#     return decorator

# @mul(2, 5)   
# def main(a, b):
#     print(a + b)

# main(10, 20)



# def mul(fun):
#     def wrapper(a,b):
#         fun(a,b)
#         print(a*b)    
#     return wrapper
# @mul
# def main(a,b):
#     print(a+b)
# main(2,5)

a=5
def f1():
    global a
    print(a)
    a=10
f1()
print(a)




# def f1():    
    
#     a=5
#     return
# b=f1()
# print(b)



