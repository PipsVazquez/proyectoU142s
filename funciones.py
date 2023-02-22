def chicharronera(a,b,c):
    x1 = (-b + (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    return x1

def chicharronera2(a,b, c):
    x2 = (-b - (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    return x2

print(chicharronera(1, 2 , -8))
print(chicharronera2(1, 2 , -8))
