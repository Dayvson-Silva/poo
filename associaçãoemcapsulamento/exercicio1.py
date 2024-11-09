
# loja online
class Cliente:
    def __init__(self,name,cpf):
        self.name = name
        self.cpf = cpf
        self.pedidos = []
        
    def listar_pedidos(self):
        for pedido in self.pedidos:
            print(f"pedido nome {pedido.name}")
            print(f"price {pedido.price}")

            
class Pedido:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.cliente = None
        
        
rian = Cliente("rian", 12345678)
pedido1 = Pedido( "arroz", 5.5)

rian.pedidos.append(pedido1)
pedido1.cliente = rian

rian.listar_pedidos()

    
         
    