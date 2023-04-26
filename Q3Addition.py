from random import randint

A = randint(0, 100)
B = randint(0, 100)
ANS = A + B
print(f"What is {A} + {B}?")

C = None
while not isinstance(C, int):
    try: C = int(input("Ans: "))
    except: pass

if ANS == C:
    print("\nCorrect!")
else:
    print(f"\nIncorrect, Answer is: {ANS}")