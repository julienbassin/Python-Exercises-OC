import json

def exercice_1():
    # Créer un fichier texte (carte.txt) contenant la variable text
    text = "WWWW-----W\nW-------WW\nWWW-M--WWW\nWWWWWW--WW"
    with open("carte.txt", "w") as file:
        file.writelines(text)


def exercice_2():

    # Afficher en console le fichier texte créé à l'exercice 1
    with open("carte.txt", 'r') as readfile:
        for lines in readfile.readlines():
            print(lines)

def exercice_3(lettre):
    # Vérifier si la lettre entrée en paramètre est présente
    # dans le fichier créé à l'exercice 1 (retourner True si
    # la lettre est présente et False sinon)
    with open("carte.txt", 'r') as f:
        lines = f.read().split("\n")
        for line in lines:
            if lettre in line:
                return True
        return False

def exercice_4(lettre):
    # Trouver la position de la lettre passée en paramètre dans
    # le fichier créé à l'exercice 1. Si lettre == "M", la fonction
    # doit renvoyer le tuple (4, 2) car le lettre "M" est dans la colonne
    # 4 (numérotation à partir de 0) et la ligne 2 dans la variable text de
    # l'exercice 1.
    with open("carte.txt", 'r') as file:
        lines = file.read().split("\n")
        for index, item in enumerate(lines):
            if item.find(lettre) is not -1: 
                return item.index(lettre), index



def exercice_5():
    # Créer un dictionnaire contenant toutes les lettres présentes
    # dans le fichier texte de l'exercice avec leur nombre d'apparition
    # dans le fichier : {"W": 22, "M": 1}
    # Ouvrir le fichier 
    # checker toutes les lettres et compter le nombre d'apparition (voir exercise python 3 livre)
    # Ajouter au dictionnaire la lettre (key) et le nbre de fois que la lettre apparait
    Mydict = {}
    with open("carte.txt", 'r') as file:
        lines = file.read().split("\n")
        for line in lines:
            for car in line:
                #si ton car est dans ton dictionnaire tu incrementes l'indice de ton car + 1 sinon c'est egal à 1
                Mydict[car] = line.count(car)
            print(Mydict)

def exercice_6():
    # Tranformer le fichier texte de l'exercice 1 en fichier JSON
    json_data = json.dumps({"a":True, "b":2})
    print(json_data)

def fonction_liste(*parametres, sep= '', fin="\n"):
    
    parametres = list(parametres)
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    chaine = sep.join(parametres)
    chaine +=fin
    print(chaine, end='')


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

def displayASCII():
    i = 0
    while i <= 969:
        print("La lettre actuelle: ", chr(i))
        i+=1

def displayAccent():
    i = 128
    for i in range(i, 256):
        print("la lettre actuelle: ", chr(i))

def maj_min():
    i = 65
    majus, minusc = "", ""
    for i in range(i, 122):
        if i > 65 and i < 90:
            i += 32
            print("la lettre en minuscule: ", chr(i))
        elif i > 97 and i < 122:
            i -= 32
            print("la lettre en majuscule: ", chr(i))

def debut_et_fin(lst):
    debut = lst[0]
    fin = lst[-1]

    return debut,fin

if __name__ == "__main__":    
    #maj_min()
    deb , fin = debut_et_fin([1,3,4,5])
    print(deb)
    print(fin)
