import math
A = None
B = None

while not isinstance(A, float):
    try: A = float(input("Leg A: "))
    except: pass
while not isinstance(B, float):
    try: B = float(input("Leg B: "))
    except: pass

A = A ** 2
B = B ** 2
C = math.sqrt(A + B)
print(f"\nC = {round(C, 5)}")
