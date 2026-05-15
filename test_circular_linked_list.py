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

    # Verifica que construir_ruleta establezca current apuntando a head
    def test_construir_ruleta_current_es_head(self):
        ruleta = CircularLinkedList()
        ruleta.construir_ruleta()
        self.assertIs(ruleta.current, ruleta.head)

    # Verifica que girar cambie la posición de current
    def test_girar_mueve_current(self):
        ruleta = CircularLinkedList()
        ruleta.construir_ruleta()
        current_antes = ruleta.current
        ruleta.girar()
        self.assertIsNot(ruleta.current, current_antes)

    # Verifica que la ruleta empiece vacía antes de construir
    def test_ruleta_empieza_vacia(self):
        ruleta = CircularLinkedList()
        self.assertIsNone(ruleta.head)
        self.assertEqual(ruleta.size, 0)

    # Verifica que insertar un solo nodo lo haga apuntarse a sí mismo
    def test_insertar_unico_nodo_circular(self):
        ruleta = CircularLinkedList()
        ruleta.insertar_numero(5)
        self.assertIs(ruleta.tall.next, ruleta.head)

    # Verifica que girar sin construir la ruleta lance RuntimeError
    def test_girar_sin_construir_lanza_error(self):
        ruleta = CircularLinkedList()
        with self.assertRaises(RuntimeError):
            ruleta.girar()

    # Verifica que el head de la ruleta construida sea el número 0
    def test_construir_ruleta_head_es_cero(self):
        ruleta = CircularLinkedList()
        ruleta.construir_ruleta()
        self.assertEqual(ruleta.head.number, 0)

    # Verifica que girar múltiples veces siempre retorne un número entre 0 y 36
    def test_girar_multiples_veces_siempre_valido(self):
        ruleta = CircularLinkedList()
        ruleta.construir_ruleta()
        for _ in range(10):
            self.assertIn(ruleta.girar(), range(37))


if __name__ == "__main__":
    unittest.main()
