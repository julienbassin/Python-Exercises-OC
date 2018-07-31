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
        print(new_list)
    return new_list

def get_position(nested_list):
    empty_list = []    
    for line in range(len(nested_list)):
        for column in range(len(nested_list)):
            if nested_list[line][column] == " ":
                empty_list.append((line, column))
    return empty_list

def get_position_mcgyver(nested_list):
    MG_list = []
    for line in range(len(nested_list)):
        for column in range(len(nested_list)):
            if nested_list[line][column] == "M":
                    MG_list.append((line, column))
    return MG_list 

def set_position_mcgyver(choice, position):
    y,x  = position[0]
    if choice.lower() == "b":
        print("incrementation de y ")
        x,y = x, y+1
    if choice.lower() == "h":
        print("incrementation de y ")
        x,y = x, y-1
    if choice.lower() == "g":
        print("incrementation de x ")
        x,y = x-1, y
    elif choice.lower() == "d":
        print("incrementation de x ")
        x,y = x+1, y
    return (x,y)
    
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
            print(get_position(maze))
            pos = get_position_mcgyver(maze)        
            print(set_position_mcgyver(choix, pos))
        else:
            break

if __name__ == '__main__':
    main()
    
