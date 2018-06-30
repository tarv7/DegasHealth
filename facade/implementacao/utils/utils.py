import string
import implementacao.banco_de_dados.conexao as db

def testaCarc(palavra):
	for i in range(len(palavra)):
		if not palavra[i].isalpha() and palavra[i] != ' ':
			return palavra[i]

	return 'a'

def crmJaExiste(crm):
	return db.verificaCRM(crm)