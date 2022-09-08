# keyword class voor het definieren van een class. Gevolgd door de naam van jouw class (car).
class Car:
    # _init_ functie. Deze functie wordt gebruikt wanneer een nieuw object wordt aangemaakt door Car()
    # aan te roepen
    def _init_(self, color, wheel_count, door_count, type, has_airbags):
        # hier koppelen we de meegekregen parameters aan de properties van de instantie (het object)
        self.color = color
        self.wheel_count = wheel_count
        self.door_count = door_count 
        self.type = type
        self.has_airbags = has_airbags
    #hieronder volgen de functions/methods die het gedrag realiseren
    def start(self):
        # schrijf hier de code die de auto laat rijden (pass betekent "doe niks")
        pass
    def drive(self):
        # schrijf hier de code die de auto laat rijden (pass betekent "doe niks")
        pass
    def honk(self):
        return "tuuut!"
    def brake(self):
        # schrijf hier de code die de auto laat remmen (pass betekent "doe niks")
        pass
    def turn(self):
        # schrijf hier de code die de auto laat draaien (pass betekent "doe niks")
        pass

car1 = Car('Paars', 6, 24, 'Fiat Panda', True)
car1.start()