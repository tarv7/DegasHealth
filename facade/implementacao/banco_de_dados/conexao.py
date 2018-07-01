import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

def iniciar():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	criarTabMedicos()
	criarTabEnfermeiros()
	criarTabAuxiliares()
	criarTabProcedimentos()
	criarTabEspecialidades()
	criarTabEquipamentos()
	criarTabTombos()
	criarTabMateriais()
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

def criarTabProcedimentos():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS procedimentos(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			cod TEXT NOT NULL,
			desc TEXT NOT NULL,
			custo TEXT NOT NULL
		)
		"""
	)

	conn.commit()
	conn.close()

# Especialidade: codigo, descricao
def criarTabEspecialidades():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS especialidades(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			cod TEXT NOT NULL,
			desc TEXT NOT NULL
		)
		"""
	)

	conn.commit()
	conn.close()

def criarTabEquipamentos():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS equipamentos(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			cod TEXT NOT NULL,
			desc TEXT NOT NULL,
			valor TEXT NOT NULL,
			tombo TEXT
		)
		"""
	)

	conn.commit()
	conn.close()

def criarTabTombos():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS tombos(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			fk_equi_cod TEXT NOT NULL,
			tombo TEXT NOT NULL
		)
		"""
	)

	conn.commit()
	conn.close()

def criarTabMateriais():
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS materiais(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			cod TEXT NOT NULL,
			desc TEXT NOT NULL,
			quant TEXT NOT NULL
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

def inserirProcedimento(tupla):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO procedimentos (cod, desc, custo) VALUES (?, ?, ?)", tupla)

	conn.commit()
	conn.close()

def inserirEspecialidade(tupla):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO especialidades (cod, desc) VALUES (?, ?)", tupla)

	conn.commit()
	conn.close()

def inserirEquipamento(tupla):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO equipamentos (cod, desc, valor) VALUES (?, ?, ?)", tupla)

	conn.commit()
	conn.close()

def inserirTombo(tupla):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO tombos (fk_equi_cod, tombo) VALUES (?, ?)", tupla)

	conn.commit()
	conn.close()

def inserirMaterial(tupla):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO materiais (cod, desc, quant) VALUES (?, ?, ?)", tupla)

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

def verificaCod(cod):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM procedimentos WHERE cod = " + cod)

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

def buscaProc(coluna, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "SELECT * FROM procedimentos WHERE %s = '%s'" % (coluna, chave)
	cursor.execute(query)

	try:
		proc = cursor.fetchone()[1:]
		strProc = '%'.join(proc)

		return [True, strProc]
	except Exception:
		return [False]

def buscaEsp(coluna, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "SELECT * FROM especialidades WHERE %s = '%s'" % (coluna, chave)
	cursor.execute(query)

	try:
		esp = cursor.fetchone()[1:]
		strEsp = '%'.join(esp)

		return [True, strEsp]
	except Exception:
		return [False]

def buscaColProc(tabela, coluna, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "SELECT * FROM %s WHERE %s = '%s'" % (tabela, coluna, chave)
	cursor.execute(query)

	return len(cursor.fetchall())

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

def alteraProc(cod, coluna, chave):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "UPDATE procedimentos SET " + coluna + " = '" + chave + "' WHERE cod = " + cod
	cursor.execute(query)

	conn.commit()
	conn.close()

def jaTombado(cod, tombo):
	conn = sqlite3.connect('banco.db')
	cursor = conn.cursor()

	query = "SELECT * FROM tombos WHERE fk_equi_cod = " + cod + " AND tombo = '" + tombo + "'"
	cursor.execute(query)

	if cursor.fetchone() == None:
		return False
	else:
		return True