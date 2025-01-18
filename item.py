
class Item : 
    def __init__(self, name, description,weight): 
        self.name = name
        self.description = description
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} : {self.description} "  f"({self.weight} kg)"
    



