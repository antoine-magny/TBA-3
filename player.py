class Player():
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history_room = []
        self.inventory = {}
    
    def move(self, direction, game):
        next_room = self.current_room.exits.get(direction)
        self.get_history()
        

        if next_room is None:
            print("\nIl n'y a aucune île dans cette direction !\n")
            return False
        
        if next_room == "mort": 
            print("\nDe terribles monstres marins rôdent par içi. Soudain, un énorme vache des mers renverse votre navire ! Vous êtes de mort !\n")
            game.finished = True
            return False
        
        self.history_room.append(self.current_room)
        self.current_room = next_room  # Déplacement effectué
        print(self.current_room.get_long_description())
        return True
    
    def get_inventory(self):
        if not self.inventory:
            print("\nVotre inventaire est vide.")
        else:
            print("\nVotre inventaire :")
            for item in self.inventory:
                print(f"-  : {item.description} ({item.weight} kg)")
    
    def get_history(self):
        if len(self.history_room) == 0:  
            print("\nAucune île n'a encore été visitée.")
            return False
        
        liste_room = []
        liste_room_unique = []
        
        print("\nVous êtes déjà allé sur les îles suivantes :")
        
        for room in self.history_room:  
            liste_room.append(room.name)  
        
        if len(liste_room) == 0: 
            print("\nAucune île précédente à afficher.")
            return False

        for element in liste_room:
            if element not in liste_room_unique:
                liste_room_unique.append(element)
        
        for room_name in liste_room_unique:
            print(f"- {room_name}")
        return liste_room_unique
    
    
    def back(self):
        if not self.history_room:
            print("\nImpossible de revenir en arrière. Vous êtes au village de Luffy, la première île du jeu !")
            return False
        
        previous_room = self.history_room.pop()
        
        if self.current_room != previous_room:
            self.current_room = previous_room
            print(f"\nVous êtes retourné à l'endroit précédent : {self.current_room.name}")
            print(self.current_room.get_long_description())
        else:
            print("\nImpossible de revenir en arrière. Vous êtes au village de Luffy, la première île du jeu !")
        return True
