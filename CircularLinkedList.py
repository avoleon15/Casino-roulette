import random
from Node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tall = None
        self.current = None
        self.size = 0



    def insertar_numero(self, number: int):
        
        new_node = Node(number)
        if self.head is None:
            self.head = new_node
            self.tall = new_node
            self.tall.next = self.head
        
        else:
            self.tall.next = new_node
            self.tall = new_node
            self.tall.next = self.head
        
        self.size += 1
        

    def construir_ruleta(self):
        for numero in range(37):
            self.insertar_numero(numero)
        self.current = self.head


    def girar(self) -> int:
        if self.head is None:
            raise RuntimeError("La ruleta no está construida. Llama a construir_ruleta() primero.")
        
        pasos = random.randint(1, self.size * 3)
        for _ in range(pasos):
            self.current = self.current.next

        return self.current.number
    
    def __repr__(self):
        if self.head is None:
            return 'CircularLinkedList(vacía)'
        numeros = []
        nodo = self.hand
        for _  in range(self.size):
            numeros.append(str(nodo.number))
            nodo = nodo.next
        return f"CircularLinkedList([{', '.join(numeros)}] → head)"
