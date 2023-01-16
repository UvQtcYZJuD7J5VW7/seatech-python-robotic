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

    def startupGeneric(self):
        self.__state = True
        self.startup()

    @abstractmethod
    def stop(self):
        pass

    def stopGeneric(self):
        self.__state = False
        self.stop()

class Aircraft():

    # Attributes
    __

class UAV(UnmannedVehicle):
    def startup(self):
        print("Pompe électrique ON")
        print("Plein riche")
        print("Démarreur 5 sec")
        print("Moteur démarré")

    def stop(self):
        print("Régime 1200 trs/min")
        print("Plein pauvre")
        print("Moteur arrrêté")

class UUV(UnmannedVehicle):
    def startup(self):
        print("Ecoutilles fermées")
        print("Démarreur 5 sec")
        print("Moteur démarré")

    def stop(self):
        print("Ecoutilles ouvertes")
        print("Retirer les clefs")
        print("Moteur arrrêté")

class UGV(UnmannedVehicle):
    def startup(self):
        print("Démarreur 5 sec")
        print("Moteur démarré")

    def stop(self):
        print("Retirer les clefs")
        print("Moteur arrrêté")

if __name__ == "__main__":
        
    uav = UAV()
    uav.startupGeneric()
    uav.stopGeneric()

    print("\n")

    ugv = UGV()
    ugv.startupGeneric()
    ugv.stopGeneric()

    print("\n")

    uuv = UUV()
    uuv.startupGeneric()
    if(uuv.getState == True):
        print("--> Moteur allumé")
    else:
        print("--> Moteur éteindre")
    uuv.stopGeneric()