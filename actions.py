"""
Description: The actions module.
"""

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.
# The error message is stored in the MSG0 and MSG1 variables and formatted
# with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """
    Cette classe regroupe les fonctions qui définissent les actions disponibles dans le jeu.

    Les fonctions de cette classe sont associées aux commandes disponibles pour le joueur
    et permettent d'interagir avec l'environnement du jeu. 
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False
        """

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Toutes les directions valides
        directions= {
            "N": "N", "NORD": "N",
            "S": "S", "SUD": "S",
            "E": "E", "EST": "E",
            "O": "O", "OUEST": "O",
            "U": "U", "UP": "U",
            "D": "D", "DOWN": "D",
            }
        direction = list_of_words[1]

        direction = direction.upper()
        if direction in directions:
            direction = directions[direction]
            player.move(direction,game)
        else:
            print(f"Direction '{direction}' non reconnue.")
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Affiche les objets et les personnages présents dans la pièce actuelle.
        """

        l = len(list_of_words)

        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        current_room = game.player.current_room
        current_room.get_inventory()

        for name, character in current_room.characters.items():
            print(f"- {name} : {character.description}")
        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet présent dans la pièce.
        """

        player = game.player
        current_room = player.current_room

        if len(list_of_words) < 2:
            print("\nUtilisation : drop <nom de l'objet>")
            return False

        item_name = " ".join(list_of_words[1:])
        if item_name in current_room.inventory:
            player.inventory[item_name] = current_room.inventory.pop(item_name)
            print(f"\nVous avez pris l'objet '{item_name}'.")
            return True
        print(f"\nL'objet '{item_name}' n'est pas présent sur cette île.")
        return False

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un objet dans la pièce actuelle.
        """

        player = game.player
        current_room = player.current_room

        if len(list_of_words) < 2:
            print("\nUtilisation : drop <nom de l'objet>")
            return False

        item_name = " ".join(list_of_words[1:])
        if item_name in player.inventory:
            current_room.inventory[item_name] = player.inventory.pop(item_name)
            print(f"\nVous avez déposé l'objet '{item_name}'.")
            return True
        print(f"\nL'objet '{item_name}' n'est pas dans votre inventaire.")
        return False

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.
        """

        player = game.player

        if len(player.history_room) == 0:
            print("\nVous n'avez encore visité aucune île.")
            return True

        print("\nHistorique des îles visitées :")
        for room in player.history_room:
            print(f"- {room.name}")
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir à la pièce précédente.
        """
        player = game.player
        return player.back()

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire du joueur.
        """

        player = game.player
        if not player.inventory:
            print("\nVotre inventaire est vide.")
            return True

        print("\nVotre inventaire contient les objets suivants :")
        for nom, objet in player.inventory.items():
            print(f"- {nom} : {objet['description']} ({objet['weight']} kg)")
        return True

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet de parler à un personnage non-joueur dans la pièce actuelle.
        """

        current_room = game.player.current_room

        if len(list_of_words) < 2:
            print("\nUtilisation : talk <nom du PNJ>")
            return False

        character_name = " ".join(list_of_words[1:])
        if hasattr(current_room, "characters") and character_name in current_room.characters:
            current_room.characters[character_name].get_msg()
            return True
        print(f"\nAucun PNJ nommé '{character_name}' ici.")
        return False
