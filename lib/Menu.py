from lib.Crud import Crud

class Menu:
  
  listaTarefas = []
  crud = Crud()

  def init(self):
    
    while True:
      print("O que gostaria de fazer? Digite: ")
      print("\t1 - Adicionar uma tarefa.")
      print("\t2 - Listar as tarefas.")
      print("\t3 - Concluir uma tarefa.")
      print("\t4 - Buscar tarefas na base de dados.")
      print("\t5 - Inserir tarefas na base de dados.")
      print("\t0 - Sair.")

      opcoes = int(input())

      if opcoes == 1:

        self.crud.adicionarTarefa(self.listaTarefas)
        
        print("\n")
      
      elif opcoes == 2:
        print("Lista tarefas")
        print("\n")
      
      elif opcoes == 3:
        print("Concluo tarefas")
        print("\n")
      
      elif opcoes == 4:
        print("Buscar na base de dados")
        print("\n")
      
      elif opcoes == 5:
        print("Inserir na base de dados")
        print("\n")
      
      elif opcoes == 0:
        print("Bye bye!")
        print("\n")
        break

      else:
        print("Essa opção não existe")
        print("\n")
