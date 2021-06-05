from lib.Tarefa import Tarefa
import sqlite3

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
    

  def concluiTarefa(self, listaTarefas):

    if(len(listaTarefas) <= 0):
      print("Não há tarefas para concluir")
      return
    
    while True:
      nome = input("Qual o nome da tarefa que gostaria de concluir? ")

      for tarefa in listaTarefas:
        if nome == tarefa.nome:
          tarefa.concluido = 1
          return
      
      print("Não existe tarefa com esse nome! Tente novamente...")
      print("\n")


  
  def adicionaTarefa(self, listaTarefas):

    nomeAtividade = input("Qual o nome da atividade? ")

    tipoAtividade = self.tipoAtividade()

    descricaoAtividade = input("Descreva a atividade: ")

    prazo = input("Prazo para conclusão(use dd/mm/yy)? ")
    
    tarefa = Tarefa(nomeAtividade, tipoAtividade, descricaoAtividade, prazo)
    listaTarefas.append(tarefa)

  
  def mostraTarefas(self, listaTarefas):

    if(len(listaTarefas) <= 0):
      print("Não há tarefas para mostrar")
      return
    
    print("\n")

    for tarefa in listaTarefas:
      print(
        f"| {tarefa.nome} | {tarefa.atividade} | {tarefa.tipo.value} | {tarefa.atividade} | {tarefa.prazo} | {tarefa.concluido} |"
      )
    
    print("\n")

  
  def notInListaTarefas(self, listaTarefas, rowNome):

    for tarefa in listaTarefas:
      if tarefa.nome == rowNome:
        print(f"{tarefa.nome} e {rowNome}")
        
        return False
    
    return True

  def buscaDadosSQLite(self, listaTarefas):

    conn = sqlite3.connect("./database/tarefas-db")

    cursor = conn.cursor()

    if not listaTarefas:
      for row in cursor.execute("SELECT * FROM Tarefas"):
        
        tarefa = Tarefa(row[0], row[1], row[2], row[3])
        listaTarefas.append(tarefa)        

    else:
      for row in cursor.execute("SELECT * FROM Tarefas"):

        if self.notInListaTarefas(listaTarefas, row[0]):
          tarefa = Tarefa(row[0], row[1], row[2], row[3])
          listaTarefas.append(tarefa)

    
    conn.commit()
    conn.close()
    
    

  def insereDadosSQLite(self, listaTarefas):

    if(len(listaTarefas) <= 0):
      print("Não há tarefas para concluir")
      return

    conn = sqlite3.connect("./database/tarefas-db")
    cursor = conn.cursor()

    for tarefa in listaTarefas:
      cursor.execute(
        f"INSERT OR REPLACE INTO Tarefas VALUES (\
          '{tarefa.nome}',\
          '{tarefa.tipo.value}',\
          '{tarefa.atividade}',\
          '{tarefa.prazo}',\
          {tarefa.concluido})"
      )
    
    conn.commit()
    cursor.close()    
    conn.close()