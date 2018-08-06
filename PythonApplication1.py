import game_constants 


class Level:
    """ 
    la class game sera la classe mère 
    la class game initialisera les cartes des labyrinthes
    la class game ouvrira les fichiers 

    la class fille irritera de la class mère et de ses propriétés
    la class fille aura comme methode de récupérer la position de MG
    la class fille aura comme methode de modifier la position de MG
    la class fille aura comme méthode de bouger la position de MG (terminal ou grpahique)
    
    """
    def __init__(self, file):
        self.file = file
        self.structure = []
    
    def generate(self):
        with open(self.file) as file:
            lines = file.read().split("\n")
            structure_level=[]        
            for line in lines:
                print(line)
                line_level=[]
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)
                self.structure = structure_level

    def get_position(self, lettre):
        for line in range(len(self.structure[0])):
            for column in range(len(self.structure)):
                if self.structure[column][line] == " ":
                    empty_list = []
                    empty_list.append((line, column))
                    return empty_list
                elif self.structure[column][line] == lettre:
                    MG_list = []
                    MG_list.append((line, column))
                    return MG_list

    
class Perso():
    def __init__(self, structure):
        #self.direction = low
        #self.case_x = 0
        #self.case_y = 0
        self.x = 0
        self.y = 0
        self.structure = structure
             
    def move_position_MG(self, direction, structure):
        if direction == "r":
            if self.x < game_constants.width:
                if self.structure[self.y][self.x+1] != "W":
                    #la nouvelle position de MG
                    self.case_x +=1
                    #l'ancienne position devient un espace
                    self.structure[self.y][self.x] = " "
                    #affecter la nouvelle position de MG dans la carte l espace devient un M
                    self.structure[self.y][self.x+1] = "M"
                else:
                    print("This is a wall !")
        if direction == "le":
            if self.x > 0:
                if self.structure[self.y][self.x-1] != "W":
                    self.case_x -=1
                    #l'ancienne position devient un espace
                    self.structure[self.y][self.x] = " "
                    #affecter la nouvelle position de MG dans la carte l espace devient un M
                    self.structure[self.y][self.x-1] = "M"
                else:
                    print("This is a wall !")
        if direction == "h":
            if self.y > 0:
                if self.structure[self.y-1][self.x] != "W":
                    self.case_y -=1
                    #l'ancienne position devient un espace
                    self.structure[self.y][self.x] = " "
                    #affecter la nouvelle position de MG dans la carte l espace devient un M
                    self.structure[self.y-1][self.x] = "M"
                else:
                    print("This is a wall !")
        if direction == "lo":
            if self.y < game_constants.width:
                if self.structure[self.y+1][self.x] != "W":
                    self.case_y +=1
                    #l'ancienne position devient un espace
                    self.structure[self.y][self.x] = " "
                    #affecter la nouvelle position de MG dans la carte l espace devient un M
                    self.structure[self.y+1][self.x] = "M"
                else:
                    print("This is a wall !")
            

a = Level("labyrinthe.txt")
labyrinthe = a.generate()
print(a.get_position("M"))

b = Perso(a.generate())
#b.move_position_MG("lo", a.generate())

print(b.structure)


