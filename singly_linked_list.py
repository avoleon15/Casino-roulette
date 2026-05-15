from Node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # primer nodo de la lista
        self.tail = None  # último nodo; su .next apunta a head (circular)
        self.size = 0     # cantidad de apuestas activas

    def insertar_apuesta(self, number: int, color: str, monto: float):
        new_node = Node(number, color, monto)
        if self.head is None:
            # lista vacía: el único nodo se apunta a sí mismo
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            # encadenar al final y cerrar el ciclo hacia head
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def eliminar_apuesta(self, number: int):
        if self.head is None:
            return False

        current = self.head
        prev = self.tail  # en lista circular, prev empieza en tail

        for _ in range(self.size):
            if current.number == number:
                if self.size == 1:
                    # era el único nodo
                    self.head = None
                    self.tail = None
                else:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                    if current == self.tail:
                        self.tail = prev
                self.size -= 1
                return True
            prev = current
            current = current.next

        return False  # número no encontrado

    def ver_apuestas(self):
        if self.head is None:
            return []

        apuestas = []
        current = self.head
        # recorrer exactamente size nodos para no entrar en loop infinito
        for _ in range(self.size):
            apuestas.append({"number": current.number, "color": current.color, "monto": current.monto})
            current = current.next
        return apuestas

    def verificar_ganador(self, resultado_number: int, resultado_color: str):
        if self.head is None:
            return []

        ganadores = []
        current = self.head
        # recorrer todas las apuestas y comparar contra el resultado de la ruleta
        for _ in range(self.size):
            gana_number = current.number == resultado_number
            gana_color = current.color == resultado_color
            if gana_number or gana_color:
                ganadores.append({
                    "number": current.number,
                    "color": current.color,
                    "gana_por_numero": gana_number,
                    "gana_por_color": gana_color,
                    "monto": current.monto
                })
            current = current.next
        return ganadores
