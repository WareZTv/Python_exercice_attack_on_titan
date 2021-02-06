# =============================================================================
# Module game
# =============================================================================


# =============================================================================
# Classe Player

class Titan:
    """
    class of participants in the game "Attack on Titan".
    We can create Titans, which can attack other Titans, ...
    to simulate a fight from "Attack on Titan"    
    -------------------------------------------------------------------------"""
    titans = []
    #----------------------------------------------------------------------  
        #builder:
    def __init__(self, name):
        """
        (<) name : str--> the name of the titan.
        we add the titan ID to 'titans' class attribut"""
        self.name = name
        self.health = 250
        Titan.titans.append(self)    
    #---------------------------------------------------------------------    
        #static methods:
    def rules():
        """announce the rules of the game"""
        print("\n\
        \tMmmmm... Si vous etes ici, j'imagine que votre décision est prise !\n\
        Je ne veux pas vous inciter à arreter mais vous etes conscient des risques ?\n\
        Vous participez quand meme au plus grand combat de tous les temps...\n\n\
        \tBon je vous explique les règles : Vous allez affronter un autre titan en duel\n\
        Vous avez chacun des tentatives d'infliger une attaque. Si elles réussissent,\n\
        Vous aurez le choix d'infliger entre 0 et 100 dégats. Enfin non puisque tout\n\
        sera tiré au sort   :)\n\
        La partie s'arrete quand l'un des deux titans est mort\n\
        \tBonne chance a vous!\n")
    
    def simulate_attack(target, damage):
        """
        (<) target : titan --> the target of simulate attack
        (<) damage : int   --> the damage to be inflicted (simulate) on the target.       
        simulate an attack and return the new health of the target"""
        return target.health - damage
    
    def real_damage(target, damage):
        """
        (<) target : class 'Titan' --> the target for of 'simulate_attack' method.
        (<) damage : class 'int'   --> the damage for the 'simulate_attack' method.
        if the health of the target returns by the 'simulate_attack' method is negative:
            change the inflicted damage value by deducting the damage inflicted too much
        return the inflicted damage (whether it is changed or not)."""
        health_target = Titan.simulate_attack(target, damage)
        if health_target < 0:
            damage = damage + health_target
        return damage
    
    def real_health(target, damage):
        """
        (<) target : class 'Titan' --> the target for of 'simulate_attack' method.
        (<) damage : class 'int'   --> the damage for the 'simulate_attack' method.
        if the target health returns by the 'simulate_attack' method is negative:
            change health value to 0
        return the target health (whether it is changed or not)"""
        health_target = Titan.simulate_attack(target, damage)
        if health_target < 0:
            health_target = 0
        return health_target
    
    def health_titans():
        """return a list of the health of all titans already created"""
        return [titan.health for titan in Titan.titans]
    
    def max_health():
        """return the max health of all titans"""
        max_health = max(Titan.health_titans())
        return max_health
            
    def choose_winner():
        """return a tuple of winner's name(s) (by comparing their health)""" 
        max_health = Titan.max_health()
        winners = tuple((titan.name for titan in Titan.titans if titan.health == max_health))
        return winners
    
    rules = staticmethod(rules)
    simulate_attack = staticmethod(simulate_attack)   
    real_damage = staticmethod(real_damage)
    real_health = staticmethod(real_health)
    health_titans = staticmethod(health_titans)
    max_health = staticmethod(max_health)
    choose_winner = staticmethod(choose_winner)   