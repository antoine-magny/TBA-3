"""
Description: la classe Character
"""

import random
from config import DEBUG

class Character():
    def __init__(self, name, current_room, description, msgs):
        self.name = name
        self.current_room = current_room
        self.description = description
        self.msgs = msgs

    def __str__(self):
        return f"{self.name} : {self.description}"
    
    def get_msg(self):
        if len(self.msgs) !=0 :  # Vérifie s'il y a des messages
            # Récupère le premier message et le replace à la fin
            msg = self.msgs.pop(0)
            self.msgs.append(msg)
            print(msg)
        else:
            print("- Ce personnage n'a rien à dire pour le moment.")
    
    
    def move(self):
        
        if random.choice([True, False]) is False:
            if DEBUG:
                print(f"DEBUG: {self.name} ne se déplace pas.")
            return False

        # Récupérer les salles adjacentes dans self.current_room.exits
        possible_exits = []
        for direction, room in self.current_room.exits.items():
            if room is not None: 
                possible_exits.append(room)

        if not possible_exits:
            if DEBUG:
                print(f"DEBUG: {self.name} est bloqué, aucune sortie disponible.")
            return False

        # Choisir une pièce aléatoire
        new_room = random.choice(possible_exits)

        # Retirer le PNJ de l'ancienne salle
        if self in self.current_room.characters:
            self.current_room.characters.remove(self)

        # Placer le PNJ dans la nouvelle salle
        self.current_room = new_room
        new_room.characters.append(self)

        if DEBUG:
            print(f"DEBUG: {self.name} se déplace vers {new_room.name}")
        return True


