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