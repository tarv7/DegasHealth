import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

def iniciar():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	criarTabFuncionarios()
	conn.commit()
	conn.close()

def deletarTabela(tabela):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("DROP TABLE IF EXISTS " + tabela)

	conn.commit()
	conn.close()

def criarTabFuncionarios():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS funcionarios(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			tipo TEXT NOT NULL,
			nome TEXT NOT NULL,
			crm TEXT NOT NULL,
			sexo VARCHAR(1) NOT NULL,
			nacionalidade TEXT NOT NULL,
			nascimento TEXT NOT NULL,
			admissao TEXT NOT NULL,
			formatura TEXT NOT NULL
		)
		"""
	)

	conn.commit()
	conn.close()

def inserir(tab, tupla):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO " + tab + "(tipo, nome, crm, sexo, nacionalidade, nascimento, admissao, formatura) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tupla)

	conn.commit()
	conn.close()


def mostrarTodos():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()
	# lendo os dados
	cursor.execute("""
	SELECT * FROM funcionarios;
	""")

	for linha in cursor.fetchall():
		print(linha)

	conn.commit()
	conn.close()

def verificaCRM(crm):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM funcionarios WHERE crm = ?", (crm,))

	return len(cursor.fetchall())

def busca(tabela, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	if not chave.isnumeric():
		coluna = 'nome'
	else:
		coluna = 'crm'

	query = "SELECT nome, sexo, crm, nacionalidade, nascimento, admissao, formatura FROM %s WHERE %s = '%s'" % (tabela, coluna, chave)
	cursor.execute(query)

	medico = cursor.fetchone()
	strMedico = '%'.join(medico)

	conn.commit()
	conn.close()
	return [True, strMedico]

def buscaColuna(tabela, crm, coluna):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "SELECT " + coluna + " FROM " + tabela + " WHERE crm = " + crm
	cursor.execute(query)

	return cursor.fetchone()[0]

def altera(tabela, crm, coluna, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "UPDATE " + tabela + " SET " + coluna + " = '" + chave + "' WHERE crm = " + crm
	cursor.execute(query)

	conn.commit()
	conn.close()