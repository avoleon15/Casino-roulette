import unittest
from circular_linked_list import CircularLinkedList


class TestCircularLinkedList(unittest.TestCase):

    # Verifica que construir_ruleta inserte los 37 números (0 al 36)
    def test_construir_ruleta_size_correcto(self):
        ruleta = CircularLinkedList()
        ruleta.construir_ruleta()
        self.assertEqual(ruleta.size, 37)

    # Verifica que girar retorne un número válido entre 0 y 36
    def test_girar_retorna_numero_valido(self):
        ruleta = CircularLinkedList()
        ruleta.construir_ruleta()
        resultado = ruleta.girar()
        self.assertIn(resultado, range(37))

    # Verifica que al insertar un nodo, tall.next apunte a head (circularidad)
    def test_insertar_numero_mantiene_circular(self):
        ruleta = CircularLinkedList()
        ruleta.insertar_numero(0)
        ruleta.insertar_numero(1)
        self.assertIs(ruleta.tall.next, ruleta.head)


if __name__ == "__main__":
    unittest.main()
