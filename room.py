# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    
    # definir un passage interdit
    
    forest.set_forbidden_exit("E")
    tower.set_forbidden_exit("O")
    tower.set_forbidden_exit("S")
    
    # test passeage interdit 
    current_room = forest 
    direction = "E"
    
    next_room = current_room.get_exit(direction)
    if next_room:
        current_room = next.room
        print(current_room.get_long_description.)
    else:
        print("Vous ne pouvez pas aller dans cette direction.")
        
