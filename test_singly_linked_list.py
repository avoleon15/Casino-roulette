import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    # Verifica que al insertar varios nodos, tail.next siga apuntando a head
    def test_insertar_multiples_nodos_mantiene_circular(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(7, "red")
        lista.insertar_apuesta(12, "black")
        self.assertIs(lista.tail.next, lista.head)

    # Verifica que size aumente con cada inserción
    def test_insertar_incrementa_size(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(5, "red")
        lista.insertar_apuesta(10, "black")
        self.assertEqual(lista.size, 2)

    # Verifica que ver_apuestas retorne todos los elementos insertados
    def test_ver_apuestas_devuelve_todos(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(7, "red")
        lista.insertar_apuesta(0, "green")
        self.assertEqual(len(lista.ver_apuestas()), 2)

    # Verifica que eliminar en lista vacía retorne False
    def test_eliminar_lista_vacia_retorna_false(self):
        lista = SinglyLinkedList()
        self.assertFalse(lista.eliminar_apuesta(5))

    # Verifica que al eliminar el head, el nuevo head sea el siguiente nodo
    def test_eliminar_head_actualiza_head(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(7, "red")
        lista.insertar_apuesta(12, "black")
        lista.eliminar_apuesta(7)
        self.assertEqual(lista.head.number, 12)

    # Verifica que eliminar un número inexistente retorne False
    def test_eliminar_numero_inexistente_retorna_false(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(7, "red")
        self.assertFalse(lista.eliminar_apuesta(99))

    # Verifica que verificar_ganador detecte una apuesta ganadora por número
    def test_verificar_ganador_por_numero(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(7, "red")
        ganadores = lista.verificar_ganador(7, "red")
        self.assertTrue(ganadores[0]["gana_por_numero"])

    # Verifica que verificar_ganador detecte una apuesta ganadora por color
    def test_verificar_ganador_por_color(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(3, "red")
        ganadores = lista.verificar_ganador(7, "red")
        self.assertTrue(ganadores[0]["gana_por_color"])

    # Verifica que verificar_ganador retorne vacío si ninguna apuesta gana
    def test_verificar_ganador_ninguna_gana(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(3, "black")
        self.assertEqual(lista.verificar_ganador(0, "green"), [])

    # Verifica que las apuestas se guarden en el orden en que se insertaron
    def test_ver_apuestas_orden_correcto(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(3, "red")
        lista.insertar_apuesta(15, "black")
        apuestas = lista.ver_apuestas()
        self.assertEqual(apuestas[0]["number"], 3)
        self.assertEqual(apuestas[1]["number"], 15)


if __name__ == "__main__":
    unittest.main()
