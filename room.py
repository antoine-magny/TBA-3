"""
Description: Room class
"""

class Room:
    """
    Classe représentant un lieu dans le jeu.

    Attributes:
        name (str): Le nom de la salle.
        description (str): Une description textuelle de la salle.
        exits (dict): Un dictionnaire des sorties.
        inventory (dict): Un dictionnaire des objets disponibles dans la salle.
        characters (dict): Un dictionnaire des personnages présents dans la salle.
    """
    def __init__(self, name, description):
        """
        Initialise une nouvelle salle.

        Args:
            name (str): Le nom de la salle.
            description (str): La description de la salle.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}

    def get_exit(self, direction) :
        """
        Retourne la salle associée à une direction donnée.

        Args:
            direction (str): La direction (ex. : 'N', 'S').

        Returns:
            Room or None: La salle associée ou None si la direction est invalide.
        """
        if direction in self.exits:
            return self.exits[direction]
        return None

    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties disponibles.

        Returns:
            str: Une description des sorties.
        """
        exit_string = "Sorties: "
        for exit_direction in self.exits :
            if self.exits[exit_direction] is not None:
                exit_string = exit_string + exit_direction  + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """
        Retourne une description complète de la salle.

        Returns:
            str: Une description détaillée de la salle.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Affiche les objets présents dans la salle.
        """
        if not self.inventory and not self.characters:
            print("\n- Il n'y a rien ici.")
        else:

            print("\n Dans cet endroit mystérieux, il y a :")
            for nom, objet in self.inventory.items():
                print(f"- {nom} : {objet['description']} ({objet['weight']} kg)")
