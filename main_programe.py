# =============================================================================
# Exercice L'attaque des Titans
# =============================================================================

# =============================================================================
# Consigne
# =============================================================================

"""
> Creer un programme simulant un combat qui respecte les contraintes suivantes:
    - Deux joueurs, auquels on demandera de choisir un pseudo
    - Les deux combatants demarrent avec 250 points de vie chacun
    - chacun attaque a son tour
    - Le combat se termine quand l'un des deux joueurs est mort
    - Chaque attaque est une tentative (si elle reussit, le joueur infligera
                                        un nombre de dégats (entre 0 et 100))
    - A la fin du combat, on declare le gagnant

>Indications :
    - le déroulement du combat doit etre logique et annoncé a l'utilisateur
      (affichez du texte, décrivez ce qu'il se passe)
    - Pour les plus avancés, vous pourrez optimiser ce code en
      l'adoptant avec vos conaissances (boucles, fonctions, classes etc.)
"""
# =============================================================================
# Réponse
# =============================================================================
from game import Titan #ma classe
import random 
#----------------------------------------------------------------------------
    #Avant que le combat ne commence...
input("(<) règles du jeu")
Titan.rules()
input("(<) début")
print("Messieurs les titans, puissions-nous connaitre vos noms ?")
    #création des titans
Titan(input(f"Nom Titan numéro 1 : "))
Titan(input(f"Nom Titan numéro 2 : "))

titans = Titan.titans #(voir attribut 'titans' de classe 'Titan')
print(f"{titans[0].name}, {titans[1].name} : Affrontez vous !\n")
#----------------------------------------------------------------------------
    #combat:
my_indexs = [0, 1]
n_attempts = 0
(id_attacker, id_target) = my_indexs.copy() #roles (attaquant/cible)
while True: #boucle infini
    n_attempts += 1
    if random.choice((True, False)):#si tentative d'attaque marche
        damage = random.randrange(100)
        print(f"la tentative d'attaque ({n_attempts}) de {titans[id_attacker].name} a réussie")
            #methodes class Titan utilisées:
        damage = Titan.real_damage(titans[id_target], damage)
        titans[id_target].health = Titan.real_health(titans[id_target], damage)
        print(f"\ril a infligé {damage} dégats à {titans[id_target].name}")
        for titan in titans:
            print(f"santé {titan.name} : {titan.health}")
        try:
            #santé de cible != 0 ?
            assert titans[id_target].health != 0
        except AssertionError:
            #santé de cible == 0            
            print(f"\nVoici le ou les gagnants : {Titan.choose_winner()}")
            break #jeu prend fin
    else:
        print(f"\nla tentative d'attaque ({n_attempts}) de {titans[id_attacker].name} a échouée")
        #inverse les roles (attaquant/cible) --> prochain tour de boucle:
    my_indexs.reverse()
    (id_attacker, id_target) = my_indexs.copy()
    input("(<) continuer")
    