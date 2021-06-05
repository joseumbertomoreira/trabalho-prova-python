from lib.Crud import Crud

class Menu:
  
  listaTarefas = []
  crud = Crud()

  def init(self):
    
    while True:
      print("O que gostaria de fazer? Digite: ")
      print("\t1 - Adicionar uma tarefa.")
      print("\t2 - Mostrar as tarefas.")
      print("\t3 - Concluir uma tarefa.")
      print("\t4 - Buscar tarefas na base de dados.")
      print("\t5 - Inserir tarefas na base de dados.")
      print("\t0 - Sair.")

      opcoes = int(input())

      if opcoes == 1:

        self.crud.adicionaTarefa(self.listaTarefas)
        
        print("\n")
      
      elif opcoes == 2:
        self.crud.mostraTarefas(self.listaTarefas)

        print("\n")
      
      elif opcoes == 3:
        self.crud.concluiTarefa(self.listaTarefas)

        print("\n")
      
      elif opcoes == 4:
        self.crud.buscaDadosSQLite(self.listaTarefas)

        print("\n")
      
      elif opcoes == 5:
        self.crud.insereDadosSQLite(self.listaTarefas)

        print("\n")
      
      elif opcoes == 0:
        print("Bye bye!")
        print("\n")
        break

      else:
        print("Essa opção não existe")
        print("\n")
