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

def corenJaExiste(coren):
	return db.verificaCOREN(coren)

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