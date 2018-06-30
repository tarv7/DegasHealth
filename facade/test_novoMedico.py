import unittest
import implementacao.medico as med
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('funcionarios')

class VerificarPangramaTests(unittest.TestCase):
	def test_tudoCerto(self):
		novo = med.medico()

		res = novo.novoMedico("Nardelle Moraes","M","97719","Brasil","26/08/1977","29/06/2012","28/01/2007")
		self.assertEqual("Medico inserido!", res)

		res = novo.novoMedico("Rudinei  Rodrigues","M","46193","Brasil","28/05/1962","22/7/1992","18/11/1988");
		self.assertEqual("Medico inserido!", res)

		res = novo.novoMedico("Larissa Pereira","F","36311","Brasil","22/01/1977","13/08/2005","07/11/1999");
		self.assertEqual("Medico inserido!", res)

		res = novo.novoMedico("Ailton  Carvalho","M","9614","Brasil","26/07/1970","04/10/1999","02/11/1995");
		self.assertEqual("Medico inserido!", res)

		res = novo.novoMedico("Tarcila do Amaral","F","9614","Brasil","26/07/1970","04/10/1999","02/11/1995");
		self.assertEqual("ERRO! CRM Já existente!", res)

		res = novo.novoMedico("Rudinei  Rodrigues","M","46193","Brasil","28/05/1962","22/7/1992","18/11/1988");
		self.assertEqual("ERRO! CRM Já existente!", res)

	def test_caracInvalido(self):
		novo = med.medico()
		
		res = novo.novoMedico("Rudine%  Rodrigues","M","46193","Brasil","28/05/1962","22/7/1992","18/11/1988")
		self.assertEqual("ERRO! Caracter % Invalido!", res)

		res = novo.novoMedico("Rudinei  R#drigues","M","46193","Brasil","28/05/1962","22/7/1992","18/11/1988")
		self.assertEqual("ERRO! Caracter # Invalido!", res)

		res = novo.novoMedico("Rudinei  Rodrigues","M","46193","Br@sil","28/05/1962","22/7/1992","18/11/1988")
		self.assertEqual("ERRO! Caracter @ Invalido!", res)

		res = novo.novoMedico("Rudine%  Rodrigues","M","46193","Br@sil","28/05/1962","22/7/1992","18/11/1988");
		self.assertEqual("ERRO! Caracter % Invalido!", res)

		res = novo.novoMedico("Rudinei  R#drigues","M","46193","Br@sil","28/05/1962","22/7/1992","18/11/1988");
		self.assertEqual("ERRO! Caracter # Invalido!", res)

		res = novo.novoMedico("Rudinei  R@drig#es","M","46193","Brasil","28/05/1962","22/7/1992","18/11/1988");
		self.assertEqual("ERRO! Caracter @ Invalido!", res)