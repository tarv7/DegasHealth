import string
from datetime import datetime
import implementacao.banco_de_dados.conexao as db

def testaCarc(palavra):
	for i in range(len(palavra)):
		if not palavra[i].isalpha() and palavra[i] != ' ':
			return palavra[i]

	return 'a'

def crmJaExiste(crm):
	return db.verificaCRM(crm)

def corenJaExiste(tab, coren):
	return db.verificaCOREN(tab, coren)

def codProcJaExiste(cod):
	return db.verificaCod(cod)

def descProcJaExiste(chave):
	return db.buscaColProc('procedimentos', 'desc', chave)

def colEspJaExiste(coluna, chave):
	return db.buscaColProc('especialidades', coluna, chave)

def verificaDataInvalida(dataStr):
	try:
		dt = datetime.strptime(dataStr, "%d/%m/%Y")
	except Exception:
		return True

def verificaDatasAnteriores(data1, data2):
	data1_obj = datetime.strptime(data1, "%d/%m/%Y")
	data2_obj = datetime.strptime(data2, "%d/%m/%Y")

	return (data1_obj - data2_obj).days

def conserta(data):
	return datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")

def ehMoeda(valor):
	if valor[0] == 'R' and valor[1] == '$':
		valor = valor[2:]
	elif valor[0] == '$':
		valor = valor[1:]

	if valor.find('.') >= 0:
		return False

	if not valor[0].isdigit():
		return False
	else:
		try:
			valor[1:].replace(",", ".", 1)
			return True
		except Exception:
			return False