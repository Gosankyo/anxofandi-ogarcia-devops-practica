from typing import Dict, List
from models.Usuario import Usuario, Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido

class TiendaService:
    def __init__(self):
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: str = None) -> Usuario:
        if tipo == "cliente":
            usuario = Cliente(nombre, email, direccion)
        elif tipo == "admin":
            usuario = Administrador(nombre, email)
        else:
            raise ValueError("Tipo de usuario no válido")
        self.usuarios[usuario.id] = usuario
        return usuario

    def agregar_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> None:
        if producto_id in self.productos:
            del self.productos[producto_id]

    def listar_productos(self) -> List[Producto]:
        return list(self.productos.values())

    def realizar_pedido(self, cliente_id: str, items: Dict[str, int]) -> Pedido:
        if cliente_id not in self.usuarios:
            raise ValueError("Cliente no existe")
        cliente = self.usuarios[cliente_id]
        if not isinstance(cliente, Cliente):
            raise ValueError("Solo los clientes pueden hacer pedidos")

        productos_seleccionados = {}
        for pid, cantidad in items.items():
            if pid not in self.productos:
                raise ValueError(f"Producto {pid} no existe")
            producto = self.productos[pid]
            if not producto.hay_stock(cantidad):
                raise ValueError(f"No hay suficiente stock de {producto.nombre}")
            producto.actualizar_stock(-cantidad)
            productos_seleccionados[producto] = cantidad

        pedido = Pedido(cliente, productos_seleccionados)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_usuario(self, cliente_id: str) -> List[Pedido]:
        return sorted(
            [p for p in self.pedidos if p.cliente.id == cliente_id],
            key=lambda x: x.fecha
        )
