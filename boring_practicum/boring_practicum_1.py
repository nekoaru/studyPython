import math


def main(x):
    x1 = 86*x**2 + 15 + 64*x**3 + 55*x**6
    x2 = math.floor(x)**3 + 6*math.log10(x**3 + x**2 + 1)
    x3 = x**2 - 77*x**3 - (x**7 / 74)
    x4 = (x**3 / 22) - 79*math.floor(1 + x**2 + x)**7
    f = x1 / x2 + math.sqrt(x3 / x4)
    return f

def main(y):
    if (y < 4):
        f = pow(math.log10(y**2/16), 4)
    if (4 <= y < 99):
        f = math.sqrt(y**3)**3 - 15*math.tan(y)**5
    if (99 <= y < 134):
        f = math.log(y) - 0.02 - y**4
    if (134 <= y < 148):
        f = 9*math.sqrt(y)**3 - 82*y**2 - 15*y**6
    if (y >= 148):
        f = 1 - (0.02 + y**3)**7
    return f     

def main(m, b, a, z):
    f = 0.0
    for j in range(1, a + 1):
        for i in range(1, b + 1):
            for c in range(1, m + 1):
                f += 57*math.log(i)**4 + z +45*math.sin((c**3 / 34) + j)**7    
    return f

def main(n):
    if (n == 0):
        return 0.92
    if (n >= 1):
        return ((main(n-1)**2 - (main(n-1) / 25) - 1)**3 + 1)


def main(x):
    f = 0
    for i in range(len(x)):
        f += (x[i//2]**2 - x[i]**3)**2
    return 60 * f
