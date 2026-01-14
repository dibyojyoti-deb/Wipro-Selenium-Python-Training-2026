def add(a,b):
    print(a+b)

def sub(a,b):
    return a-b,a

add(10,20)
print(sub(100,20))
def hello(greeting='Hello', name='world'):
     print ('%s, %s!' % (greeting, name))
hello('Greetings')
def hello_1(greeting, name): 
     print ('%s, %s!' % (greeting, name))
# The order here doesn't matter at all: hello_1(name='world', greeting='Hello')
def print_params(*params): 
     print (params) 

print_params('Testing') 
print_params(1, 2, 3)
def print_params_3(**params): 
     print (params) 

print_params_3(x=1, y=2, z=3)
def print_params_4(x, y, z=3, *pospar, **keypar):  
     print (x, y, z) 
     print (pospar)
     print (keypar)

print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2) 
print_params_4(1, 2)
