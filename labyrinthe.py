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

def get_position(nested_list, lettre):
    empty_list = []
    MG_list = []    
    for line in range(len(nested_list)):
        for column in range(len(nested_list)):
            if nested_list[line][column] == " ":
                empty_list.append((line, column))
                return empty_list
            elif nested_list[line][column] == lettre:
                MG_list.append((line, column))
                return MG_list


def move_position_MG(position_empty_maze):
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
    global position_MG
    file = "labyrinthe.txt"
    Continue = True
    choix = ''
    maze = maze_nestedlist(file)
    
    position_MG = get_position(maze, "M")
    print("Current position: {0}".format(position_MG))
    
    while Continue:
        choix = input("entrer une lettre ")
        if choix.lower() in {'h', 'd', 'b','g'}:                   
            set_position_MG(choix, position_MG)
        else:
            break

if __name__ == '__main__':
    main()
    
