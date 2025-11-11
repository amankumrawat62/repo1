'''lambda function'''
# print((lambda a,b:a*b)(3,3))


# def f1(f,a):
#     return f(a)
# print(f1(lambda x:x*x,4))



# n =['ac','a','abc','apple','okla']
# a= sorted(n, key=lambda n:len(n))
# print(a)

# n=[1,4,5,3,2]
# c=(sorted(n,key=lambda n:n%2))
# print()



# def f1(n):
#     return f1(n+1)
#     print(n)



# def f1(n):
#     if n==74:
#         return 0
#     print(n)
#     return f1(n-1)
# f1(100)


# def f1(n):
#     if n>20:
#         return 0
#     print(n)
#     return f1(n+2)
# f1(2)


# def f1(n):
#     if n==1:
#         return n
#     return n*f1(n-1)
# print(f1(3))


# data=[12,3,5,6,9]
# def f1():
#     global a
#     a=len(data)
#     if a%2!=0:
#         return data
    
# print(f1())



# def s(n):
#     if n<10:
#         return 0
#     else:
#         print(n)
#     return s(n-1)
# s(10)


# def dis(n):
#     if n<40:
#         return 0
#     else:
#         print(n)
#     return dis(n-1)
# dis(55)


# def even(n):
#     if n == 0:
#         return []
#     result = even(n - 1)
#     if n % 2 == 0:
#         result.append(n)
#     return result
# print(even(20))


# data=[]
# def f1(n):
#     if n>20:
#         return 0
#     elif n%2==0:
#         data.append(n)
#     return f1(n+1)
# f1(1)
# print(data)


'''palindrom'''
# data=0
# def di(n):
#     global data
#     if n<=0:
#         return 0
#     rev=n%10
#     data=data*10+rev
#     return di(n//10)
# s=141
# di(s)
# if data==s:
#     print(d," is palindrom ")
# else:
#     print(d," is not palindrom")


'''find febonanci series using recursion'''
# def feb(n):
#     if n<=0:
#         return 0
#     elif n==0:
#         return n
#     else:
#         return feb(n-1)+feb(n-2)
# print(feb(5))

'''febonanci series using loop'''
# a=0
# b=1
# for i in range(16):
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c
    
# a=0
# b=1
# def feb(n):
#     global a
#     global b
#     if n<=0:
#         return a
#     c=a+b
#     print(a,end=' ')
#     a=b
#     b=c
#     return feb(n-1)
# print(feb(7))



'''OOPS'''


def mul(fun):
    def wrapper(a,b):
        print(a*b)
        fun(a,b)
    return wrapper
    
@mul
def main(a,b):
    print(a+b)
main(2,5)