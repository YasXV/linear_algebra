import unittest
from matrice import *
from Vecteur import Vecteur 

class TestMatrice(unittest.TestCase):
    def test_addition(self):
        m1 = Matrice([[1, 2], [3, 4]])
        m2 = Matrice([[5, 6], [7, 8]])
        result = m1+m2
        expected = Matrice([[6, 8], [10, 12]])
        self.assertEqual(result, expected)

    def test_multiplication_deux_matrices(self):
        m1 = Matrice([[1, 2], [3, 4]])
        m2 = Matrice([[5, 6], [7, 8]])
        result = multiplier_matrice(m1, m2)
        expected = Matrice([[19, 22], [43, 50]])
        self.assertEqual(result, expected)

    def test_matrice_vecteur(self):
        m1 = Matrice([[1, 2], [3, 4]])
        v1 = Vecteur([1, 2])
        result = m1(v1)
        expected = Vecteur([5, 11])
        self.assertEqual(result, expected)

    def test_indexation_matrice(self):
        m1 = Matrice([[1, 2], [3, 4]])
        result = m1[1][0]
        expected = 3
        self.assertEqual(result, expected)

    def test_indexation_slice_matrice_colone(self):
        m1 = Matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = m1 [:, 2]
        expected = [3, 6, 9]
        self.assertEqual(result, expected)

    def test_indexation_slice_matrice_ligne(self):
        m1 = Matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = m1 [2, :]
        expected = [7, 8, 9]
        self.assertEqual(result, expected)

    def test_extraction_ligne(self):
        m1 = Matrice([[9, -2], [-3, 1]])
        result = m1.ligne(1)
        expected = Vecteur([-3, 1])
        self.assertEqual(result, expected)

    def test_extraction_colonne(self):
        m1 = Matrice([[9, -2, 5, 8, -2], [-3, 1, 9, 7, 3]])
        result = m1.colonne(3)
        expected = Vecteur([8, 7])
        self.assertEqual(result, expected)

    def test_comparaison_matrice(self):
        m1 = Matrice([[-1, 2], [3, 4]])
        m2 = Matrice([[1, 2], [3, 4]])
        result = m1==m2
        expected = False
        self.assertEqual(result, expected)

    def test_matrice_non_egales(self):
        m1 = Matrice([[1, 2], [3, 4]])
        m2 = Matrice([[1, 2], [3, 4]])
        result = m1!=m2
        expected = False
        self.assertEqual(result, expected)

    def test_matrice_diagonale(self):
        m1 = Matrice([[1, 0], [0, 4]])
        m2 = Matrice([[1, 2], [3, 4]])
        result1 = m1.est_diagonale()
        result2 = m2.est_diagonale()
        expected1 = True
        expected2 = False
        self.assertEqual(result1, expected1) and self.assertEqual(result2, expected2)


class TestVecteur(unittest.TestCase):
    def test_addition(self):
        v1 = Vecteur([1, 2, 3])
        v2 = Vecteur([4, 5, 6])
        result = v1+v2
        expected = Vecteur([5, 7, 9])
        self.assertEqual(result, expected)

    def test_produit_scalaire(self):
        v1 = Vecteur([1, -2, 3])
        v2 = Vecteur([4, 23, 1])
        result = v1@v2
        expected = -39
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()