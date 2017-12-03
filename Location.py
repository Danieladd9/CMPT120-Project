class Location:
    #location class holds all the items the name descirpiton and if it has been searched or visited
    def __init__(self, shortName, items, description):
        self.description = description
        self.name = shortName
        self.items = items
        self.hasVisited = False
        self.hasSearched = False
    #tells the player if any items are there and sets the search value to true
    def search(self):
        if self.items == []:
            print("There are no items here")
        else:
            itemList = ""
            for i in self.items:
                itemList += i
            print("you see the following items " + itemList)
        self.hasSearched = True
    def look(self):
        print("\nYour current Location is " + self.description)
    def take(self, item):
        if self.hasSearched == True:
            if item in self.items:
                print("you picked up a " + item)
                self.items.remove(item)
            else:
                print("there nothing there to take")
        else:
            print("You do not see anything")
    def drop(self, item, inventory):
        if item in inventory:
            print("you dropped a " + item)
            inventory.remove(item)
            self.items.append(item)
        else:
            print("you don't have that item")
