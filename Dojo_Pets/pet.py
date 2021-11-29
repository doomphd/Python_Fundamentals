class Pet:
    def __init__( name , type , tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
    def sleep(self):
        print("Pet energy go up 25")
    def eat(self):
        print("Pet energy go up 25")
    def play(self):
        print("Pet energy go up 25")    
    def noise(self):
        print("Pet energy go up 25")

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound
