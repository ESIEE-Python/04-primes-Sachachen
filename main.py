"""je"""
from math import sqrt
#### Fonction secondaire


def isprime(p):

    """
    Trouve les nombres premiers

    Args: 
        p: valeur entiere positive

    Returns
         
    """

    premier = True
    if p == 1:
        return False
    for d in range (2,int(sqrt(p)+1)) :
        if p%d==0 :
            premier = False
    return premier

#### Fonction principale


def main():
    """
    je suis pd
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
