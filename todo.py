"""Une tâche peut être représentée avec une structure de dictionnaire dont les clés suivantes peuvent être :

    N : l’ordre de la tâche dans le fichier.
    X : (la tâche est accomplie ou pas)
    completionDate : la date d’achèvement du tâche.
    creationDate : la date de création du tâche.
    priority : la priorité du tâche (A).
    context : une liste qui contient les contextes auxquels appartient la tâche @python @pc.
    project : une liste qui contient les projets auxquels appartient la tâche +etude +ap1.
    text : la ligne du texte définissant la tâche.
"""
exemple1 = {"N":1, "X":True,"priority":"(A)","completionDate": "2016-05-20","creationDate": "2016-04-30","text": "measure space for","context": ["@chapel"], "project": ["+chapelShelving"],"metadata": {"due":"2016-05-30"}}

"""(A) Remercie maman pour les boulettes de viande @phone
(B) Ramassage de Goodwill Schedule +GarageSale @phone
Postez des affiches dans le quartier +GarageSale"""
exemple2=[{"context": "@phone","priority": "(A)","text":"Remercie maman pour les boulettes de viande"},{"project":"+GarageSale","text":"Ramassage de Goodwill Schedule","priority": "(B)","context": "@phone"},{"project":"+GarageSale","text":"postez desaffiches dans le quatier"}]

"""Une recherche avec le contexte @phone """
exemple3={"text": "Remercie maman pour les boulettes de viande","priority": "(A)","context": "@phone"}


"""
Ces tâches ont des dates de création :

2011-03-02 Document + Format de tâche TodoTxt
(A) 2011-03-02 Appelez maman
"""
exemple5=[{'text': 'Remercie maman pour les boulettes de viande', 'priority': '(A)', 'context': '@phone', 'creationDate': '2011-03-02'}, {'txet': 'Ramassage de Goodwill Schedule +GarageSale', 'priority': '(B)', 'context': '@phone', 'creationDate': '2011-03-02'}, {'text': 'postez desaffiches dans le quatier',"project":"+GarageSale",'creationDate': '2011-03-02'}]

"""Voici une tâche complète :"""
exemple6={"X": True,"completionDate": "2011-03-03","priority": "(B)"}

"""Ces tâches ont des dates de création :

(A) 2011-03-02 Appelez maman
"""

exemple7={"X": False,"creationDate":"2011-03-02","priority": "(A)"}



"""Cette tâche n’a pas de date de création :"""
exemple8={"priority": "(A)","text": "appelez mama","completionDate": "2011-03-02"}

def commence_par_plus(x):
    """une fonction qui renvoie une liste des mots qui commencent par +
    param x(list or tuple): une liste ou tuple
    return (list): une liste contenant les mots qui commencent par(+)
    cu: aucune
    ex
    >>> commence_par_plus(["+s"])
    ['+s']
    """
    j=list()
    for i in x:
        if i[0]=="+":
            j.append(i)
    return j

def commence_par_arobase(x):
    """une fonction qui renvoie une liste des mots qui commencent par @
    param x(list or tuple): une liste ou tuple
    return (list): une liste contenant les mots qui commencent par(@)
    cu: aucune
    ex
    >>> commence_par_arobase(["@s"])
    ['@s']
    """
    j=list()
    for i in x:
        if i[0]=="@":
            j.append(i)
    return j

def les_dates(n,dico):
    """ une fonction qui ajoute des dates dans un dict
    param n:(list ou tuple) une liste ou tuple saise
    param dico : (dict) un dictionaire
    return (list): une liste des dates
    effet de bord: modification de dict
    CU: aucune
    ex
    >>> f=dict()
    >>> les_dates(["2016-04-30"],f)
    ['2016-04-30']
    """
    ll=list()
    for i in n:
        if len(i)==10 and i[0].isdigit() and i[-1].isdigit() and i.count("-")==2:
            ll.append(i)
    if len(ll)==1:
        dico["creationDate"]=ll[0]
    elif len(ll)==2:
        dico["compeletionDate"]=ll[0]
        dico["creationDate"]=ll[1]
    return ll


def parser_tache(tache):
    """ une fonction qui fabrique un dictionaire à partir d'une chaine de caractère, le
    dictionaire est une tache!
    param tache :(str) une chaine de caractère
    return (dict): un dictionaire
    cu:
    une ligne = une tache.
    si il ya une priorité, elle doit etre un lettre maj entre().
    les contexts doivent commencer par @ et les projets par +.
    si la tache est complète, on ecrit true et false sinon.
    si la tache possède une numéro, il doit etre en tout premier de la  chaine.
    si il existe une date, cela veut dire que c'est la date de création, autrement, il faut
    ecrire les deux dates!
    le text, contexts,porjets, peuvent etre n'imorte où dans la chaine.
    
    ex
    >>> parser_tache("x (A) mangé @resto")=={'project': ['@resto'], 'X': True, 'priority': '(A)', 'text': 'mangé'}
    True
    """
    text=list()
    fait=list()
    metdic=dict()
    splittache=tache.split()
    ledic=dict()
    project=commence_par_plus(splittache)
    context=commence_par_arobase(splittache)
    if len(project)!= 0:
        for i in project:
            fait.append(str(i))
    if len(context)!=0:
        for j in context:
            fait.append(str(j))
    if len(project)!=0:
        ledic["project"]=project
    if len(context)!=0:
        ledic["context"]=context
    for i in splittache:
        if i[0]=="(" and i[-1]==")" and len(i)==3:
            ledic["priority"]=i
            fait.append(str(ledic["priority"]))
        if len(i)<=7 and i.isdigit() and splittache.index(i)==0:
            ledic["N"]=i
            fait.append(str(ledic["N"]))
        if i=="x":
            ledic["X"]=True
            fait.append(str(ledic["X"]))
        if i=="X":
            ledic["X"]=False
            fait.append(str(ledic["X"]))
    for i in splittache:
        if ":" in i and "-" in i and i[-1].isdigit() and i[-10].isdigit() and splittache.index(i)==len(splittache)-1:
            met=i
            date=met[-10:]
            metcle=met[:-11]
            metdic[metcle]=date
            ledic["metadata"]=metdic
            fait.append(str(i))
        les_dates(splittache,ledic)
    if len(les_dates(splittache,ledic))!=0:
        for i in les_dates(splittache,ledic):
                fait.append(str(i))
    for i in splittache:
        if i not in fait and i!="x" and i!="X":
            text.append(str(i))
    ledic["text"]=" ".join(text)
    return ledic

