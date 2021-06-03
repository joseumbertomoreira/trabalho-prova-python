from lib.Tarefa import Tarefa

class Crud:


  def tipoAtividade(self):
    while True:

      print("Qual o tipo de atividade: ")
      print("\t1 - Pessoal.")
      print("\t2 - Trabalho.")
      print("\t2 - faculdade.")
      print("\n")
      
      opcoes = int(input())

      if opcoes != 1 & opcoes != 2 & opcoes != 3:
        print("Opção inexistente! Escolha outra.")
        print("\n")
      else:
        return opcoes
    
    

  
  def adicionarTarefa(self, listaTarefas):

    nomeAtividade = input("Qual o nome da atividade? ")

    tipoAtividade = self.tipoAtividade()

    descricaoAtividade = input("Descreva a atividade: ")

    prazo = input("Prazo para conclusão(use dd/mm/yy)? ")
    
    tarefa = Tarefa(nomeAtividade, tipoAtividade, descricaoAtividade, prazo)
    listaTarefas.append(tarefa)

    