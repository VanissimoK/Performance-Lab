import sys

def formul(xe, ye, r1, r2, x, y):
    result = ((x - xe)**2) / (r1**2) + ((y - ye)**2) / (r2**2)
    return result

circle_path = sys.argv[1]
dot_path  = sys.argv[2]

with open(circle_path) as f:
    xe, ye, r1, r2 = map(float, f.read().split())
    
with open(dot_path) as f:
    for line in f:
        x, y = map(float, line.split())
        znach = formul(xe, ye, r1, r2, x, y)
        if znach == 1:
            print(0)
        elif znach < 1:
            print(1)
        else:
            print(2)
