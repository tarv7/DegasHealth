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

	def encontraEquipamento(self, chave):
		busca = db.buscaProc('cod', chave)
		if busca[0] == True:
			return busca[1]
		else:
			busca = db.buscaProc('desc', chave)
			if busca[0] == True:
				return busca[1]
			else:
				return "Equipamento não cadastrado"

#Alteracao executada com sucesso!
#ERRO! Inconsistencia de datas: Formatura posterior a admissão!
	def alteraEquipamento(self, cod, coluna, chave):
		colunas = {}
		colunas["Valor"] = "custo"
		colunas["Descricao"] = "desc"

		if colunas[coluna] == "custo":
			custo = chave
			if not util.ehMoeda(custo):
				return "Erro: valor de custo inválido"

			if custo[0] == 'R':
				custo = custo[2:]
			elif custo[0] == '$':
				custo = custo[1:]
		
		altera = db.alteraProc(cod, colunas[coluna], chave)
		return "Equipamento alterado com sucesso"