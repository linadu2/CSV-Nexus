import unittest
import os
from V1.main import load_csv, write_csv, merge_csv, equality_check, sort_data

class TestCSVNexus(unittest.TestCase):

    def setUp(self):
        """Prépare les fichiers CSV de test avant chaque test."""
        self.file1 = "test1.csv"
        self.file2 = "test2.csv"
        self.output_file = "../output.csv"

        with open(self.file1, "w", encoding='utf-8') as f1:
            f1.write("nom,quantité,prix,categorie\n")
            f1.write("ProduitA,10,5.5,Cat1\n")
            f1.write("ProduitB,20,10.0,Cat2\n")

        with open(self.file2, "w", encoding='utf-8') as f2:
            f2.write("nom,quantité,prix,categorie\n")
            f2.write("ProduitC,15,7.0,Cat1\n")
            f2.write("ProduitD,30,12.5,Cat3\n")

    def tearDown(self):
        """Supprime les fichiers CSV de test après chaque test."""
        if os.path.exists(self.file1):
            os.remove(self.file1)
        if os.path.exists(self.file2):
            os.remove(self.file2)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_load_csv(self):
        """Test du chargement d'un fichier CSV."""
        header, data = load_csv(self.file1)
        self.assertEqual(header, ["nom", "quantité", "prix", "categorie", "département"])
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], ["ProduitA", 10.0, 5.5, "Cat1", "test1"])

    def test_write_csv(self):
        """Test de l'écriture d'un fichier CSV."""
        header = ["nom", "quantité", "prix", "categorie", "département"]
        data = [
            ["ProduitA", 10.0, 5.5, "Cat1", "test1"],
            ["ProduitB", 20.0, 10.0, "Cat2", "test1"]
        ]
        write_csv(self.output_file, data, header, force_overwrite=True)
        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, "r", encoding='utf-8') as f:
            content = f.readlines()
        self.assertEqual(len(content), 3)  # header + 2 rows
        self.assertIn("nom,quantité,prix,categorie,département\n", content)

    def test_merge_csv(self):
        """Test de la fusion de deux fichiers CSV."""
        header = None
        data = []
        header, data = merge_csv([self.file1, self.file2], data, header)
        self.assertEqual(len(data), 4)
        self.assertEqual(data[2], ["ProduitC", 15.0, 7.0, "Cat1", "test2"])
        self.assertEqual(header, ["nom", "quantité", "prix", "categorie", "département"])

    def test_equality_check(self):
        """Test de la vérification de l'égalité des en-têtes."""
        header1 = ["nom", "quantité", "prix", "categorie"]
        header2 = ["nom", "quantité", "prix", "categorie"]
        header3 = ["nom", "quantité", "prix"]
        self.assertTrue(equality_check(header1, header2))
        self.assertFalse(equality_check(header1, header3))

    def test_sort_data(self):
        """Test du tri des données."""
        header = ["nom", "quantité", "prix", "categorie", "département"]
        data = [
            ["ProduitA", 10.0, 5.5, "Cat1", "test1"],
            ["ProduitB", 20.0, 10.0, "Cat2", "test1"],
            ["ProduitC", 15.0, 7.0, "Cat1", "test2"]
        ]
        sorted_data = sort_data(data, header, "prix")
        self.assertEqual(sorted_data[0], ["ProduitA", 10.0, 5.5, "Cat1", "test1"])
        self.assertEqual(sorted_data[-1], ["ProduitB", 20.0, 10.0, "Cat2", "test1"])

        with self.assertRaises(ValueError):
            sort_data(data, header, "non_existent_column")

if __name__ == "__main__":
    unittest.main()

