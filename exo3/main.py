from abc import ABCMeta, abstractmethod

class UnmannedVehicle(metaclass=ABCMeta):

    # Attributes
    __state = False

    # Methods
    @property
    def getState(self) -> bool:
        return self.__state

    @abstractmethod
    def startup(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class UAV(UnmannedVehicle):
    def startup(self):
        self.__state = True
        print("Pompe électrique ON")
        print("Plein riche")
        print("Démarreur 5 sec")
        print("Moteur démarré")

    def stop(self):
        self.__state = False
        print("Régime 1200 trs/min")
        print("Plein pauvre")
        print("Moteur arrrêté")

class UUV(UnmannedVehicle):
    def startup(self):
        self.__state = True
        print("Ecoutilles fermées")
        print("Démarreur 5 sec")
        print("Moteur démarré")

    def stop(self):
        self.__state = False
        print("Ecoutilles ouvertes")
        print("Retirer les clefs")
        print("Moteur arrrêté")

class UGV(UnmannedVehicle):
    def startup(self):
        self.__state = True
        print("Démarreur 5 sec")
        print("Moteur démarré")

    def stop(self):
        self.__state = False
        print("Retirer les clefs")
        print("Moteur arrrêté")

if __name__ == "__main__":
        
    uav = UAV()
    uav.startup()
    uav.stop()

    print("\n")

    ugv = UGV()
    ugv.startup()
    ugv.stop()

    print("\n")

    uuv = UUV()
    uuv.startup()
    uuv.stop()
    if(uuv.getState == True)
    {
        print("Moteur allumé")
    }
    else
    {
        print("Moteur éteindre")
    }