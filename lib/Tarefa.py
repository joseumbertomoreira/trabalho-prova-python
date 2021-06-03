from lib.TipoTarefa import TipoTarefa

class Tarefa:
  
  concluido = 0

  def __init__(self, nome, tipo, atividade, prazo):
    
    self.nome = nome
    
    if tipo == 1:
      self.tipo = TipoTarefa.PESSOAL
    
    elif tipo == 2:
      self.tipo = TipoTarefa.TRABALHO
    
    elif tipo == 3:
      self.tipo = TipoTarefa.FACULDADE
    
    self.atividade = atividade

    self.prazo = prazo

