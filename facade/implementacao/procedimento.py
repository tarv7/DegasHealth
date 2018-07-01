import implementacao.banco_de_dados.conexao as db
import implementacao.utils.utils as util

# Codigo, Descricao, Custo
class procedimento(object):
	def __init__(self):
		db.iniciar()
		super().__init__()
	def novoProcedimento(self, cod, desc, custo):
		# Verifica se CRM ja existe
		if util.codProcJaExiste(cod) > 0:
			return "Código de Procedimento Ja Cadastrado"

		if util.descProcJaExiste(desc) > 0:
			return "Descrição de Procedimento Ja Cadastrado"

		if not util.ehMoeda(custo):
			return "Erro: valor de custo inválido"

		if custo[0] == 'R':
			custo = custo[2:]
		elif custo[0] == '$':
			custo = custo[1:]

		db.inserirProcedimento((cod, desc, custo))
		return 'Procedimento Incluido com Sucesso'

	def encontraProcedimento(self, chave):
		busca = db.buscaProc('cod', chave)
		if busca[0] == True:
			return busca[1]
		else:
			busca = db.buscaProc('desc', chave)
			if busca[0] == True:
				return busca[1]
			else:
				return "Procedimento não cadastrado"

#Alteracao executada com sucesso!
#ERRO! Inconsistencia de datas: Formatura posterior a admissão!
	def alteraProcedimento(self, cod, coluna, chave):
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
		return "Procedimento alterado com sucesso"