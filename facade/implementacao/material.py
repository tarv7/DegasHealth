import implementacao.banco_de_dados.conexao as db
import implementacao.utils.utils as util

# Codigo, Descricao, Custo
class material(object):
	def __init__(self):
		db.iniciar()
		super().__init__()
	def novoMaterial(self, cod, desc, quant):
		db.inserirMaterial((cod, desc, quant))
		return 'Material Cadastrado com sucesso'