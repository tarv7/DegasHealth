import implementacao.banco_de_dados.conexao as db
from implementacao.funcionario import *
import implementacao.utils.utils as util

# Nome, COREN, Sexo, Nacionalidade, Data Nasc., Data Admiss., Data Formatura
class auxiliar(Funcionario):
	def __init__(self):
		db.iniciar()
		super().__init__()
	def novoAuxiliar(self, nome, sexo, coren, nac, nasc, admis, form):
		# Testa nome
		if util.testaCarc(nome) != 'a':
			return "ERRO! Caracter '" + util.testaCarc(nome) + "' Invalido!"

		# Testa Nacionalidade
		if util.testaCarc(nac) != 'a':
			return "ERRO! Caracter '" + util.testaCarc(nac) + "' Invalido!"

		# Verifica se COREM ja existe
		if util.corenJaExiste('auxiliares', coren) > 0:
			return "ERRO! COREN Já existente!"

		if util.verificaDataInvalida(nasc) or util.verificaDataInvalida(admis) or util.verificaDataInvalida(form):
			return "ERRO! Data Inválida!"

		if util.verificaDatasAnteriores(admis, form) < 0:
			return "ERRO! Inconsistencia de datas: Formatura posterior a admissão!"

		nasc = util.conserta(nasc)
		admis = util.conserta(admis)
		form = util.conserta(form)

		db.inserir('auxiliares', 'coren', (nome, coren, sexo, nac, nasc, admis, form))
		return 'Auxiliar/Técnico inserido!'

	def encontraAuxiliar(self, chave):
		busca = db.busca("auxiliares", 'coren', chave)
		if busca[0] == True:
			return busca[1]

#Alteracao executada com sucesso!
#ERRO! Inconsistencia de datas: Formatura posterior a admissão!
	def alteraAuxiliar(self, coren, coluna, chave):
		colunas = {}
		colunas["Nome"] = "nome"
		colunas["Sexo"] = "sexo"
		colunas["Nacionalidade"] = "nacionalidade"
		colunas["DtNasc"] = "nascimento"
		colunas["DtAdmiss"] = "admissao"
		colunas["DtFormatura"] = "formatura"

		if colunas[coluna] == "admissao":
			form = db.buscaColuna('auxiliares', 'coren', coren, 'formatura')
			if util.verificaDatasAnteriores(chave, form) < 0:
				return "ERRO! Inconsistencia de datas: Formatura posterior a admissão!"
		elif colunas[coluna] == "formatura":
			admis = db.buscaColuna('auxiliares', 'coren', coren, 'admissao')
			if util.verificaDatasAnteriores(admis, chave) < 0:
				return "ERRO! Inconsistencia de datas: Formatura posterior a admissão!"
		
		altera = db.altera('auxiliares', 'coren', coren, colunas[coluna], chave)
		return "Alteracao executada com sucesso!"