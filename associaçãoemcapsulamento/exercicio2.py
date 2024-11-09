# gerenciamento de tarefas
class Tarefa:
    def __init__(self,name,description,prioridade):
        self.name = name
        self.description = description
        self.prioridade = prioridade

class Projeto:
    def __init__(self,name):
        self.name = name
        self.tarefas = []
    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(f"tarefa -> {tarefa.name}")
            print(f"descrição -> {tarefa.description}")
            print(f"prioridade -> {tarefa.prioridade}")
            print("==================================")
            
        
casa_limpa = Projeto("Casa Limpa")
lavar_louca = Tarefa("Lavar louça", "Lave e seque", 2)
lavar_banheiro = Tarefa("lavar banheiro", "logoooooo", 1)

casa_limpa.tarefas.append(lavar_louca) 
casa_limpa.tarefas.append(lavar_banheiro) 


casa_limpa.listar_tarefas()
        
         
        