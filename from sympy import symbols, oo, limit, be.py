from sympy import symbols, oo, limit, besseli, exp

x = symbols('x')
expr = besseli(0, x + 1) / besseli(0, x)
result = limit(expr, x, oo)

print(result)