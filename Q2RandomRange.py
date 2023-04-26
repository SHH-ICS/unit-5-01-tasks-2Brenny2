import random
A = None
B = None

while not isinstance(A, int):
    try: A = int(input("Min: "))
    except: pass
while not isinstance(B, int):
    try: B = int(input("Max: "))
    except: pass

print(f"\nRandom #: {random.randint(A, B)}")