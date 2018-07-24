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
        print("Maze Structures: ", sep=' \n')
        print(new_list)
    return new_list

def position_empty(nested_list):
    empty_list = [] 
    for line in range(15):
        for column in range(15):
            if nested_list[line][column] == " ":
                empty_list.append((line, column))
    print(empty_list)
                

position_liste = maze_nestedlist("labyrinthe.txt")
position_empty(position_liste)