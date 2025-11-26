from services.Tienda_service import TiendaService
from models.Producto import ProductoElectronico, ProductoRopa, Producto

if __name__ == "__main__":
    tienda = TiendaService()

    # Registrar usuarios
    cliente1 = tienda.registrar_usuario("cliente", "Ana", "ana@example.com", "Calle A")
    cliente2 = tienda.registrar_usuario("cliente", "Luis", "luis@example.com", "Calle B")
    cliente3 = tienda.registrar_usuario("cliente", "Marta", "marta@example.com", "Calle C")
    admin = tienda.registrar_usuario("admin", "Carlos", "carlos@example.com")

    # Agregar productos
    p1 = ProductoElectronico("Portatil", 1200, 5, 24)
    p2 = ProductoElectronico("Movil", 800, 10, 12)
    p3 = ProductoRopa("Camiseta", 20, 50, "M", "Rojo")
    p4 = ProductoRopa("Pantalon", 40, 30, "L", "Azul")
    p5 = Producto("Libro", 15, 100)

    for p in [p1, p2, p3, p4, p5]:
        tienda.agregar_producto(p)

    # Listar productos
    print("\n--- INVENTARIO ---")
    for producto in tienda.listar_productos():
        print(producto)

    # Realizar pedidos
    pedido1 = tienda.realizar_pedido(cliente1.id, {p1.id: 1, p3.id: 2})
    pedido2 = tienda.realizar_pedido(cliente2.id, {p2.id: 1, p5.id: 3})
    pedido3 = tienda.realizar_pedido(cliente3.id, {p4.id: 2, p5.id: 1})

    print("\n--- PEDIDOS REALIZADOS ---")
    for pedido in [pedido1, pedido2, pedido3]:
        print(pedido)
        print("-" * 50)

    # Histórico de pedidos de un cliente
    print("\n--- HISTORICO DE PEDIDOS DE ANA ---")
    for pedido in tienda.listar_pedidos_usuario(cliente1.id):
        print(pedido)
