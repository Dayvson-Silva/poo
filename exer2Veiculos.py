opt = int(input("1 - carro \n2 - bike \nEscolha: "))


    
     
match opt:
    case 1:

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
  
        my_car = Car() 
        print(my_car.info_car)



    case 2:

        class Veiculo:
            def __init__(self):
                self.name = str(input(f"Me informe o nome do seu Veículo :"))
                self.color = str(input(f"Me informe a cor do seu Veículo :"))
                self.model = str(input(f"Me informe o modelo do seu Veículo :"))

        class Bike(Veiculo):
            def __init__(self):
                super().__init__()
            def info_bike(self):
                return f"O nome do seu Veículo é {self.name} com a cor {self.color} e o modelo {self.model}"

       


            
        


        