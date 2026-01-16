from functools import reduce

number=list(range(1,21))
even_nums=list(filter(lambda x:x%2==0, number))
squared_even=list(map(lambda x:x**2, even_nums))
total_sum=reduce(lambda x,y:x+y, squared_even)
print (f"{'Index':<7} | {'Value': <5}")
print("-"*15)
for index,value in enumerate(squared_even):
    print(f"{index:<7} | {value:<5}")

print("-" * 15)
print(f"Total Sum :{total_sum}")
