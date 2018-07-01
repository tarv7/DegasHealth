import implementacao.banco_de_dados.conexao as db
import implementacao.utils.utils as util

# Codigo, Descricao, Custo
class equipamento(object):
	def __init__(self):
		db.iniciar()
		super().__init__()
	def novoEquipamento(self, cod, desc, valor):
		db.inserirEquipamento((cod, desc, valor))
		return 'Equipamento cadastrado com sucesso'

	def tombaEquipamento(self, codEqui, tombo):
		if db.jaTombado(codEqui, tombo):
			return 'Erro: Tombo já existente'

		db.inserirTombo((codEqui, tombo))
		return 'Equipamento tombado com sucesso'