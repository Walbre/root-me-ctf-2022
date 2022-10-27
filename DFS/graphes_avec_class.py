

class graphs:

    def __init__(self, sommets:list=[]):
        self.ordre = len(sommets)

        self.sommets = sommets
        self.liasons = {}
        for sommet in sommets:
            self.liasons[sommet] = []

    def ajouterSommet(self, nom:str):
        self.ordre += 1
        self.sommets.append(nom)
        self.liasons[nom] = []

    def enleverSommet(self, nom):
        self.ordre -= 1
        self.sommets.pop(self.sommets.index(nom))
        self.liasons.pop(nom)

        for key, value in self.liasons.items():
            trouve = False
            for elemment in value:
                if elemment == nom:
                    trouve = True

            if trouve:
                self.liasons[key].pop(self.liasons[key].index(nom))

    def est_dans_sommets(self, nom):
        for elemment in self.sommets:
            if elemment == nom:
                return True
        return False

    def ajouterArete(self, nom1, nom2):

        if not self.est_dans_sommets(nom1):
            raise ValueError("{} n'est pas dans le graph".format(nom1))

        if not self.est_dans_sommets(nom2):
            raise ValueError("{} n'est pas dans le graph".format(nom2))

        deja_lie = False
        for elemment in self.liasons[nom1]:
            if deja_lie is False and elemment == nom2:
                deja_lie = True

        if deja_lie:
            raise ValueError("{} est deja lié à {}".format(nom1, nom2))

        self.liasons[nom1].append(nom2)


    def supprimerArete(self, nom1, nom2):
        if not self.est_dans_sommets(nom1):
            raise ValueError("{} n'est pas dans le graph".format(nom1))

        if not self.est_dans_sommets(nom2):
            raise ValueError("{} n'est pas dans le graph".format(nom2))

        lie = False
        for elemment in self.liasons[nom1]:
            if lie is False and elemment == nom2:
                lie = True
        if lie:
            self.liasons[nom1].pop(self.liasons[nom1].index(nom2))
        else:
            raise ValueError("{} n'est pas lie à {}".format(nom1, nom2))

    def ordre(self):
        return self.ordre

    def __str__(self):

        renvoyer = ""
        for element in self.sommets:
            p = element + " -> "
            for element2 in self.liasons[element]:
                p = p + element2 + " | "
            if p.endswith(" | "):
                p = p[:-3]
            renvoyer += p + "\n"
        return renvoyer


    def liste_voisins(self, s, deja_visite):
        endroit = None
        for i in range(len(self.sommets)):
            if s == self.sommets[i]:
                endroit = i

        if endroit is None:
            raise ValueError("{} n'est pas dans le graphe".format(s))

        voisins = []
        for sommet in self.liasons[s]:
            if not sommet in deja_visite:
                voisins.append(sommet)

        return voisins



    def existeChemin(self, a, b):


        if a == b:
            return [1]

        if not self.est_dans_sommets(a):
            raise ValueError("{} n'appartient pas au graphe'").format(a)

        if not self.est_dans_sommets(b):
            raise ValueError("{} n'appartient pas au graphe'").format(b)

        chemin = [a]

        deja_visite = [a]

        test = 0
        while chemin != []:
            test += 1
            if chemin[-1] == b:
                return chemin

            voisins = self.liste_voisins(chemin[-1], deja_visite)
            if voisins != []:
                chemin.append(voisins[0])
                deja_visite.append(voisins[0])
            else:
                chemin.pop()
        return chemin






if __name__ == '__main__':
    g = graphs(["A", "B"])
    print(g.sommets, g.liasons)

    g.ajouterSommet("C")
    print(g.sommets, g.liasons)

    g.enleverSommet("C")
    print(g.sommets, g.liasons)

    g.ajouterSommet("C")
    g.ajouterArete("A", "B")
    g.ajouterArete("A", "C")
    print(g.sommets, g.liasons)

    #g.supprimerArete("A", "B")
    print(g.sommets, g.liasons)
    print(g)


    k = graphs(["A", "B", "C"])
    k.ajouterArete("B", "A")
    k.ajouterArete("C", "A")
    k.enleverSommet("A")
    print(k.sommets, k.liasons)

    q = graphs(["A", "B", "C", "D"])
    q.ajouterArete("A", "B")
    q.ajouterArete("B", "C")
    print(q.existeChemin("A", "C"))