
class Room:
    def __init__(self, name, description): 
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {} # dictionnaire de dictionnaire (chaque objet est un dictionnaire)
        self.characters = {} # dictionnaire de dictionnaire (chaque personnage est un dictionnaire)
    
    
    
    def get_exit(self, direction) :
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string = exit_string + exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
    
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        if not self.inventory and not self.characters:
            print("\n- Il n'y a rien ici.")
        else:
            
            print("\n Dans cet endroit mystérieux, il y a :")
            # Parcourt l'inventaire du lieu (avec les variables "nom" et "objet") pour récupérer les noms, les descriptions et le poids des objets
            for nom, objet in self.inventory.items():
                print(f"- {nom} : {objet['description']} ({objet['weight']} kg)")
        

