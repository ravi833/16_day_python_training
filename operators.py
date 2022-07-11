'''operators in python'''

'''arthimatic operator'''
# a,b=(int(x) for x in input('enter the value of a and b:').split())
# print(f'the value of {a}+{b}: is {a+b}')  #9
# print(f'the value of {a}-{b}: is {a-b}')  #-1
# print(f'the value of {a}*{b}: is {a*b}')  #20
# print(f'the value of {a}/{b}: is {a/b}')  #  0.8
# print(f'the value of {a}%{b}: is {a%b}')  #4
# print(f'the value of {a}**{b}: is {a**b}')  #1024


'''floor division'''
# e=4/2  
# print(e)  #2.0
# d=4//2
# print(d)  #2
# g=5//2.0
# print(g)  #2.0
# h=5.0//2
# print(h) #2.0
# j=5.0/2
# print(j) #2.5

''' assugnment operators'''
# a=5  ; b=6
# a=a+b
# print(a)  #11
# print(a+b)   #17

# g=2
# g+=2
# print(g)  #4

'''relational operators'''
# a=int(input())
# b=int(input())
# print(a<b)   #true
# print(a<b)  #false
# print(a>b)  #false
# print(a>b)  #true
# print(a==b)  #true
# print(a==b)  #false
# print(a!=b)  #false
# print(a!=b)  #true
# print('a=%d, b=%d and a<b=%d '%(a,b,a<b))  #1


'''logical operators'''
# a=int(input())
# b=int(input())
# print((a<b) and (a>b))  #false
# print((a<b) and (a<b))  #true
# print((a<b) or (a<b))  #true
# print((a<b) or (a>b))  #true
# print((a>b) or (a>b))  #false
# print((a>b) or (a>b))  #false
# print(not a==b)  #true
# print(not a!=b)  #false

'''bitwise operator'''
# a=int(input())
# b=int(input())
# # c=int(input())
# # print(a and b and c)  #5
# # print(a&b)  #4
# # print(a|b)  #7

'''identity operator'''
# a=20
# b=20
# print(id(a))
# print(id(b))
# if (a is b):
#     print(a==b)  #true
# else:
#     print(a!=b)
# x=5
# print(type(x) is int)  #true
 
'''membership operator'''
# name=['ravi','babu','gowtham']
# print('babu' in name)  #true
# print('harika' in name)  #false

'''shift operator'''
a=20
print(a>>1)  #10
print(a>>2)  #5
print(a>>3)  #2
a=20
print(a<<1)  #40
print(a<<2)  #80
print(a<<3)  #120