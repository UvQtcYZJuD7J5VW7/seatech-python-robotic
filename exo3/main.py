from abc import ABCMeta, abstractmethod

class UnmannedVehicle(metaclass=ABCMeta):
    """
    Classe abstraite, redéfinir les méthodes suivantes :
    |   startup(self) -> bool
    |   stop(self) -> bool
    """

    # Attributes
    __state = False

    # Methods
    @property
    def getState(self) -> bool:
        """
        Renvoie False (défaut) si UnmannedVehicle arreté
        Renvoie True si UnmannedVehicle démarré
        """
        return self.__state

    @abstractmethod
    def startup(self) -> bool:
        """
        Démarrer le véhicule
        Pas d'arguments
        Renvoie True si UnmannedVehicle a démarré
        """
        pass

    @abstractmethod
    def stop(self):
        pass

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
     # Attributes
    __seaSpeed = 0
    
    # Methods
    def pitch(self, pitch:int) -> None:
        """
        Permet de définir l'assiette UUV
        Une exception est levée si UUV arreté
        Confirme l'assiette si réussite
        """
        if(self.__state == False):
            raise Exception("UUV stoppé")
        else:
            if(pitch < 0):
                print("UUV en descente")
            elif(pitch == 0):
                print("UUV stabilisé")
            elif(pitch > 0):
                print("UUV en montée")
            else:
                print("Comportement indéfini")

class UGV(UnmannedVehicle):
    """Unmanned Ground Vehicle"""
    pass

if __name__ == "__main__":
        
    uav = UAV()
    uav.startup()
    uav.stop()

    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()

    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()