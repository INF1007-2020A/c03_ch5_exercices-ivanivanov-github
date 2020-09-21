#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre = float(input("Entrez un nombre: "))
    if nombre < 0:
        nombre = -1 * nombre
    return nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    resultat = []
    for loop in prefixes:  
        nom = loop + suffixe
        resultat.append(nom)
    return resultat


def prime_integer_summation():
    nbPremier = 0
    somme = 0
    nb = 2
    while(nbPremier<100):
        for diviseur in range(2,nb+1): 
            if nb % diviseur == 0 and diviseur != nb:
                break
            if nb % diviseur == 0 and diviseur == nb:
                somme += nb
                nbPremier += 1
        nb += 1
    return somme


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
