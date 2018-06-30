import unittest
import implementacao.medico as med
import implementacao.banco_de_dados.conexao as db

class VerificarPangramaTests(unittest.TestCase):
	def test_medicoAposPersistencia(self):
		novo = med.medico()

		res = novo.novoMedico("Jonelice  Pinto","F","3566","Portugal","07/02/1989","28/9/2017","22/12/2012");
		self.assertEqual("Medico inserido!", res);

		res = novo.novoMedico("Alvaro Degas","M","3566","Brasil","05/06/1989","28/09/2017","22/12/2012");
		self.assertEqual("ERRO! CRM Já existente!", res);

		res = novo.novoMedico("Jaqueline  das Neves","F","89673","Brasil","12/02/1984","31/04/2013","05/07/2011");
		self.assertEqual("ERRO! Data Inválida!", res);

		res = novo.novoMedico("Jaqueline  das Neves","F","89673","Brasil","12/02/1984","30/2/2013","05/07/2011");
		self.assertEqual("ERRO! Data Inválida!", res);

		res = novo.novoMedico("Jaqueline  das Neves","F","89673","Brasil","12/02/1984","31/3/2011","05/07/2013");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.novoMedico("Jaqueline  das Neves","F","89673","Brasil","12/02/1984","31/05/2013","05/07/2011");
		self.assertEqual("Medico inserido!", res);

		res = novo.encontraMedico("Nardelle Moraes");
		self.assertEqual("Nardelle Moraes%M%97719%Brasil%26/08/1977%29/06/2012%28/01/2007", res);

		res = novo.encontraMedico("36311");
		self.assertEqual("Larissa Pereira%F%36311%Brasil%22/01/1977%13/08/2005%07/11/1999", res);