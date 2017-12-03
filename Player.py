class Player:
    def __init__(self, userName):
        self.x = 1
        self.y = 4
        self.userName = userName
        self.inventory = []
        self.score = 5
        self.moves = 20
        self.location = 3
        self.winOrLose = "none"
    def updateLocation(self):
        self.location = worldMatrix[self.y][self.x]
    def use(self, item):
        if item in self.inventory:
            if item == "camera":
                print("You took a photo")
            elif item == "baby" and self.location == 10:
                self.winOrLose = "win"
        else:
            print("you don't have the item")
