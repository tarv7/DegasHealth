import implementacao.banco_de_dados.conexao as db
from implementacao.funcionario import *
import implementacao.utils.utils as util

# Nome, CRM, Sexo, Nacionalidade, Data Nasc., Data Admiss., Data Formatura
class medico(Funcionario):
	def __init__(self):
		db.iniciar()
		super().__init__()
	def novoMedico(self, nome, sexo, crm, nac, nasc, admis, form):
		# Testa nome
		if util.testaCarc(nome) != 'a':
			return "ERRO! Caracter " + util.testaCarc(nome) + " Invalido!"

		# Verifica se CRM ja existe
		if util.crmJaExiste(crm) > 0:
			return "ERRO! CRM Já existente!"

		# Testa Nacionalidade
		if util.testaCarc(nac) != 'a':
			return "ERRO! Caracter " + util.testaCarc(nac) + " Invalido!"

		db.inserir('funcionarios', ('medico', nome, crm, sexo, nac, nasc, admis, form))
		return 'Medico inserido!'

novo = medico()
#novo.novoMedico('Thales', '123', 'M',"Brasil","26/08/1977","29/06/2012","28/01/2007")
#db.mostrarTodos()