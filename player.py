"""
Description: Player class
"""

class Player():
    """
    Représente un joueur dans le jeu d'aventure.

    Cette classe contient les informations et comportements liés au joueur,
    y compris sa position actuelle, son inventaire et l'historique des lieux visités.

    Attributs:
        name (str): Le nom du joueur.
        current_room (Room): La salle où se trouve actuellement le joueur.
        history_room (list[Room]): L'historique des lieux visités par le joueur.
        inventory (dict): L'inventaire du joueur, stockant les objets sous la forme 
                          de paires {nom de l'objet: objet}.

    Méthodes:
        get_history(): Affiche et retourne l'historique des lieux visités.
        get_inventory(): Affiche le contenu de l'inventaire du joueur.
        move(direction, game): Déplace le joueur dans une direction spécifiée.
        back(): Ramène le joueur à son lieu précédent dans l'historique.
    """
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history_room = []
        self.inventory = {}

    def move(self, direction, game):
        """
        Déplace le joueur vers une direction spécifiée.

        Cette méthode met à jour la position actuelle du joueur si la direction
        est valide. Elle gère les cas spéciaux tels que les directions non valides
        ou les situations de fin de jeu.

        Args:
            direction (str): La direction dans laquelle le joueur souhaite se déplacer.
            game (Game): L'objet du jeu pour accéder aux données du jeu.

        Returns:
            bool: True si le déplacement est réussi, False sinon.
        """
        next_room = self.current_room.exits.get(direction)
        self.get_history()

        if next_room is None:
            print("\nIl n'y a aucune île dans cette direction !\n")
            return False

        if next_room == "mort":
            print("""\nDe terribles monstres marins rôdent par içi.
            Soudain, un énorme vache des mers renverse votre navire !
            Vous êtes de mort !\n""")
            game.finished = True
            return False

        self.history_room.append(self.current_room)
        self.current_room = next_room  # Déplacement effectué
        print(self.current_room.get_long_description())
        return True

    def get_inventory(self):
        """
        Affiche le contenu de l'inventaire du joueur.

        Cette méthode parcourt les objets de l'inventaire du joueur et affiche
        leurs noms, descriptions et poids. Si l'inventaire est vide, un message
        spécifique est affiché.

        Returns:
            None
        """
        if not self.inventory:
            print("\nVotre inventaire est vide.")
        else:
            print("\nVotre inventaire :")
            for item in self.inventory:
                print(f"-  : {item.description} ({item.weight} kg)")

    def get_history(self):
        """
        Affiche le contenu de l'inventaire du joueur.

        Cette méthode parcourt les objets de l'inventaire du joueur et affiche
        leurs noms, descriptions et poids. Si l'inventaire est vide, un message
        spécifique est affiché.

        Returns:
            None
        """
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
        """
        Ramène le joueur à son lieu précédent.

        Cette méthode permet au joueur de revenir dans le dernier lieu visité,
        à condition que l'historique des lieux ne soit pas vide. Si le joueur
        est déjà au point de départ, un message spécifique est affiché.

        Returns:
            bool: True si le retour en arrière est effectué, False sinon.
        """
        if not self.history_room:
            print("""\nImpossible de revenir en arrière.
            Vous êtes au village de Luffy, la première île du jeu !""")
            return False

        previous_room = self.history_room.pop()

        if self.current_room != previous_room:
            self.current_room = previous_room
            print(f"\nVous êtes retourné à l'endroit précédent : {self.current_room.name}")
            print(self.current_room.get_long_description())
        else:
            print("""\nImpossible de revenir en arrière.
            Vous êtes au village de Luffy, la première île du jeu !""")
        return True
