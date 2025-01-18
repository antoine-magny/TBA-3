"""
Description: The actions module.
"""

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command hhhh
# The functions return True if the command was executed successfully, False otherwise. 
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

from item import *

class Actions:

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
        # Get the direction from the list of words.
        direction = list_of_words[1]
        
        #Convertir la direction en majuscule
        direction = direction.upper()
        if direction in directions:
            direction = directions[direction]
            player.move(direction,game)
        else:
            print(f"Direction '{direction}' non reconnue.")
        return True
    
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
    
    
    def look(game, list_of_words, number_of_parameters):
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
    
    def take(game, list_of_words, number_of_parameters):
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
        else:
            print(f"\nL'objet '{item_name}' n'est pas présent sur cette île.")
            return False


    def drop(game, list_of_words, number_of_parameters):
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
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans votre inventaire.")
            return False
    
    def history(game, list_of_words, number_of_parameters):
        player = game.player

        if len(player.history_room) == 0: # Vérifie si une île a été visitée est vide
            print("\nVous n'avez encore visité aucune île.") # Message si aucune île n'a été visitée
            return True  # Terminer l'exécution avec succès

        # Afficher l'historique des îles visitées
        print("\nHistorique des îles visitées :") # Message d'information
        for room in player.history_room: # Parcourt les îles visitées
            print(f"- {room.name}") # Affiche le nom de chaque île visitée
        return True

    def back(game, list_of_words, number_of_parameters):
        player = game.player
        return player.back()
    
    def check(game, list_of_words, number_of_parameters):
        player = game.player
        if not player.inventory:
            print("\nVotre inventaire est vide.")
            return True
        
        print("\nVotre inventaire contient les objets suivants :")
        # Parcourt les paires clé/valeur. Dans chaque paire, nom est la clé et objet est la valeur. Et dans chaque objet, il y a une description et un poids.
        for nom, objet in player.inventory.items(): 
            print(f"- {nom} : {objet['description']} ({objet['weight']} kg)")
        return True
    
    
    def talk(game, list_of_words, number_of_parameters):
        current_room = game.player.current_room

        if len(list_of_words) < 2:
            print("\nUtilisation : talk <nom du PNJ>")
            return False

        character_name = " ".join(list_of_words[1:])
        if hasattr(current_room, "characters") and character_name in current_room.characters:
            current_room.characters[character_name].get_msg()
            return True
        else:
            print(f"\nAucun PNJ nommé '{character_name}' ici.")
            return False

