opt = int(input("1 - carro \n2 - bike \nEscolha: "))

class Veiculo:
    def __init__(self):
        self.name = str(input(f"Me informe o nome do seu Veículo :"))
        self.color = str(input(f"Me informe a cor do seu Veículo :"))
        self.model = str(input(f"Me informe o modelo do seu Veículo :"))
    
     
          
class Car(Veiculo):
    def __init__(self):
        super().__init__()
    def info_car(self):
        return f"O nome do seu Veículo é {self.name} com a cor {self.color} e o modelo {self.model}"
  

class Bike(Veiculo):
    def __init__(self):
        super().__init__()
    def info_bike(self):
        return f"O nome do seu Veículo é {self.name} com a cor {self.color} e o modelo {self.model}"

       
    
     
my_bike = Bike()
my_car = Car() 
match opt:
    case 1:
        if opt == 1:
            print(my_car.info_car())
        else:
            print(my_bike.info_bike())
            
        


        