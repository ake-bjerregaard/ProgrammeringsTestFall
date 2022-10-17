#3 klasser
#Fisk superklass
#Gädda ärver från Fisk
#Aborre ärver från Fisk
#Fisk ska ha attributet simhastighet

class Fisk:
    
    def __init__(self, simhastighet):
        self.simhastighet = simhastighet

class Gädda(Fisk):

    def __init__(self, simhastighet):
        super().__init__(simhastighet)


class Aborre(Fisk):
    
    def __init__(self, simhastighet):
        super().__init__(simhastighet)