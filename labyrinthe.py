def maze_nestedlist(file):
    with open(file) as readfile:
        lines = readfile.read().split("\n") #retourne une liste dans lines
        print("Maze : ", sep=' \n')
        new_list=[]
        for line in lines:
            print(line, sep=' \n')
            sub_list=[]
            for l in line:
                sub_list.append(l)
            new_list.append(sub_list)
    return new_list

def get_position(nested_list):
    empty_list = []    
    for line in range(len(nested_list)):
        for column in range(len(nested_list)):
            if nested_list[line][column] == " ":
                empty_list.append((line, column))
    return empty_list

def get_position_MG(nested_list):
    MG_list = []
    for line in range(len(nested_list)):
        for column in range(len(nested_list)):
            if nested_list[line][column] == "M":
                    MG_list.append((line, column))
    return MG_list 

def move_position_MG():
    pass

def set_position_MG(choice, position):
    y,x  = position[0]
    if choice.lower() == "b":
        x,y = x, y+1
    if choice.lower() == "h":
        x,y = x, y-1
    if choice.lower() == "g":
        x,y = x-1, y
    if choice.lower() == "d":
        x,y = x+1, y
    position_mcgyver = (x,y)
    print("la nouvelle position est : {0}".format(position_mcgyver))
    
def main():
    global position_mcgyver
    file = "labyrinthe.txt"
    Continuer = True
    choix = ''
    print("Opening {0}".format(file))
    while Continuer != False:
        choix  = input("entrer une lettre ")
        if choix.lower() not in {'q', ''}:
            maze = maze_nestedlist(file)
            pos = get_position_MG(maze)        
            print(set_position_MG(choix, pos))
        else:
            break

if __name__ == '__main__':
    main()
    
