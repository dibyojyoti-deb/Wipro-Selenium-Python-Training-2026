number=list(range(1,21))
even_nums=list(filter(lambda x:x%2==0, number))
squared_even=list(map(lambda x:x**2, even_nums))
print (squared_even)