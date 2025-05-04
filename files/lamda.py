y = lambda x : x*x

def myfun(n):
    return lambda x: x*n

double = myfun(2)
triple = myfun(3)

print(double(11)) # 22
print(triple(11)) # 33