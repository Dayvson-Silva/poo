# Exemplos

# my_name = 'Dayvson'.upper()
# print(type(my_name))


# my_numbers = [22,94,17]


# my_numbers.append(0)
# print(type(my_numbers))


# class Carro:
#     # atributos
#     def __init__(self, modelo, cor, placa, motor):
#         self.modelo = modelo
#         self.cor = cor
#         self.placa = placa
#         self.motor = motor

#     # todo metodo dentro de uma classe precisar usar SELF
#     # metodos
#     def ligar(self):
#         print("Carro a Todo Vapor")

#     def buzinar(self):
#         print("BI BI TI")
        
#     def frear(self):
#         print("uuuuuhuhuhuuhuuhh")
        
# uno_com_escada = Carro("uno", "verde", "DDD-4545",1.4)
# uno_sem_escada = Carro("uno", "verde", "DDD-4545",1.4)
# uno_com_escada.ligar()
# # pra chamar dentro da classe
# print(uno_sem_escada.motor)


# exemplo 1

# class Cachorro:
#     def __init__(self, name, race, age):
#         self.name = name
#         self.race = race
#         self.age = age

# caremelo = Cachorro("cletin Fubá","Vira-Lata", 4)
# print(caremelo.race)


# exemplo 2 outro estilo de se fazer com def 

# class Pessoa:
#     def __init__(self, name, age, weight, gender):
#         self.name = name
#         self.age = age
#         self.weigh = weight
#         self.gender = gender
    
#     def mostra_infos(self):
#         return f"O {self.name} tem a idade de {self.age} anos, com o peso de {self.weigh} quilos e do genero {self.gender}"
    
# dayvson = Pessoa("Dayvson", 30, 135, "Masculino")
# print(dayvson.mostra_infos())


# exemplo 3 

class Business:

    def __init__(self):
        self.employers = []

    def add_employers(self):
        employer = {
            "name": input("Digite o nome do funcionario :"),
            "role": input("Digite o seu  cargo :"),
            "salary": float(input("Digite o salario que vai receber :"))
        }


        self.employers.append(employer)
        print("Bem Vindo a Empresa VASP")


    def list_employers(self):
        for func in self.employers:
            print(func["name"])
            print(func["role"])
            print(func["salary"])

    def remove_employers(self):
        name_remove = input("Digite o nome do fucionario que deseja desligar da empresa :")
        for func in self.employers:
            if func["name"] == name_remove:
                self.employers.remove(func)
                print("Funcionario Desligado da Empresa")

vasp =  Business()

vasp.add_employers()
vasp.list_employers()
vasp.remove_employers()


        
