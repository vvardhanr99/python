# # this is a program to check if a number is even or odd
# # and also check if the number is zero
# # number = int(input("Enter a number: "))
# # if number % 2 ==0:
# #     print("Number is Even ",number)
# # if number % 2 !=0:
# #     print("Number is Odd ",number)
# # elif number == 0:
# #     print("Number is Zero ",number)

# # a = 10
# # print(type(a))
# # a = 'vishnu'
# # print(type(a))


# # def my_function():
# #     global y 
# #     y = 20

# # my_function()
# # print(y)

# # def even_odd(num):
# #     if num % 2 == 0:
# #         print( "Even")
# #     if num %2  != 0:
# #         print ("Odd")
# #     elif num == 0:
# #         print( "Zero")

# # even_odd(0)



# row = 6
# for i in range(0,row):
#     for j in range(0,i+1):
#         print("* " ,end="")
#     print("\r")
    


# name = " vishnu Vardhan Reddy"
# print(name.split(" "))
# print(name.strip(" "))

# x = 10

# print("{}{}".format(name,x))
# print(f"{name}{x}")

# def function_sum(x,y):
#     print(x+y)

# function_sum(10,20)

# x = 10;
# y = 20;

# x += y # x =30
# y = x - y # y = 10
# x -= y #y = 20
# print("x = ",x) 
# print("y = ",y)


# print ( 5 == 5)
# print ( 5 == '5')


# x = 10000
# y = 10000

# print(x is y)
# print(id(x))

# print(id(y))

# x = 10003232
# y = 10003232

# print(id(x))  # Different memory address
# print(id(y))  # Different memory address
# print(x is y)  # False, because they are different objects


mylist = [1,2,3,4,5,6,7,8,9,10]
mylist.append(11)
print(mylist)

mytuple= ("vsihnu",)
print(mytuple)
print(type(mytuple))

myset = {'vishnu', 'reddy', 'vishnu'}
for i in myset:
    print(i)
print(myset) # set will not allow duplicates



mydict = {'name': 'vishnu', 'age': 25}
print(mydict)

