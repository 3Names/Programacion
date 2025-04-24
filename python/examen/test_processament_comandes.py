import unittest
import os
from processament_comandes import Producte, Client, Comanda, processar_comandes

class TestProcessamentComandes(unittest.TestCase):

    def setUp(self):
        # Crear fitxers de prova
        with open("test_productes.txt", "w") as f:
            f.write("ProducteA,10.00\n")
            f.write("ProducteB,5.00\n")
        with open("test_clients.txt", "w") as f:
            f.write("1,ClientX,clientx@exemple.com\n")
            f.write("2,ClientY,clienty@exemple.com\n")
        with open("test_comandes.txt", "w") as f:
            f.write("1,1,ProducteA:2,ProducteB:1\n")
            f.write("2,2,ProducteB:3\n")

    def tearDown(self):
        # Eliminar fitxers de prova
        for filename in ["test_productes.txt", "test_clients.txt", "test_comandes.txt"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_classe_producte(self):
        producte = Producte("TestProducte", 19.99)
        self.assertEqual(producte.nom, "TestProducte")
        self.assertEqual(producte.preu, 19.99)

    def test_classe_client(self):
        client = Client(99, "TestClient", "test@exemple.com")
        self.assertEqual(client.id_client, 99)
        self.assertEqual(client.nom, "TestClient")
        self.assertEqual(client.email, "test@exemple.com")

    def test_classe_comanda_calcular_total(self):
        producte1 = Producte("Prod1", 10.00)
        producte2 = Producte("Prod2", 5.00)
        client = Client(1, "Client", "client@exemple.com")
        comanda = Comanda(1, client, [producte1, producte2], [2, 3])
        self.assertEqual(comanda.calcular_total(), 35.00)

    def test_processar_comandes_basic(self):
        resultats = processar_comandes("test_productes.txt", "test_clients.txt", "test_comandes.txt")
        self.assertEqual(len(resultats), 2)
        self.assertEqual(resultats[0]['id_comanda'], 1)
        self.assertEqual(resultats[0]['nom_client'], 'ClientX')
        self.assertAlmostEqual(resultats[0]['total'], 25.00)
        self.assertEqual(resultats[1]['id_comanda'], 2)
        self.assertEqual(resultats[1]['nom_client'], 'ClientY')
        self.assertAlmostEqual(resultats[1]['total'], 15.00)

if __name__ == '__main__':
    unittest.main()
