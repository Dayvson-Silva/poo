# exercicio de get e set privacidade 
# registro de aluno
import random

class Aluno:
    def __init__(self,name,age,registry):
        self.__name = name
        self.__age = age
        self.__matricula = registry
        
    def get_name(self):
        return self.__name
    def set_name(self , new_name):
        if new_name:
            self.__name = new_name
            
    def get_age (self):
        return self.__age
    def set_age(self , new_age):
        if new_age:
            self.__name = new_age
            
    def get_registry (self):
        return self.__matricula
    def set_registry(self , new_registry):
        if new_registry:
            self.__name = new_registry
    

student = Aluno(input("type your name: "), input("type your age: "), random.randint(100000, 1000000))

name = student.get_name()
print(name)

age = student.get_age()
print(age)

resgistry = student.get_registry()
print(resgistry)

