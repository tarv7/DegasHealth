import unittest
import implementacao.medico as med
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('funcionarios')

class VerificarPangramaTests(unittest.TestCase):
	def test_1medicoNovo(self):
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

	def test_2medicoAposPersistencia(self):
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

	def test_3medicoMaisApos(self):
		novo = med.medico()

		res = novo.alteraMedico("97719","Nome", "Jose Ferreira");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraMedico("97719");
		self.assertEqual("Jose Ferreira%M%97719%Brasil%26/08/1977%29/06/2012%28/01/2007", res);

		res = novo.alteraMedico("46193","Sexo", "F");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraMedico("46193");
		self.assertEqual("Rudinei  Rodrigues%F%46193%Brasil%28/05/1962%22/07/1992%18/11/1988", res);

		res = novo.alteraMedico("9614","Nacionalidade", "Italia");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraMedico("9614");
		self.assertEqual("Ailton  Carvalho%M%9614%Italia%26/07/1970%04/10/1999%02/11/1995", res);

		res = novo.alteraMedico("36311","DtNasc", "31/01/1971");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraMedico("36311");
		self.assertEqual("Larissa Pereira%F%36311%Brasil%31/01/1971%13/08/2005%07/11/1999", res);

		res = novo.alteraMedico("3566","DtAdmiss", "19/07/2002");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.alteraMedico("3566","DtAdmiss", "19/07/2015");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraMedico("3566");
		self.assertEqual("Jonelice  Pinto%F%3566%Portugal%07/02/1989%19/07/2015%22/12/2012", res);

		res = novo.alteraMedico("89673","DtFormatura", "30/03/2014");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.alteraMedico("89673","DtFormatura", "30/03/2010");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraMedico("89673");
		self.assertEqual("Jaqueline  das Neves%F%89673%Brasil%12/02/1984%31/05/2013%30/03/2010", res);