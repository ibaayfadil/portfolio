'''
1. Introduction to Data Strcuture
    List = 
    Tuple =
    Dictionary = 
2. The List for Data Structure
3. The Dictionary for Data Structure
4. Tasks
'''

'''
#List 
a = ["kentung", "fajri", "henhen", "acon"]
print(a[1])
b = [1, 2, 3, 4]
# print(b[3])
b.pop(1)

c = ["Budi", 120, "Kentang", 9821]
print(type(c))

a = [1,2,3,4]
a[1] = 7
print(a)
a.pop()
print(a)
a.pop(0)
print(a)


a = [1,2,3,4]
b = [12,14,18,20]
a.extend(b) #berfungsi untuk menambahkan 2 dictionary
print(a)

a = [1,3]
a.append(12) #berfungsi untuk menambahkan data pada dictionary dengan data ditambahkan ke indeks terakhir
print(a)

a = [1,3,9]
a.insert(2, 100) #berfungsi untuk menambahkan data pada dictionary dengan 2 sebagai indeks nya dan 100 data nya
print(a)


shopping = ["Soda", "cake", "fruit", "biscuit"]
search = "biscuit"
if search in shopping:
    print(shopping.index(search))
else:
    print(-1)

search = "soda"
if search in shopping:
    print(shopping.index(search))
else:
    print("data tersebut tidak ada")


d = [3, 10, -2, 1, 100]
d.sort()
print(d)

a = [1, 2, 4, 8, 11, 17, 20, 0, 22, 25]
for i in a : 
    print(f"content {a.index(i)} = {i}") 


a = [1, 2, 4, 8, 11, 17, 20, 0, 22, 25]
print(a[:])
print(a[4:])
print(a[:3])
a.sort() 
for i in a : 
    print(f"content {a.index(i)} = {i}") 


A = [1,2,3,4]
B = [5,6,7,8]
print(A*B) #tidak bisa
print(A*2)
print(A + B)
print(B + 5) #tidak bisa
print(A - B) #tidak bisa
print(A/B) #tidak bisa
# Kesimpulan pada list hanya bisa perkalian dan pertambahan


#dictionary for data structure 
student = {"id":109, "name":"iqbal", "age":20, "sex":"male"}
print(student['name'])
print(student.values())
'''

groupmember = {'m': ['dedi', 'henhen', 'kentung'], 'f': ['bila', 'rena', 'ajay']}
print(groupmember)
print(groupmember['m'])
print(groupmember['f'])
print(groupmember.keys())
print(groupmember.values())
for i in groupmember:
    print(groupmember[i])