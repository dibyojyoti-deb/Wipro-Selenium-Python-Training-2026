numbers =[10,20,3,40]
names=["Ram","Hari","Ramhya"]
mixed=["Python",3.5,True]

numbers[1]=100
print(numbers)
print(names)
print (mixed)

for i in numbers:
    print (i)

if 10 in numbers:
    print("Found")

matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])

names.reverse()
print (names)
names.append("Kalai")
print (names)

names.extend(["Pavan","Leela"])
print (names)

names.remove("Kalai")
print(names)

names.insert(3,"Uma")
print (names)