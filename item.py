"""
Description: la classe Item
"""

class Item :
    """
        Représente un objet que le joueur peut trouver, transporter ou utiliser.

        Attributs :
        -----------
        name : str
            Le nom de l'objet.
        description : str
            Une description de l'objet.
        weight : float
            Le poids de l'objet.

        Méthodes :
        ----------
        __str__() -> str
            Retourne une représentation textuelle de l'objet sous la forme
            "<nom> : <description> (<poids> kg)".
    """
    def __init__(self, name, description,weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} "  f"({self.weight} kg)"
