import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

def iniciar():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	criarTabMedicos()
	criarTabEnfermeiros()
	criarTabAuxiliares()
	conn.commit()
	conn.close()

def deletarTabela(tabela):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("DROP TABLE IF EXISTS " + tabela)

	conn.commit()
	conn.close()

def criarTabMedicos():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS medicos(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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

# COREN -> Conselho Regional de Enfermagem
# novoEnfermeiro: Nome, Sexo, COREN, Nacionalidade, Data Nasc., Data Admiss., Data Formatura
def criarTabEnfermeiros():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS enfermeiros(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nome TEXT NOT NULL,
			coren TEXT NOT NULL,
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
def criarTabAuxiliares():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS auxiliares(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nome TEXT NOT NULL,
			coren TEXT NOT NULL,
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

def inserir(tab, crmcoren, tupla):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO " + tab + "(nome, "+crmcoren+", sexo, nacionalidade, nascimento, admissao, formatura) VALUES (?, ?, ?, ?, ?, ?, ?)", tupla)

	conn.commit()
	conn.close()


def mostrarTodos():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()
	# lendo os dados
	cursor.execute("""
	SELECT * FROM medicos;
	""")

	for linha in cursor.fetchall():
		print(linha)

	conn.commit()
	conn.close()

def verificaCRM(crm):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM medicos WHERE crm = ?", (crm,))

	return len(cursor.fetchall())

def verificaCOREN(tab, coren):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM "+tab+" WHERE coren = ?", (coren,))

	return len(cursor.fetchall())

def busca(tabela, crmcoren, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	if not chave.isnumeric():
		coluna = 'nome'
	else:
		coluna = crmcoren

	query = "SELECT nome, sexo, "+crmcoren+", nacionalidade, nascimento, admissao, formatura FROM %s WHERE %s = '%s'" % (tabela, coluna, chave)
	cursor.execute(query)

	medico = cursor.fetchone()
	strMedico = '%'.join(medico)

	conn.commit()
	conn.close()
	return [True, strMedico]

def buscaColuna(tabela, crmcoren, crmcorenValue, coluna):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "SELECT " + coluna + " FROM " + tabela + " WHERE "+crmcoren+" = " + crmcorenValue
	cursor.execute(query)

	return cursor.fetchone()[0]

def altera(tabela, crmcoren, crmcorenValue, coluna, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "UPDATE " + tabela + " SET " + coluna + " = '" + chave + "' WHERE "+crmcoren+" = " + crmcorenValue
	cursor.execute(query)

	conn.commit()
	conn.close()