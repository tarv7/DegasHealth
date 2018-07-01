import unittest
import implementacao.especialidade as esp
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('especialidades')

class EspecialidadeTests(unittest.TestCase):
	def test_1procedimentoNovo(self):
		novo = esp.especialidade()

		res = novo.novaEspecialidade("594","Ginecologia");
		self.assertEqual("Especialidade Registrada com sucesso", res);

		res = novo.novaEspecialidade("594","Urologia");
		self.assertEqual("Especialidade já cadastrada", res);
		res = novo.novaEspecialidade("166","Urologia");
		self.assertEqual("Especialidade Registrada com sucesso", res);

		res = novo.novaEspecialidade("531","Ginecologia");
		self.assertEqual("Especialidade já cadastrada", res);
		res = novo.novaEspecialidade("531","Cardiologia");
		self.assertEqual("Especialidade Registrada com sucesso", res);

		res = novo.novaEspecialidade("764","Cirurgia Cardíaca");
		self.assertEqual("Especialidade Registrada com sucesso", res);

		res = novo.novaEspecialidade("251","Ortopedia");
		self.assertEqual("Especialidade Registrada com sucesso", res);

		res = novo.novaEspecialidade("316","Cirurgia Ortopédica");
		self.assertEqual("Especialidade Registrada com sucesso", res);

		res = novo.novaEspecialidade("465","Clínica Geral");
		self.assertEqual("Especialidade Registrada com sucesso", res);

		res = novo.encontraEspecialidade("465");
		self.assertEqual("465%Clínica Geral", res);

		res = novo.encontraEspecialidade("Cardiologia");
		self.assertEqual("531%Cardiologia", res);