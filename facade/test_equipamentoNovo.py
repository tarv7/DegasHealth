import unittest
import implementacao.equipamento as aqui
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('equipamentos')
db.deletarTabela('tombos')

class ProcedimentoTests(unittest.TestCase):
	def test_1equipamentoNovo(self):
		novo = aqui.equipamento()

		res = novo.novoEquipamento("912","Mesa de Cirurgia","35000");
		self.assertEqual("Equipamento cadastrado com sucesso", res);

		res = novo.novoEquipamento("885","Maca","4000");
		self.assertEqual("Equipamento cadastrado com sucesso", res);

		res = novo.novoEquipamento("188","Cadeira","500");
		self.assertEqual("Equipamento cadastrado com sucesso", res);

		res = novo.novoEquipamento("358","Mesa de Trabalho","800");
		self.assertEqual("Equipamento cadastrado com sucesso", res);

		res = novo.novoEquipamento("685","Raio X","45000");
		self.assertEqual("Equipamento cadastrado com sucesso", res);

		res = novo.novoEquipamento("206","Ultrassom","30000");
		self.assertEqual("Equipamento cadastrado com sucesso", res);

		res = novo.novoEquipamento("845","Tomógrafo","800000");
		self.assertEqual("Equipamento cadastrado com sucesso", res);

		res = novo.tombaEquipamento("912", "MC001");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("912", "MC002");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("912", "MC002");
		self.assertEqual("Erro: Tombo já existente", res);

		res = novo.tombaEquipamento("912", "MC003");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("885", "MCA001");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("885", "MCA002");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("885", "MCA003");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("885", "MCA004");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("885", "MCA005");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("188", "CAD001");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("188", "CAD002");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("188", "CAD003");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("188", "CAD004");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("188", "CAD005");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("188", "CAD006");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("188", "CAD007");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("358", "MST001");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("358", "MST002");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("358", "MST003");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("358", "MST004");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("685", "RX01");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("685", "RX02");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("206", "US01");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("206", "US02");
		self.assertEqual("Equipamento tombado com sucesso", res);

		res = novo.tombaEquipamento("845", "TM02");
		self.assertEqual("Equipamento tombado com sucesso", res);