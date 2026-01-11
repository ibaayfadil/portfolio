# def my_function():
#     print("Hello Iqbal F")

# my_function()

# def my_function(fname):
#     print(fname + " Putri")

# my_function("Emil")
# my_function("Rahmat")
# my_function("Dinda")

# def my_function(fname, lname):
#     print(fname + " " + lname)

# my_function("Emil", "Putri")
# my_function("Rahmat", "Putri")
# my_function("Dinda", "Putri")


# global_lang = 'DataScience'

# def var_scope_test():
#     local_lang = 'Python'
#     print(local_lang)

# var_scope_test()
# print(global_lang)
# # print(local_lang) # Error karna local_lang terdapat di suatu fungsi 

# global_var = 999

# def function1():
#     print("value in 1nd function :", global_var)

# def function2():
#     print("value in 2nd function :", global_var)

# function1()
# function2()

# global_var = 5

# def function1():
#     print("value in 1nd function :", global_var)

# def function2():
#     global_var = 321
#     print("value in 2nd function :", global_var)
#     # Pada function 2 global_var akan tetap mencetak local definisi yang ada pada fungsi 2 sehingga hasilnya berbeda dengan function 1 dan 3

# def function3():
#     print("value in 3nd function :", global_var)

# function1()
# function2()
# function3()


# x = 5

# def function1():
#     print("value in 1nd function :", x)

# def function2():
#     # Modify variabel global untuk keyword global
#     global x
#     x = 555
#     print("value in 2nd function :", x)
   
# def function3():
#     print("value in 3nd function :", x)

# function1()
# function2()
# function3()


# def my_function(*kids):
#     print("The youngest child is " + kids[len(kids)-1])

# my_function("Iqbal", "Fajri", "Farah", "Faizal")

# def sum_number(*args):
#     result = 0
#     for x in args :
#         result += x
#     return result

# print(sum_number(1, 2, 3, 4, 5, 6))


# def country(country = "Indonesia"):
#     print("I am from " + country)

# country("Sweden")
# country("India")
# country()

# def persegi_panjang(p ,l):
#     luas = p * l
#     return luas

# print(persegi_panjang(2, 4))

# def persegi_panjang(p ,l):
#     return p * l

# print(persegi_panjang(2, 4))


# def my_function():
#     pass

# my_function()

# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)

# my_function(child3 = "Iqbal", child1 = "Fajri", child2 = "Farah")

# def factorial(n):
#     if n == 1 :
#         return 1
#     else :
#         return n * factorial(n-1)

# print(factorial(5))

'''
STRING CREATION 
'''
word = "Hellow World"
print(word)

'''
COUNTING LENGTH
'''
word = "Hello World"
print(len(word))

'''
FIND
'''
word = "Hellow World"
x = word.find("l")
y = word.find("o")

print("the first letter 'l' in on", x, "the first letter 'o' in on", y)
