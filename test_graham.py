import unittest
from graham import graham


class TestGrahamAlgorithm(unittest.TestCase):

    def test_pusta_lista(self):
        with self.assertRaises(ValueError):
            graham([])

    def test_jeden_punkt(self):
        self.assertEqual(graham([(0, 0)]), [(0, 0)])

    def test_dwa_punkty(self):
        self.assertEqual(graham([(0, 0), (1, 1)]), [(0, 0), (1, 1)])

    def test_punkty_na_jednej_prostej(self):
        self.assertEqual(graham([(0, 0), (1, 1), (2, 2)]), [(0, 0), (2, 2)])

    def test_punkty_zidentycznymi_wspolrzednymi(self):
        self.assertEqual(graham([(1, 1), (1, 1), (1, 1)]), [(1, 1)])

    def test_punkty_w_roznch_czesciach_plaszczyzny(self):
        punkty = [(0, 0), (1, 1), (-1, -1), (2, 3), (-2, -3)]
        self.assertEqual(graham(punkty), [(-2, -3), (1, 1), (2, 3), (-1, -1)])
        
    def test_duzo_punktow(self):
        punkty = [(10, -3), (-7, 4), (-4, 2), (8, -2), (-9, -6), (-2, 2), (7, 9), (1, 9), (4, -2), (-1, 0), (6, -9), (-8, 6), (-6, -2), (-4, 9), (0, 10), (-4, -7), (4, 7), (-1, -1), (3, -8), (-5, -7)]
        self.assertEqual(graham(punkty), [(6, -9), (10, -3), (7, 9), (0, 10), (-4, 9), (-8, 6), (-9, -6), (-5, -7)])

    def test_punkty_o_duzych_wspolrzednych(self):
        punkty = [(1000000, 1000000), (2000000, 0), (3000000, 3000000)]
        self.assertEqual(graham(punkty), [(2000000, 0), (3000000, 3000000), (1000000, 1000000)])

    def test_nieprawidlowe_typy_danych(self):
        with self.assertRaises(ValueError):
            graham([(1, 2), "string", (3, 4)])

    def test_bledny_typ_danych(self):
        with self.assertRaises(ValueError):
            graham("string")

if __name__ == "__main__":
    unittest.main()

