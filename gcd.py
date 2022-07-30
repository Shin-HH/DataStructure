# gcd by sub
a, b = map(int, input().split())

def gcd_sub(a, b):
    while a != 0 and b != 0:
        if a > b: a -= b
        else: b -= a
    
    return a + b

def gcd_mod(a, b):
    while a != 0 and b != 0:
        if a > b: a %= b
        else: b %= a
    
    return a + b

def gcd_rec(a, b):
    if a == 0 or b == 0:
        return a + b
    
    if a > b: return gcd_rec(a % b, b)
    else: return gcd_rec(a, b % a)

print('sub:', gcd_sub(a, b))
print('mod:', gcd_mod(a, b))
print('rec:', gcd_rec(a, b))
