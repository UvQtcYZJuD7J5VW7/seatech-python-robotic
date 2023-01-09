from subclass.Robot import Robot
from subclass.Human import Human

class Cyborg(Robot, Human):
    """
    Documentation du cyborg
    """

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def __str__(self):
        return Robot.__str__(self) + "\n" + Human.__str__(self)

if __name__ == "__main__":

    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.getName(), 'sexe', cyborg.sex)
    print('Charging battery...')
    cyborg.start()
    cyborg.charge(80)
    print(cyborg)
    cyborg.feed('banana')
    cyborg.feed(['coca', 'chips', "machin", "truc"])
    print(cyborg)
    try:
        cyborg.feed("Steak1")
    except Exception as e:
        print(e)
    cyborg.digest()
    try:
        cyborg.feed("Steak1")
    except Exception as e:
        print(e)
    print(cyborg)
    cyborg.poo()
    print(cyborg)