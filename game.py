"""
Description: Game class
"""
# Import modules

import random
from room import Room
from player import Player
from command import Command
from actions import Actions
from character import Character

class Game :
    """
    Classe principale du jeu d'aventure textuelle.

    Attributs:
        finished (bool): Indique si le jeu est terminé.
        rooms (list[Room]): Liste des salles du jeu.
        commands (dict): Commandes disponibles dans le jeu.
        player (Player): Joueur principal.

    Méthodes:
        setup(): Configure les salles, commandes et objets du jeu.
        play(): Lance la boucle principale du jeu.
        process_command(command_string): Traite une commande saisie par le joueur.
        print_welcome(): Affiche le message de bienvenue.
    """
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    # Setup the game
    def setup(self):

        """
        Setup commands
        """
        help_c = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help_c

        quit_command = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit_command
        self.commands["exit"] = quit_command

        go_c = Command("go",
        " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)",
        Actions.go, 1)
        self.commands["go"] = go_c

        history_c = Command("history", " : permet de présenter l'historique", Actions.history, 1)
        self.commands["history"] = history_c

        back_c = Command("back", " : revenir en arrièrre",
        Actions.back, 0)
        self.commands["back"] = back_c

        check_c = Command("check", " : vérifier les objets dans votre inventaire",
        Actions.check, 0)
        self.commands["check"] = check_c

        look_c = Command("look", " : observer les objets présents dans sur l'île",
        Actions.look, 0)
        self.commands["look"] = look_c

        take_c = Command("take", " 'objet' : prendre un objet sur l'île",
        Actions.take, 1)
        self.commands["take"] = take_c

        drop_c = Command("drop", " 'objet' : poser un objet sur l'île",
        Actions.drop, 1)
        self.commands["drop"] = drop_c

        talk_c = Command("talk", " <nom du PNJ> : discuter avec un personnage non joueur",
        Actions.talk, 1)
        self.commands["talk"] = talk_c

        # Nouveaux lieux :
        # Attention : format des descriptions des îles : "Vous êtes" + "description de l'île"
        arlong_park = Room("arlong_park",
        "dans la base redoutable d'Arlong et de ses hommes-poissons.")
        self.rooms.append(arlong_park)

        fuschia_village = Room("fuschia_village",
        "dans le paisible village natal de Luffy, situé en bord de mer. "
        "Attention aux monstres marins qui rôdent autour !")
        self.rooms.append(fuschia_village)

        shells_town = Room("shells_town",
        "dans une ville où la Marine est omniprésente, "
        "dominée par une immense base militaire.")
        self.rooms.append(shells_town)

        baratie = Room("baratie",
        "dans un restaurant flottant connu pour "
        "sa cuisine exceptionnelle et ses batailles épiques. "
        "Un certain sanji y est chef cuisinier.")
        self.rooms.append(baratie)

        grand_line = Room("Grand Line",
        "au milieu des mers où se trouve un passage "
        "à sens unique vers la route des pirates !")
        self.rooms.append(grand_line)

        royaume_de_drum = Room("Royaume de Drum",
        "dans une île où le froid règne, "
        "on y trouve un certain médecin appelé chopper.")
        self.rooms.append(royaume_de_drum)

        pays_de_wa = Room("Pays de Wa",
        "un pays où les samouraïs vivent en paix.")
        self.rooms.append(pays_de_wa)

        dresserosa = Room("dresserosa",
        "dans une ville où règne un tyran qui transforme ses "
        "malfaiteurs en jouets pour enfants.")
        self.rooms.append(dresserosa)

        little_garden = Room("Little Garden",
        "une île où deux géants de 100 ans se battent pour la gloire.")
        self.rooms.append(little_garden)

        alabasta = Room("alabasta",
        "un royaume désertique où règne une lutte contre un crocodile des sables.")
        self.rooms.append(alabasta)

        skypiea = Room("skypiea",
        "une île céleste, flottant dans un océan de nuages.")
        self.rooms.append(skypiea)



        # Create exits for rooms
        fuschia_village.exits = {
            "N": arlong_park,
            "E": shells_town,
            "S": grand_line,
            "O": baratie,
            "U": None,
            "D": None
        }
        arlong_park.exits = {
            "N": None,
            "E": None,
            "S": fuschia_village,
            "O": None,
            "U": None,
            "D": None
        }
        shells_town.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": fuschia_village,
            "U": None,
            "D": None
        }
        baratie.exits = {
            "N": None,
            "E": fuschia_village,
            "S": None,
            "O": None,
            "U": None,
            "D": None
        }
        grand_line.exits = {
            "N": None,
            "E": royaume_de_drum,
            "S": alabasta,
            "O": little_garden,
            "U": None,
            "D": None
        }
        royaume_de_drum.exits = {
            "N": None,
            "E": None,
            "S": pays_de_wa,
            "O": grand_line,
            "U": None,
            "D": None
        }
        pays_de_wa.exits = {
            "N": royaume_de_drum,
            "E": None,
            "S": "laugh_tale",
            "O": alabasta,
            "U": None,
            "D": None
        }
        alabasta.exits = {
            "N": grand_line,
            "E": pays_de_wa,
            "S": "mort",
            "O": dresserosa,
            "U": None,
            "D": None
        }
        dresserosa.exits = {
            "N": little_garden,
            "E": alabasta,
            "S": "mort",
            "O": None,
            "U": None,
            "D": None
        }
        little_garden.exits = {
            "N": None,
            "E": grand_line,
            "S": dresserosa,
            "O": None,
            "U": skypiea,
            "D": None
        }
        skypiea.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "U": None,
            "D": little_garden
        }

        # Ajout des objets sur les îles
        gomu_gomu_no_mi = {
            "description": "Fruit du démon qui donne des pouvoirs élastiques",
            "weight": 0.5
        }
        shimotsuki_kozaburo_katanas = {
            "description": "2 des 3 katanas de zoro",
            "weight": 4.0
        }
        wado_ichimonji = {
            "description": "L'épée donnée à titre posthume par Kuina à zoro",
            "weight": 2.0
        }
        shusui = {
            "description": "L'épée légendaire du samouraï Ryuma",
            "weight": 2.0
        }
        lance_pierre = {
            "description": "L'arme de prédilection d'Usopp",
            "weight": 1.0
        }
        rumble_ball = {
            "description": "Une drogue rendant chopper très puissant",
            "weight": 0.5
        }
        hana_hana_no_mi = {
            "description": "Fruit du démon des éclosions",
            "weight": 0.5
        }
        ito_ito_no_mi = {
            "description": "Fruit du démon des fils",
            "weight": 0.5
        }
        hache_du_cogneur = {
            "description": "Une hache pour Dorry, un des géants de Little Garden",
            "weight": 100.0
        }
        epee_brogy = {
            "description": "Une épée pour brogy, un des géants de Little Garden",
            "weight": 75.0
        }
        uo_uo_no_mi = {
            "description": "Fruit du dragon oriental",
            "weight": 4.0
        }
        one_piece = {
            "description": "Le trésor le plus grand de tous les temps"
        }

        # Ajout des objets sur les îles
        # lieu.inventory[clé] = valeur (la valeur étant le dictionnaire définit précédement)
        fuschia_village.inventory["Gomu Gomu no Mi"] = gomu_gomu_no_mi
        shells_town.inventory["Shimotsuki Kozaburo Katanas"] = shimotsuki_kozaburo_katanas
        shells_town.inventory["Wado Ichimonji"] = wado_ichimonji
        shells_town.inventory["Shusui"] = shusui
        shells_town.inventory["Lance-pierre"] = lance_pierre
        royaume_de_drum.inventory["Rumble Ball"]= rumble_ball
        alabasta.inventory["Hana Hana no Mi"]= hana_hana_no_mi
        dresserosa.inventory["Ito Ito no Mi"]= ito_ito_no_mi
        little_garden.inventory["Hache du Cogneur"]= hache_du_cogneur
        little_garden.inventory["Terry Sword"]= epee_brogy
        pays_de_wa.inventory["Uo Uo no Mi"]= uo_uo_no_mi

        # Personnages :
        # Ajout des PNJ dans les pièces
        makino = Character(
            "Makino",
            None,
            "La serveuse du bar de Fuschia Village",
            ["Tu veux une bière, mon ptit ?", "Bois un jus Luffy !"]
        )

        arlong = Character(
            "Arlong",
            None,
            "Chef des hommes-poissons et maître d'Arlong Park",
            ["Rendez-vous humains !", "Nami sera à moi pour toujours."]
        )

        zoro = Character(
            "Zoro",
            None,
            "Un sabreur à 3 épées",
            ["Les cicatrices sur le dos sont la honte d'un épéiste"]
        )

        sanji = Character(
            "Sanji",
            None,
            "Un cuisinier d'exception",
            [
                "La cuisine est un don de dieu, les épices un don du diable... "
                "Je crois que ce plat était un peu trop épicé pour toi !"
            ]
        )

        chopper = Character(
            "Chopper",
            None,
            "Un reine médecin",
            [
                "Luffy, si pour que tu atteignes ton but je dois devenir un monstre, "
                "alors j'en deviendrais un !!"
            ]
        )

        robin = Character(
            "Robin",
            None,
            "La seule personne sur la planète à lire les écritures anciennes",
            [
                "L'histoire se répète sans cesse, mais les hommes ne peuvent "
                "retourner sur le passé"
            ]
        )

        dorry = Character(
            "Dorry",
            None,
            "Un géant se battant pour la gloire",
            ["La raison de ce combat, il y a belle lurette qu'on l'a oubliée"]
        )

        brogy = Character(
            "Brogy",
            None,
            "Un géant se battant pour la gloire",
            ["Un siècle... ce fut vraiment un long combat!"]
        )

        doflamigo = Character(
            "Doflamigo",
            None,
            "Un tiran animé par le pouvoir",
            [
                "Les faibles ne pourront pas s'échapper, les forts feront la loi, "
                "place à une nouvelle ère !"
            ]
        )

        momo = Character(
            "Momo",
            None,
            "Un jeune souverain du Pays de Wa et fils du héros de ce pays",
            ["Je te le jure Luffy, un jour je battrai Kaido !"]
        )

        fuschia_village.characters = {"Makino": makino}
        arlong_park.characters = {"Arlong": arlong}
        shells_town.characters = {"zoro": zoro}
        baratie.characters = {"sanji": sanji}
        alabasta.characters = {"robin": robin}
        little_garden.characters = {"dorry": dorry}
        little_garden.characters = {"brogy": brogy}
        dresserosa.characters = {"doflamigo": doflamigo}
        pays_de_wa.characters = {"momo": momo}
        royaume_de_drum.characters = {"chopper": chopper}

        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = fuschia_village

    def move_characters(self):
        """Déplace un seul PNJ aléatoire vers une sortie aléatoire par tour."""
        all_characters = []
        for room in self.rooms:
            for name, character in room.characters.items():
                all_characters.append((name, character, room))
        if not all_characters:
            return  # Aucun PNJ à déplacer, on sort de la fonction

        name, character, current_room = random.choice(all_characters)

        exits = []
        for exit_i in current_room.exits.values():
            if isinstance(exit_i, Room):
                exits.append(exit_i)

        if not exits:
            return

        new_room = random.choice(exits)
        new_room.characters[name] = character
        del current_room.characters[name]
        character.current_room = new_room
        print(f"\n{character.name} s'est déplacé vers {new_room.name}.")

    # Play the game
    def play(self):
        """
        Fonction qui fait tourner le jeu en permanence.
        """
        self.setup()
        self.print_welcome()

        # Loop until the game is finished
        while self.finished is not True:
            self.process_command(input("> "))
            self.move_characters()
        return

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Récupère les commmandes tapés et exécute l'action ascociée
        """
        #Affiche rien lorsque le joueur tape "entrer"
        if command_string=='':
            return None
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"""\nCommande '{command_word}' non reconnue.
            Entrez 'help' pour voir la liste des commandes disponibles.\n""")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
        return None

    # Print the welcome message
    def print_welcome(self):
        """
        Affiche le message de bienvenue.
        """
        print("\nBienvenue dans ce jeu d'aventure ! "
        f"Votre pseudonyme est {self.player.name} et vous incarnez "
        "Luffy dans l'univers du manga One Piece. "
        "Quand vous aurez visité East blue (les premières îles du jeu), "
        "partez pour Grand Line au sud de Fuschia Village. "
        "Mais attention ! Une fois sur Grand Line vous ne pourrez plus faire marche arrière ! "
        "Bonne chance !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

def main():
    """
    Create a game object and play the game
    """
    Game().play()

if __name__ == "__main__":
    main()
