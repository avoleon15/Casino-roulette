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

