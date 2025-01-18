"""
Description: la classe Character
"""

class Character():
    """
    Représente un personnage non-joueur (PNJ) dans l'univers du jeu.

        Attributs :
        -----------
        name : str
            Le nom du personnage.
        current_room : Room
            La pièce ou l'île où se trouve actuellement le personnage.
        description : str
            Une description textuelle du personnage.
        msgs : list
            Une liste de messages que le personnage peut communiquer au joueur.

        Méthodes :
        __str__() -> str
            Retourne une représentation textuelle du personnage sous la forme
            "<nom> : <description>".
        get_msg() -> None
            Affiche un message du personnage au joueur. Les messages sont récupérés
            dans l'ordre, puis réintégrés en fin de liste pour créer un cycle.
    """
    def __init__(self, name, current_room, description, msgs):
        self.name = name
        self.current_room = current_room
        self.description = description
        self.msgs = msgs

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        """
        Affiche les messages des personnages.
        """
        if len(self.msgs) !=0 :
            msg = self.msgs.pop(0)
            self.msgs.append(msg)
            print(msg)
        else:
            print("- Ce personnage n'a rien à dire pour le moment.")
