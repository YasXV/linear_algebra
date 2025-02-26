from Vecteur import Vecteur
from typing import Optional, List

class Matrice(): 
    def __init__(self, monvecteur: List[List[float]]) -> "Matrice": 
        """
        Initialisation de la classe Matrice
        
        Args:
            monvecteur (list): liste de listes représentant la matrice

        Returns:
            None

        Raises:
            ValueError: Si les dimensions de la matrice ne sont pas spécifiées et que la liste de listes n'est pas donnée
        """
        if monvecteur is not None:
            self.matrice = Vecteur([Vecteur(ligne) for ligne in monvecteur])
            self.n = len(monvecteur)
            self.m = len(monvecteur[0])
            self.composants = monvecteur
        else:
            raise ValueError("Vous devez donner une liste de liste représentant la matrice")
        

    def __str__(self):
        return(str(self.matrice))
    
    def __eq__(self, autreMatrice):
        epsilon = 10e-6
        if(isinstance(autreMatrice, Matrice)):
            if(self.dimension() != autreMatrice.dimension()):
                return False
            else:
                return all([self.ligne(i)==autreMatrice.ligne(i) for i in range(self.dimension()[0])])
            
    def __ne__(self, autreMatrice):
        return not (self == autreMatrice)
        
    def ligne(self,i):
        return Vecteur(self[i])
    
    def colonne(self,j):
        return Vecteur(self[:,j])
    
    def dimension(self):
        return (self.n, self.m)
    
    def __getitem__(self, indices):
        if isinstance(indices, tuple):
            i,j = indices
            if isinstance(i, slice) :
                return [self.composants[k][j] for k in range(self.dimension()[0])] 
            elif isinstance(j, slice):
                return [self.composants[i][k] for k in range(self.dimension()[1])]
            else:
                return self.composants[i][j]
        else:
            return self.composants[indices]
    
    
    def __add__(self, autreMatrice):
        if not isinstance(autreMatrice, Matrice):
            raise ValueError("Addition entre matrices seulement")
        if self.dimension() != autreMatrice.dimension():
            raise ValueError("Les deux matrices n'ont pas la même dimension")
        else:
            return Matrice(monvecteur=[[lc1+lc2 for lc1,lc2 in zip(ligne1,ligne2)] for ligne1, ligne2 in zip(self.composants, autreMatrice.composants)])
        
    
    def __mul__(self, num):
        return Matrice(monvecteur=[[num*elt for elt in ligne] for ligne in self.composants])
    
    def __rmul__(self, num):
        return self.__mul__(num)
    
    def __call__(self, unvecteur: Vecteur) -> "Matrice":
        """
        Multiplie la matrice par un vecteur.
        
        Args:
            unvecteur (Vecteur.Vecteur): Un vecteur de même taille que le nombre de colonnes de la matrice.
        
        Returns:
            Matrice: Le vecteur résultant.
        """
        if not isinstance(unvecteur, Vecteur):
            raise ValueError("Multiplication matrice-vecteur seulement")

        if self.dimension()[1] != len(unvecteur):
            raise ValueError("Le vecteur n'a pas la même dimension que le nombre de colonnes de la matrice")
        else:
            return Vecteur([self.ligne(i)@unvecteur for i in range(self.dimension()[0])])
        
    def est_diagonale(self):
        return all([self[i][j]==0 for i in range(self.dimension()[0]) for j in range(self.dimension()[1]) if i!=j])

    
def multiplier_matrice(matrice1, matrice2):
        if not isinstance(matrice1, Matrice) or not isinstance(matrice2, Matrice):
            raise ValueError("Produit matriciel entre matrices seulement")
        if (matrice1.dimension()[1] != matrice2.dimension()[0]):
            raise ValueError("Les deux matrices n'ont pas la même dimension")
        else:
            return Matrice(monvecteur=[[sum([matrice1[i][k]*matrice2[k][j] for k in range(matrice1.dimension()[1])]) for j in range(matrice2.dimension()[1])] for i in range(matrice1.dimension()[0])])

        
        
        






if __name__== "__main__":
    print("HELLLLO")
    m1 = Matrice(monvecteur=[[1,2],[3,4]])
    monvecteur=[[1,2,3],[4,5,6],[7,8,9]]
    print(monvecteur[:][1])
    m2 = Matrice(monvecteur=[[1,6],[7,8]])
    print(m1+m2)
    print(m1[:,1])
    print(3*m2)
    print(m1.colonne(1))
    print(m1.ligne(1))
    print(multiplier_matrice(m1,m2))
    print(m1(Vecteur([1,2])))
    print(m1==m1)
    print(m1==m2)
