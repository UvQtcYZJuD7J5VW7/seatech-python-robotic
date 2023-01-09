"""
Adrien
Rev-A (09/01/2023) : Initial dev
"""

class Human():   
    """
    Documentation de l'humain
    """

    # Attributes
    __dict = {
        "M": "Male",
        "F": "Female"
    }
    __sex = ""
    __food_in_instestine = []
    __intestine_limit = 5

    # Accessors
    @property
    def sex(self) -> str:
        return self.__sex

    @property
    def food(self) -> list:
        return self.__food_in_instestine

    def appendFood(self, foodstuff) -> None:
        if(len(self.__food_in_instestine) < self.__intestine_limit):
            self.__food_in_instestine.append(foodstuff)
        else:
            raise Exception("Too much food ! Please, digest.")

    # Methods
    def __init__(self, sex:str) -> None:
        if(sex in self.__dict):
            self.__sex = self.__dict[sex]
        else:
            raise Exception("Sexe inexistant")

    def __str__(self) -> str:
        return str(self.food)

    def feed(self, foodstuff:str) -> None:
        if(type(foodstuff) == list):
            for f in foodstuff:
                self.appendFood(f)
        else:
            self.appendFood(foodstuff)

    def digest(self) -> None:
        self.__food_in_instestine.pop(0)
        print("Digestion -1")

    def poo(self):
        self.__food_in_instestine.clear()
        print("Cyborg has emptied itself")

if __name__ == "__main__":
    h = Human("M")
    print(h.sex)
    h.feed("Steak1")
    h.feed("Steak2")
    h.feed("Steak3")
    h.feed("Steak4")
    h.feed("Steak5")
    try:
        h.feed("Steak6")
    except Exception as e:
        print(e)
    print(h.food)
    h.digest()
    print(h.food)
    try:
        h.feed("Steak8")
    except Exception as e:
        print(e)
    print(h.food)