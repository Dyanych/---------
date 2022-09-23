# Recusive methode 

def factorialRec(n):
    return 1 if n == 1 else factorialRec(n-1) * n

print(factorialRec(5))