def pretty(tache):
    """ une fonction qui imprime une tache siaise d'une façon précise
    param tache:(dict) un dict saisi
    return (none type) : le dict imprimé
    cu: aucune
    ex
    >>> pretty({"priority":"(A)","text": "téléphoné"})
    -----------------------------------
    priority : (A)
    text : téléphoné
    """
    range=list()
    les_cles=list()
    for i in tache:
        les_cles.append(i)
    if "priority" in les_cles:
        range.append(tache["priority"])
    if "completionDate" in les_cles and "creationDate" in les_cles:
        range.append(tache["creationDate"])
        range.append(tache["completionDate"])
    if "creationDate" in les_cles and "completionDate" not in les_cles:
        range.append(tache["creationDate"])
    if "completionDate" in les_cles and "crationDate" not in les_cles:
        range.append(tache["completionDate"])
    if "X" in les_cles:
        range.insert(1,tache["X"])
    for i in les_cles:
        if tache[i] not in range:
            range.append(tache[i])
    print("-"*35)
    for i in range:
        for b in tache:
            if i==tache[b]:
                print(b,":",i)
    
def lire(n):
    """ qui renvoie la liste de toutes les tâches contenues dans un fichier.
    param n:(txt) un fichier
    return (list): une liste de toutes les taches
    cu: aucune
    """
    m=list()
    s=list()
    with open(n,"r") as n2:
        f=n2.readline()
        m.append(f.strip())
        while f!= "":
            f=n2.readline()
            m.append(f.strip())
    return m

def ls(fichier):
    """ imprime toutes les tâches contenues dans fichier.
    param fichier(txt): un fichier txt
    return (None type): les taches imprimées
    cu: aucune
    """
    with open(fichier,"r") as file:
        f=file.readline()
        while f!="":
            f=file.readline()
            pretty(eval(f))

def add(ligne,fichier):
    """ une fonction qui ajoute une ligne dans un fichier
    param linge:(str) une ligne
    param fichier (txt): un fichier
    cu: aucune
    """
    with open(fichier,"a") as file:
        m=file.write(ligne)

def remove(n,fn):
    """ une fonction qui suprime une ligne dans un fichier
    param n (int): un entier, le nombre de la ligne que l'on désire suprimmer
    param fn (txt): le fichier qui contient la ligne qu'on veut supprimmer
    return(None):
    cu: aucune
    """
    with open(fn,"r") as f:
        l=f.read().split("\n")
        del l[n]
    with open(fn,"w") as f:
        f.write("\n".join(l))

def search(valeur,fichier,cle="text"):
    """ imprime le nombre de tâches trouvées, puis imprime les tâches trouvées, la clé par défaut est “text”.
    param valeur(str): une chaine de caractère qui représente une valeur d'une clé de dictionaire
    param fichier(txt): un fichier txt, dans lequel on cherche la valeur
    param cle(txt): une clé de dictionaire, qui est par défaut = text
    cu: aucune
    """
    j=0
    m=list()
    with open(fichier,"r") as f:
        l=f.read().split("\n")
        for i in l:
            s=eval(i)
            for i in s:
                if i==cle and s[cle] == valeur:
                    j+=1
                    m.append(s)
                    pretty(s)
                    print(" \n C'est la tache numéro: ",j,"\n")
                    
                    

def s(n):
    fait=list()
    range=list()
    ff=list()
    for key,value in n.items():
        ff.append(n[key])
    if "priority" in n:
        range.insert(0,n["priority"])
        fait.append(n["priority"])
    if "creationDate" in n and "completionDate" in n and "priority" in n:
        range.insert(1,n["completionDate"])
        range.insert(2,n["creationDate"])
        fait.append(n["completionDate"])
        fait.append(n["creationDate"])
    if "X" in n and "priority" in n:
        if n["X"] == True:
            range.insert(1,"x")
            fait.append(n["X"])
        elif n["X"] == False:
            range.insert(1,"X")
            fait.append(n["X"])
    if "project" in n:
        range.append(" ".join(n["project"]))
        fait.append(n["project"])
    if "context" in n:
        range.append(" ".join(n["context"]))
        fait.append(n["context"])
    if "metadata" in n:
        l=n["metadata"]
        d=""
        for k,v in l.items():
            d=k+v
        range.append(d)
        fait.append(n["metadata"])
    for i in ff:
        if i not in fait:
            range.append(i)
    return " ".join(range)


if __name__ == "__main__":
    import doctest
    doctest.testmod()