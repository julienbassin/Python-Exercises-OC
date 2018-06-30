

def exercice_1():
    # Créer un fichier texte (carte.txt) contenant la variable text
    text = "WWWW-----W\nW-------WW\nWWW-M--WWW\nWWWWWW--WW"
    try:
        file = open("carte.txt", "w")
        file.writelines(text)
    except ValueError:
        print("Impossible d'ouvrir le fichier !")
    finally:
        file.close()


def exercice_2():

    # Afficher en console le fichier texte créé à l'exercice 1
    try:
        with open("carte.txt", 'r') as readfile:
            for lines in readfile.readlines():
                print(lines)
    except ValueError:
        print("Impossible d'ouvrir le fichier !")
    pass


def exercice_3(lettre):
    # Vérifier si la lettre entrée en paramètre est présente
    # dans le fichier créé à l'exercice 1 (retourner True si
    # la lettre est présente et False sinon)
    try:
        with open("carte.txt", 'r') as f:
            lines = f.read().split("\n")
            for line in lines:
                if lettre in line:
                    return True
            return False

    except ValueError:
        print("Impossible d'ouvrir le fichier !")
    pass


def exercice_4(lettre):
    # Trouver la position de la lettre passée en paramètre dans
    # le fichier créé à l'exercice 1. Si lettre == "M", la fonction
    # doit renvoyer le tuple (4, 2) car le lettre "M" est dans la colonne
    # 4 (numérotation à partir de 0) et la ligne 2 dans la variable text de
    # l'exercice 1.
    try:
        with open("carte.txt", 'r') as f:
            lines = f.read().split("\n")
            for l in range(len(lines)):
                text = lines[l].find(lettre)
                if text != -1:
                    break
        f.close()
        if text != -1:
            return [text, l]
        else:
            return -1
    except ValueError:
        print("Impossible d'ouvrir le fichier !")
    finally:
        f.close()


def exercice_5():
    # Créer un dictionnaire contenant toutes les lettres présentes
    # dans le fichier texte de l'exercice avec leur nombre d'apparition
    # dans le fichier : {"W": 22, "M": 1}
    # Ouvrir le fichier 
    # checker toutes les lettres et compter le nombre d'apparition (voir exercise python 3 livre)
    # Ajouter au dictionnaire la lettre (key) et le nbre de fois que la lettre apparait
    MyDict = {}
    LettreW = "W"
    LettreTiret = "-"
    LettreM = "M"
    try:
        with open("carte.txt", 'r') as f:
            lines = f.read().split("\n")
            for line in lines:
                for c in line:
                    print (c)

                MyDict[line] = l
    except ValueError:
        print("Impossible d'ouvrir le fichier !")
    finally:
        f.close()

    pass

def exercice_6():
    # Tranformer le fichier texte de l'exercice 1 en fichier JSON
    pass

def exercice_7():
    # Demander si le joueur veut continuer le jeu (avec input). Si la
    # réponse est "oui" ou "o", on repose la même question. Si la réponse
    # est "non" ou "n", la boucle s'arrête. Si une autre réponse est donnée,
    # afficher "Réponse non correcte" puis reposer la question.
    Question = "Voulez-vous continuer ?\n"
    Response = "Bresil"
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}
    while True:
        choice = eval(input("Voulez-vous continuer ?\n").lower())
        if choice in yes:
            eval(input("Voulez-vous continuer ?\n").lower())
        elif choice in no:
            break
        else:
            print("Réponse non correcte")
            eval(input("Voulez-vous continuer ?\n").lower())

if __name__ == "__main__":    
    #exercice_1()
    #exercice_2()
    #print(exercice_3("M"))
    #print(exercice_4("M"))
    #exercice_5()
    #exercice_6()
    exercice_7()
