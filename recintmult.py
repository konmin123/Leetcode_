print("Two n-digit positive integers x and y.")
print("Assumption : x,y is the power of 2.")

x = int(input("X : "))
y = int(input("Y : "))


def RecIntMult(x1, y1):
    if x1/10 < 1 and y1/10 < 1:
        return x1 * y1
    else:
        n = len(str(x1))
        n2 = n//2
        a, b = divmod(x1, 10**n2)
        c, d = divmod(y1, 10**n2)
        ac = RecIntMult(a, c)
        ad = RecIntMult(a, d)
        bd = RecIntMult(b, d)
        bc = RecIntMult(b, c)
        return ac*10**n+(ad+bc)*10**n2+bd


print(RecIntMult(x, y))