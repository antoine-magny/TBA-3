# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
import random


class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    
    
    # Setup the game
    def setup(self):
        # Setup commands
        
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        self.commands["exit"] = quit    
        
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        
        history = Command("history", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.history, 1)
        self.commands["history"] = history
        
        back = Command("back", " : revenir en arrièrre", Actions.back, 0)
        self.commands["back"] = back
        
        check = Command("check", " : vérifier les objets dans votre inventaire", Actions.check, 0)
        self.commands["check"] = check
        
        look = Command("look", " : observer les objets présents dans sur l'île", Actions.look, 0)
        self.commands["look"] = look
        
        take = Command("take", " 'objet' : prendre un objet sur l'île", Actions.take, 1)
        self.commands["take"] = take
        
        drop = Command("drop", " 'objet' : poser un objet sur l'île", Actions.drop, 1)
        self.commands["drop"] = drop
        
        talk = Command("talk", " <nom du PNJ> : discuter avec un personnage non joueur", Actions.talk, 1)
        self.commands["talk"] = talk
        
        
        # Nouveaux lieux : 
        
        # Attention : format des descriptions des îles : "Vous êtes" + "description de l'île"
        
        Arlong_Park = Room("Arlong_Park", "dans la base redoutable d'Arlong et de ses hommes-poissons. Une navigatrice y est retenue prisonnière.")
        self.rooms.append(Arlong_Park)
        
        Fuschia_Village = Room("Fuschia_Village", "dans le paisible village natal de Luffy, situé en bord de mer. Attention aux monstres marins qui rôdent autour !")
        self.rooms.append(Fuschia_Village)
        
        Shells_Town = Room("Shells_Town", "dans une ville où la Marine est omniprésente, dominée par une immense base militaire. Un certain Capitaine Morgan y fait régner la terreur. Il retient prisonnier un sabreur et un tireur d'élite.")
        self.rooms.append(Shells_Town)
        
        Baratie = Room("Baratie", " dans un restaurant flottant connu pour sa cuisine exceptionel et ses batailles épiques. Un certain Sanji y est chef cuisinier.")
        self.rooms.append(Baratie)
         
        Grand_Line = Room("Grand Line", "au milieu des mers ce trouve un passage à sens unique vers l'avenir")
        self.rooms.append(Grand_Line)

        Royaume_de_Drum = Room("Royaume de Drum"," dans une iles où le froid reigne, on y trouve un certain medecin appelé Chopper")    
        self.rooms.append(Royaume_de_Drum)   

        Pays_de_Wa = Room("Pays de Wa"," un pays ou les samourais vive en paix. Ce trouve un indice important pour le trésor")  
        self.rooms.append(Pays_de_Wa)

        Alabasta = Room("Alabasta", "un pays de sable, un pays aride mélangé de pauvreté et de grande richesses, ce trouve la dernier femme de cette planete à pouvoir lire des indices pour trouver le trésor")
        self.rooms.append(Alabasta)

        Dresserosa = Room("Dresserosa" , " dans une ville où reigne un tiran qui traransforme ses malfeteurs en jouets pour enfants, ce trouve un indice important pour le trésor")
        self.rooms.append(Dresserosa)

        Little_Garden = Room("Little Garden" , "une iles ou 2 géant de 100ans ce battent pour la gloire")
        self.rooms.append(Little_Garden)

        Skypiéa = Room("Skypiéa","une ile volante, où ce trouve un indice imporant pour le trésor")
        self.rooms.append(Skypiéa)

        Laugh_Tale = Room("Laugh Tale","une ile secréte qui referme un trésor si tout les indices sont trouvés")
        self.rooms.append(Laugh_Tale)

        # Create exits for rooms
        Fuschia_Village.exits = {"N": Arlong_Park, "E": Shells_Town, "S": Grand_Line, "O": Baratie, "U": None, "D": None}
        Arlong_Park.exits = {"N": None, "E": None, "S": Fuschia_Village, "O": None, "U": None, "D": None}
        Shells_Town.exits = {"N": None, "E": None, "S": None, "O": Fuschia_Village, "U": None, "D": None}
        Baratie.exits = {"N": None, "E": Fuschia_Village, "S": None, "O": None, "U": None, "D": None}    
        Grand_Line.exits = {"N": None, "E": Royaume_de_Drum, "S": Alabasta, "O": Little_Garden, "U": None, "D": None}
        Royaume_de_Drum.exits = {"N": None, "E": None, "S": Pays_de_Wa, "O": Grand_Line, "U": None, "D": None}
        Pays_de_Wa.exits = {"N": Royaume_de_Drum, "E": None, "S": Laugh_Tale, "O": Alabasta, "U": None, "D": None}
        Alabasta.exits = {"N": Grand_Line, "E": Pays_de_Wa, "S": "mort", "O": Dresserosa, "U": None, "D": None}
        Dresserosa.exits = {"N": Little_Garden, "E": Alabasta, "S": "mort", "O": None, "U": None, "D": None}
        Little_Garden.exits = {"N": None, "E": Grand_Line, "S": Dresserosa, "O": None, "U": Skypiéa, "D": None}
        Skypiéa.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": Little_Garden}
        Laugh_Tale.exits = {"N": Pays_de_Wa, "E": None, "S": None, "O": None, "U": None, "D": None}
        
        """
        
        Demander à maxence de me faire le monde de one piece
        Genre les objets les îles et les personnages 
        
        
        """
        
        # Ajout des objets sur les îles
        gomu_gomu_no_mi = {"description": "Fruit du démon qui donne des pouvoirs élastiques", "weight": 0.5}
        Shimotsuki_Kozaburo_Katanas = {"description": "2 des 3 katanas de Zoro", "weight": 4.0}
        wado_ichimonji = {"description": "L'épée donnée à titre posthume par Kuina à zoro ", "weight": 2.0}        
        shusui = {"description": "L'épée légendaire du samouraï Ryuma", "weight": 2.0}
        lance_pierre = {"description": "L'arme de prédilection d'Usopp", "weight": 1.0}        
        Jambe_noir = {"description": "La jambe droite de Sanji", "weight": 0.5} 
        Rumble_Ball = {"description": "Une Drogue rendant Chopper très puissant", "weight": 0.5} 
        Hana_Hana_no_Mi = {"description": "Fruit des éclosions", "weight": 0.5}
        Ito_Ito_No_Mi = {"description": "Fruit des fils", "weight": 0.5}
        Hache_du_Cogneur = {"description": "Une hache pour les géant", "weight": 100.0}
        Terry_Sword = {"description": "Une épée pour les géant", "weight": 75.0}
        Uo_Uo_no_Mi = {"description": "Fruit du dragon oriental", "weight": 4.0}
        One_piece = {"description": "Le trésor le plus Grand de tout les temps"}
        # Ajout des objets sur les îles
        # lieu.inventory[clé] = valeur (la valeur étant le dictionnaire définit précédement)
        
        
        Fuschia_Village.inventory["Gomu Gomu no Mi"] = gomu_gomu_no_mi
        Shells_Town.inventory["Shimotsuki_Kozaburo_Katanas"] = Shimotsuki_Kozaburo_Katanas
        Shells_Town.inventory["Wado Ichimonji"] = wado_ichimonji
        Shells_Town.inventory["Shusui"] = shusui
        Shells_Town.inventory["Lance-pierre"] = lance_pierre
        Baratie.inventory["Jambe Noir"]= Jambe_noir
        Royaume_de_Drum.inventory["Rumble Ball"]= Rumble_Ball
        Alabasta.inventory["Hana Hana no Mi"]= Hana_Hana_no_Mi
        Dresserosa.inventory["Ito Ito no Mi"]= Ito_Ito_No_Mi
        Little_Garden.inventory["Hache du Cogneur"]= Hache_du_Cogneur
        Little_Garden.inventory["Terry Sword"]= Terry_Sword
        Pays_de_Wa.inventory["Uo Uo no Mi"]= Uo_Uo_no_Mi
        Laugh_Tale.inventory["One Piece"]= One_piece

        # Personnages : 
        # Ajout des PNJ dans les pièces
        makino = Character("Makino", None, "La serveuse du bar de Fuschia Village", ["Tu veux une bière, mon ptit ?", "Bois un jus Luffy !"])
        arlong = Character("Arlong", None, "Chef des hommes-poissons et maître d'Arlong Park", ["Rendez-vous humains !", "Nami sera à moi pour toujours."])
        Zoro = Character("Zoro",None, "Un sabreurà 3 épées " , [ "Les cicatrices sur le dos sont la honte d'un épéiste"])
        Sanji = Character("Sanji",None, "Un cuisinier d'éxection" , ["La cuisine est un don de dieu, les epices un don du diable... je crois que c'était un peu trop épicé pour toi"])
        Chopper = Character("Chopper", None,"Un reine médecin" ,["Luffy, si pour que tu atteignes ton but je dois devenir un monstre, alors j'en deviendrais un !!"])
        Robin = Character("Robin", None,"La seule personne sur la planete à lire les ecritures anciennes" ,["L'histoire se répète sans cesse, mais les hommes ne peuvent retourner dans le passé"])
        Dorry = Character("Dorry", None,"Un géant ce battant pour la gloire" ,["La raison de ce combat, il y a belle lurette qu'on l'a oubliée"])
        Brogy =Character("Brogy", None,"Un géant ce battant pour la gloire" ,["Un siècle... ce fut vraiment un long combat!"])
        Doflamigo = Character("Doflamigo", None,"Un tiran animé par le pouvoir" ,["Les faibles ne pourront pas s'échapper, les forts feront la loi, place à une nouvelle ère"])
        Momo = Character("Momo", None,"Un jeune souverain du Pays de Wa et fils du héros de ce pays" ,["Comment pouvons- noius vous regarder dans les yeux ?"])
        
        
        
        Fuschia_Village.characters = {"Makino": makino}
        Arlong_Park.characters = {"Arlong": arlong}
        Shells_Town.characters = {"Zoro": Zoro}
        Baratie.characters = {"Sanji": Sanji}
        Alabasta.characters = {"Robin": Robin}
        Little_Garden.characters = {"Dorry": Dorry}
        Little_Garden.characters = {"Brogy": Brogy}
        Dresserosa.characters = {"Doflamigo": Doflamigo}
        Pays_de_Wa.characters = {"Momo": Momo}
        
        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Fuschia_Village
    
    
    def move_characters(self):
        """Déplace un seul PNJ aléatoire vers une sortie aléatoire par tour."""
        # Créer une liste de tous les PNJs dans toutes les pièces
        all_characters = []
        for room in self.rooms:
            for name, character in room.characters.items():
                all_characters.append((name, character, room))
        
        if not all_characters:
            return  # Aucun PNJ à déplacer, on sort de la fonction
        
        name, character, current_room = random.choice(all_characters)
        
        exits = []
        for exit in current_room.exits.values():
            if isinstance(exit, Room):
                exits.append(exit)

        if not exits:
            return  # Pas de sorties valides pour déplacer le PNJ
        
        # Déplacer le PNJ vers une pièce aléatoire
        new_room = random.choice(exits)
        new_room.characters[name] = character
        del current_room.characters[name]
        character.current_room = new_room
        # Afficher un message pour signaler le déplacement
        print(f"\n{character.name} s'est déplacé vers {new_room.name}.")


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        
        # Loop until the game is finished
        while self.finished != True:
            self.process_command(input("> "))
            self.move_characters()
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        
        #Affiche rien lorsque le joueur tape "entrer"
        if command_string=='':
            return None

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue dans ce jeu d'aventure ! Votre pseudonyme est {self.player.name} et vous incarnez Luffy dans l'univers de One Piece.  Vous devez d'abord trouver des membres pour constituer votre équipage et lorsque vous serez prêts, vous pourrez partir sur Grand Line pour trouver le One Piece. Attention, une fois sur Grand Line vous ne pourrez pas faire marche arrière ! Bonne chance !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
