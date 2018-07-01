import implementacao.banco_de_dados.conexao as db
import implementacao.utils.utils as util

# Codigo, Descricao, Custo
class associacao(object):
	def __init__(self):
		db.iniciar()
		super().__init__()
	def materialProcedimento(self, proc, mat):
		db.inserirAsso('fk_mat_cod', (proc, mat))
		return 'Material Incluido com sucesso no procedimento'

	def equipamentoProcedimento(self, proc, equi):
		db.inserirAsso('fk_equi_cod', (proc, equi))
		return 'Equipamento Incluido com sucesso no procedimento'

	def listMateriaisProcedimento(self, cod):
		return db.buscaListaProc('fk_mat_cod', cod)

	def listEquipamentosProcedimento(self, cod):
		return db.buscaListaProc('fk_equi_cod', cod)