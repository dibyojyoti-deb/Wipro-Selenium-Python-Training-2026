from enum import Enum

fruits=['apple','orange','banana']
for index,value in enumerate(fruits):
    print(index,value)

print()

class Color(Enum):
    Red=1
    Green=2
    Blue=3
print(Color.Red.value)
print(Color.Red.name)