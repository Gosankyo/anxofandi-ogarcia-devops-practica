import uuid
from datetime import datetime
from typing import Dict
from .Usuario import Cliente
from .Producto import Producto

class Pedido:
    def __init__(self, cliente: Cliente, productos: Dict[Producto, int]):
        self.id = str(uuid.uuid4())
        self.cliente = cliente
        self.productos = productos  # dict {producto: cantidad}
        self.fecha = datetime.now()

    def calcular_total(self) -> float:
        return sum(prod.precio * cantidad for prod, cantidad in self.productos.items())

    def __str__(self) -> str:
        productos_str = "\n".join(
            [f" - {prod.nombre} x{cantidad} = {prod.precio * cantidad:.2f}€"
             for prod, cantidad in self.productos.items()]
        )
        return (f"Pedido {self.id}\nCliente: {self.cliente.nombre}\nFecha: {self.fecha}\n"
                f"Productos:\n{productos_str}\nTOTAL: {self.calcular_total():.2f}€")
