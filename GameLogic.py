from singly_linked_list import SinglyLinkedList
from circular_linked_list import CircularLinkedList
 
 
class Game:
    def __init__(self, saldo_inicial: float = 1000.0):
        self.saldo = saldo_inicial
        self.apuestas = SinglyLinkedList()
        self.ruleta = CircularLinkedList()
        self.ruleta.construir_ruleta()

    def apostar(self, number: int, color: str, monto: float) -> bool:
        """
        Registra una apuesta si hay saldo suficiente.
        Descuenta el monto del saldo y lo inserta en la lista de apuestas.
        Retorna True si la apuesta fue registrada, False si no hay saldo.
        """
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return False
 
        if monto > self.saldo:
            print(f"Saldo insuficiente. Saldo actual: {self.saldo}")
            return False
 
        self.saldo -= monto
        self.apuestas.insertar_apuesta(number, color, monto)
        print(f"Apuesta registrada: número {number}, color {color}, monto {monto}. Saldo restante: {self.saldo}")
        return True
    

    def calcular_resultado(self) -> float:
        """
        Gira la ruleta, verifica las apuestas ganadoras y actualiza el saldo.
        Retorna el número donde cayó la ruleta.
 
        Pagos:
            - Gana por número exacto : 35x el monto
            - Gana por color         : 2x el monto
            - Gana por ambos         : 35x + 2x el monto
        """
        resultado_number = self.ruleta.girar()
        resultado_color = self._color_del_numero(resultado_number)
 
        print(f"\nRuleta cayó en: {resultado_number} ({resultado_color})")
 
        ganadores = self.apuestas.verificar_ganador(resultado_number, resultado_color)

        if not ganadores:
            print("Ninguna apuesta ganó esta ronda.")
        else:
            for apuesta in ganadores:
                ganancia = 0
                if apuesta["gana_por_numero"]:
                    ganancia += apuesta["monto"] * 35
                if apuesta["gana_por_color"]:
                    ganancia += apuesta["monto"] * 2
                self.saldo += ganancia
                print(f"  ¡Ganaste! Número {apuesta['number']}, color {apuesta['color']} → +{ganancia}. Saldo: {self.saldo}")
 
        # Limpiar apuestas de la ronda
        self.apuestas = SinglyLinkedList()
 
        return resultado_number