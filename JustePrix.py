#jeu du juste prix
#choisir un nombre entre 1 et 1000
#tant que le jeu n'est pas fini
# demandr à l'user "entrer un prix"
# si il trouve le prix c'est gagné
#si il trouve pas dire si c'est moins ou plus

debut= input("BIENVENUE AU JUSTE PRIX DÉMARREZ EN ÉCRIVANT OK :")


while debut !="OK":
    debut = input("BIENVENUE AU JUSTE PRIX DÉMARREZ EN ÉCRIVANT OK :")

if debut == "OK":
    print("bonne chance !")
#le jeu choisis un nombre
from random import randint
prix=randint(1,1000)
rep= int(input("devinez le nombre entre 1 et 1000:"))

while rep != prix:
     if rep <prix:
        print("c'est plus grand!")
        rep = int(input("devinez le nombre entre 1 et 1000:"))
     elif rep > prix:
         print("c'est plus petit !")
         rep = int(input("devinez le nombre entre 1 et 1000:"))

     if rep == prix:
         print("je te Félicite ! tu as gagné le prix était bien de {}".format(prix))
         break
