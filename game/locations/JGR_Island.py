from game import location
from game.display import announce
import game.config as config
import game.items as items
import random

# Island
class FlowerIsland(location.Location):
    def __init__(self, x, y, world):
        super().__init(x,y,world)
        self.name = "island"
        self.symbol = 'F'
        self.visitable = True
        self.locations = {}
        self.starting_location = Beach_with_ship(self)

        self.locations["north_beach"] = self.starting_location
        self.locations["south_beach"] = South_beach(self)
        self.locations["west_beach"] = West_beach(self)

        self.locations["east_beach"] = East_beach(self)
        self.locations["shed"] = House(self)

        self.locations["south_jungle"] = South_jungle(self)
        self.locations["flower_forest"] = Flower_forest(self)
        # area only accessable through the flower forest in the south jungle
        self.locations["central_castle_wall"] = Central_castle_wall(self)
        self.locations["central_castle"] = Central_castle(self)

    def enter(self, ship):
        announce("You arrive at a foggy island covered in flowers")

    def visit(self):
        config.the_player.location = self.starting_location

# Sub-locations
class Beach_with_ship(location.Sublocation):
    def __init__ (self, main_location):
        super().__init__(main_location)
        self.name = "north_beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        self.event_chance = 20
        self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        description = "You exit the ship and onto the island.\nEverything is so colorful it doesn't feel like reality."
        announce(description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north"):
            announce ("You return to your ship and begin to depart from the island"
            if (central_castle_switch_flipped == True):
                config.the_player.next_loc = config.the_player.ship
                config.the_player.visiting = False
            else:
                #some random number to determine if the ship survives
        elif (verb == "south"):
            announce ("The fog becomes too thick and eventually you find yourself where you started."
        elif (verb == "west" or verb == "east"):
            config.the_player.next_loc = self.main_location.locations[f"{verb}Beach"]
            # a switch needs to be added to the central castle to allow
            # the player to leave without any worry to destroying the ship
            
            
            
        
"""trying to go across the island like from west beach to east beach will
result in the player getting lost and ending up where they started unless
they are in the south and travel into the flower forest then from there to
the central castle wall then into the castle and then from the interior
castle they can go which ever way they want. The castle should be a five
room dungeon. Trying to leave the island after going ashore will have a
very high chance of killing every pirate alive. Island is supposed to be
a tough challenge but if successful you get a lot of useful items and lots
of shillings"""
