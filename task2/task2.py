def formul(xe, ye, r1, r2, x, y):
    result = ((x - xe)**2) / (r1**2) + ((y - ye)**2) / (r2**2)
    return result

with open('circle.txt') as f:
    xe, ye, r1, r2 = map(float, f.read().split())
    
with open('dot.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        znach = formul(xe, ye, r1, r2, x, y)
        if znach == 1:
            print(0)
        elif znach < 1:
            print(1)
        else:
            print(2)
