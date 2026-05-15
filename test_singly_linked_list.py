import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    # Verifica que al insertar el primer nodo, tail.next apunte a head (circularidad)
    def test_insertar_primer_nodo_circular(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(7, "red")
        self.assertIs(lista.tail.next, lista.head)

    # Verifica que ver_apuestas retorne una lista vacía cuando no hay apuestas
    def test_ver_apuestas_lista_vacia(self):
        lista = SinglyLinkedList()
        self.assertEqual(lista.ver_apuestas(), [])

    # Verifica que al eliminar el único nodo, head, tail y size queden en None/0
    def test_eliminar_unico_nodo_deja_lista_vacia(self):
        lista = SinglyLinkedList()
        lista.insertar_apuesta(7, "red")
        lista.eliminar_apuesta(7)
        self.assertIsNone(lista.head)
        self.assertIsNone(lista.tail)
        self.assertEqual(lista.size, 0)

    # Verifica que verificar_ganador retorne lista vacía si no hay apuestas registradas
    def test_verificar_ganador_lista_vacia(self):
        lista = SinglyLinkedList()
        self.assertEqual(lista.verificar_ganador(7, "red"), [])


if __name__ == "__main__":
    unittest.main()
