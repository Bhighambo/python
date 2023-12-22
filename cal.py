a = float(input("Entre la première valeur..."))
b = float(input("Entre la deuxième valeur..."))
def Sommes():
    c = a + b
    return c
def Multiplication():
    d = a * b
    return d
def Soustraction():
    e = a - b
    return e
def Division():
    f = a / b
    return f


if __name__ == '__main__':
    print("La sommes est :", Sommes())
    print("Le produit est :", Multiplication())
    print("Le reste est :", Soustraction())
    print("Le quontient est :", Division())