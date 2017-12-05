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
        self.worldMatrix = worldMatrix = [
                        [ -1,-1,-1, -1,-1],
                        [ -1, 7, 6, 8, -1],
                        [ -1, 5, 1, 10,-1],
                        [ -1, 2, 0, 11,-1],
                        [ -1, 3, 4, 9, -1],
                        [ -1,-1,-1,-1, -1]
                        ]
    def updateLocation(self):
        self.location = self.worldMatrix[self.y][self.x]
    
    def use(self, item):
        if item in self.inventory:
            if item == "camera":
                print("You took a photo")
            elif item == "baby" and self.location == 10:
                self.winOrLose = "win"
        else:
            print("you don't have the item")
