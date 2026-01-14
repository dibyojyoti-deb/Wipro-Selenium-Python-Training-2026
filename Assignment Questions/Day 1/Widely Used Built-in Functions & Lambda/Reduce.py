from functools import reduce

number=list(range(1,21))
even_nums=list(filter(lambda x:x%2==0, number))
squared_even=list(map(lambda x:x**2, even_nums))
total_sum=reduce(lambda x,y:x+y, squared_even)
print (total_sum)