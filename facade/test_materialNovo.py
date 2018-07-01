import unittest
import implementacao.material as mat
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('materiais')

class MaterialTests(unittest.TestCase):
	def test_1materialNovo(self):
		novo = mat.material()

		res = novo.novoMaterial("2415","Fio de Sutura","2");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("3314","Gaze","2");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("9622","Esparadrapo","3");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("1881","Gesso","5");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("5796","Parafuso de Platina","150");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("4404","Placa de Platina","500");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("5927","Stinter cardíaco","500");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("8996","Antisseptico","15");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("7278","Broncodilatador","20");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("1110","Anestesia Geral","800");
		self.assertEqual("Material Cadastrado com sucesso", res);

		res = novo.novoMaterial("1111","Anestesia Local","40");
		self.assertEqual("Material Cadastrado com sucesso", res);