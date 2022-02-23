'''
TASK #1 COMPLETE
'''
print("TASK #1")
a = 0; b = 1
print((a + b) % (a + b) / b // b ** b - -b)

'''
TASK #2 COMPLETE
'''
print("TASK #2")
from sys import getsizeof
num = 100_000**100_000
print(num, getsizeof(num))
fum = 100_000_000.0**38 #OVERFLOW WITH 39
print(fum, getsizeof(fum))
import builtins
print(dir(builtins))
a1 = 42
a2 = 42.0
a3 = int(42.0)
a4 = float(42.0)
a5 = 0x2A
a6 = 0b101010
a7 = 0o52
a8 = hex(42)
a9 = bin(42)
a10 = oct(42)

'''
TASK #3 COMPLETE
'''
print("TASK #3")
import this
import antigravity
import __hello__
from __future__ import braces

'''
TASK #4
'''
print("TASK #4")

def mul12(par):
    par += par + par
    par += par
    par += par
    return par

def mul16(par):
    par += par 
    par += par
    par += par
    par += par
    return par

def mul15(par):
    par += par + par
    par -= -(par + par )
    return par

def mul29(par):
    return    
print(mul15(1))

'''
TASK #5 COMPLETE
'''
print("TASK #5")
print((True * 2 + False) * -True)

'''
TASK #6 COMPLETE
'''
print("TASK #6")
1 = input() #1
while True print('Hello world') #2
print(spam*3) #3
print('2' + 2) #4
 for i in range(10): #5
    print(i)
n = 1007 / 0 #6
print ( chr(-97)) #7
import math
print(math.exp(1000)) #8

'''
TASK #7 COMPLETE
'''
print("TASK #7")
print(0.6 + 0.3 == 0.9)

'''
TASK #8 COMPLETE
'''
print("TASK #8")
x = 5
print(1 < x < 10, 1 < (x < 10))
print(1 < True, 1 < 42 == 42)

'''
TASK #9 COMPLETE
'''
print("TASK #9")

def naive_mul(x, y):
    r = 0
    for i in range(0, y):
        r += x
    return r

def check_naive_mul():
    for i in range(0, 101):
        for j in range(0, 101):
            if (naive_mul(i,j) != i*j):
                return False
    return True

print(check_naive_mul())

'''
TASK #10 COMPLETE
'''
print("TASK #10")
def is_even(num):
        return (not num % 2)

def fast_mul(num1, num2):
    mul = 0
    if (not is_even(num1)):
        mul +=  num2 * (num1 % 2)
    while(num1 > 1):
        num1 //= 2; num2 *= 2
        if (not is_even(num1)):
            mul += num2
    return mul

def check_fast_mul():
    for i in range(0, 101):
        for j in range(0, 101):
            if (fast_mul(i,j) != i*j):
                return False
    return True

def fast_pow(num1, par):
    mul = 0
    num2 = num1
    for i in range(par-1):
        mul = fast_mul(num1, num2)
        num1 = mul
    return mul

print(fast_pow(2,4))