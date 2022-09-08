
class PacPerson:
    def _init_(self, speed, lives):
        self.lives = lives
        self.speed = speed

    def eat(self, bolletjeOfSpookje):
        pass
    def drive(self):
        pass
    def movement(self,direction):
        pass
    def playsound(self,sound):
        pass
    def respawn(self):
        pass

class Ghost:
    def _init_(self,speed, color, mode):
        self.color = color
        self.speed = speed
        self.mode = mode

    def follow(self):
        pass
    def suprise(self):
        pass
    def wander(self):
        pass
    def chooseMode(self):
        pass
    def movement(self,direction):
        pass
    def playsound(self,sound):
        pass
    def respawn(self):
        pass
    def run(self):
        pass

PacMan = PacPerson(10, 3)
Pinky = Ghost(1,'Pink','suprise')
Blinky = Ghost(1.2,'Red', 'follow')