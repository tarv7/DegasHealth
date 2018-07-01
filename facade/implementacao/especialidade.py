import implementacao.banco_de_dados.conexao as db
import implementacao.utils.utils as util

# Especialidade: codigo, descricao
class especialidade(object):
	def __init__(self):
		db.iniciar()
		super().__init__()
	def novaEspecialidade(self, cod, desc):
		if util.colEspJaExiste('cod', cod) > 0:
			return "Especialidade já cadastrada"
		if util.colEspJaExiste('desc', desc) > 0:
			return "Especialidade já cadastrada"

		db.inserirEspecialidade((cod, desc))
		return 'Especialidade Registrada com sucesso'

	def encontraEspecialidade(self, chave):
		busca = db.buscaEsp('cod', chave)
		if busca[0] == True:
			return busca[1]
		else:
			busca = db.buscaEsp('desc', chave)
			if busca[0] == True:
				return busca[1]
			else:
				return "Especialidade não cadastrada"

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