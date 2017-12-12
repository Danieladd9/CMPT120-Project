class Player:
    def __init__(self, userName):
        self.x = 1
        self.y = 4
        self.userName = userName
        self.inventory = []
        self.score = 5
        self.moves = 20
        self.location = 3
        self.previous = 3
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
        self.previous = self.location
        self.location = self.worldMatrix[self.y][self.x]

    def backTrack(self):
        self.location = self.previous
        print("you back tracked")
    
    def use(self, item):
        if item in self.inventory:
            if item == "camera":
                print("You took a photo")
            elif item == "baby" and self.location == 10:
                self.winOrLose = "win"
            elif item == "fries":
                print("You eat the fries")
                print("Hey did you eating more moves?")
                self.moves = self.moves + 5
                self.inventory.remove(item)
            
        else:
            print("you don't have the item")
            
    def playerInventory(self):
        print(self.inventory)
        
    def playerPray(self):
        if "baby" in self.inventory:
            print("Take the to the Admission Office her mother is looking for her")
        else:
            print("Go find the lost baby in Legoland")

    def playerConverse(self):
        if "baby" in self.inventory:
            print("The baby is whinning to you")
        elif "baby" not in self.inventory and self.location == 10:
            print("I lost my baby our baby in Legoland")
        else:
            print("You talk to yourself")
            
        
