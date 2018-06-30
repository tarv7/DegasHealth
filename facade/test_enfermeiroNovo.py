import unittest
import implementacao.enfermeiro as enf
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('enfermeiros')

class VerificarPangramaTests(unittest.TestCase):
	def test_1enfermeiroNovo(self):
		novo = enf.enfermeiro()

		res = novo.novoEnfermeiro("Amadildo Maldonado","M","197719","Brasil","24/08/1969","29/06/2017","28/01/2016");
		self.assertEqual("Enfermeiro inserido!", res);

		res = novo.novoEnfermeiro("Bruna%  Surfer","F","151329","Brasil","18/04/1972","22/07/1999","18/11/1990");
		self.assertEqual("ERRO! Caracter '%' Invalido!", res);

		res = novo.novoEnfermeiro("Carine  R#drigues","F","151329","Brasil","28/05/1962","22/7/1992","18/11/1988");
		self.assertEqual("ERRO! Caracter '#' Invalido!", res);

		res = novo.novoEnfermeiro("Doravante  Alavante","F","151329","Br@sil","24/01/1982","22/7/2012","18/11/2000");
		self.assertEqual("ERRO! Caracter '@' Invalido!", res);

		res = novo.novoEnfermeiro("Edilen%e  dos Santos","F","151329","Br@sil","03/12/1991","22/1/2018","18/11/2017");
		self.assertEqual("ERRO! Caracter '%' Invalido!", res);

		res = novo.novoEnfermeiro("Fábio  J#nior","M","151329","Br@sil","28/05/1962","23/03/1992","28/12/1988");
		self.assertEqual("ERRO! Caracter '#' Invalido!", res);

		res = novo.novoEnfermeiro("Geremilda  L@jot#","F","151329","Brasil","18/05/1962","22/07/1992","18/11/1988");
		self.assertEqual("ERRO! Caracter '@' Invalido!", res);

		res = novo.novoEnfermeiro("Horáclides da Hora Certa","M","151329","Brasil","28/05/1962","22/07/1992","18/11/1988");
		self.assertEqual("Enfermeiro inserido!", res);

		res = novo.novoEnfermeiro("Ítalo  Pinto Vloger","M","151329","Brasil","28/05/1962","22/7/1992","18/11/1988");
		self.assertEqual("ERRO! COREN Já existente!", res);

		res = novo.novoEnfermeiro("Jalapeno Kino","M","19614","Brasil","26/07/1970","04/10/1999","02/11/1995");
		self.assertEqual("Enfermeiro inserido!", res);

		res = novo.novoEnfermeiro("Larissa de Las Dolores","F","19614","Brasil","26/07/1970","04/10/1999","02/11/1995");
		self.assertEqual("ERRO! COREN Já existente!", res);

		res = novo.novoEnfermeiro("Maria do Bairro","F","136311","Brasil","22/01/1977","13/08/2005","07/11/1999");
		self.assertEqual("Enfermeiro inserido!", res);

	def test_2enfermeiroAposPersistencia(self):
		novo = enf.enfermeiro()

		res = novo.novoEnfermeiro("Alfarroba Cacau","F","1566","Portugal","07/02/1989","28/09/2017","22/12/2012");
		self.assertEqual("Enfermeiro inserido!", res);

		res = novo.novoEnfermeiro("Olivia Oliveira das Olivas","M","1566","Brasil","05/06/1989","28/09/2017","22/12/2012");
		self.assertEqual("ERRO! COREN Já existente!", res);

		res = novo.novoEnfermeiro("John  de Las Nieves","M","189673","Brasil","12/02/1984","31/04/2013","05/07/2011");
		self.assertEqual("ERRO! Data Inválida!", res);

		res = novo.novoEnfermeiro("John  Gothic Ranger","M","189673","Brasil","12/02/1984","30/2/2013","05/07/2011");
		self.assertEqual("ERRO! Data Inválida!", res);

		res = novo.novoEnfermeiro("Jaquelina  das Neves","F","189673","Brasil","12/02/1984","31/3/2011","05/07/2013");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.novoEnfermeiro("Bátima da Silva Sauro","F","189673","Brasil","12/02/1984","31/05/2013","05/07/2011");
		self.assertEqual("Enfermeiro inserido!", res);

		res = novo.encontraEnfermeiro("Amadildo Maldonado");
		self.assertEqual("Amadildo Maldonado%M%197719%Brasil%24/08/1969%29/06/2017%28/01/2016", res);

		res = novo.encontraEnfermeiro("151329");
		self.assertEqual("Horáclides da Hora Certa%M%151329%Brasil%28/05/1962%22/07/1992%18/11/1988", res);

	def test_3enfermeiroMaisApos(self):
		novo = enf.enfermeiro()

		res = novo.alteraEnfermeiro("197719","Nome", "Arminho Amando Amador Amor Divino");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraEnfermeiro("197719");
		self.assertEqual("Arminho Amando Amador Amor Divino%M%197719%Brasil%24/08/1969%29/06/2017%28/01/2016", res);

		res = novo.alteraEnfermeiro("151329","Sexo", "F");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraEnfermeiro("151329");
		self.assertEqual("Horáclides da Hora Certa%F%151329%Brasil%28/05/1962%22/07/1992%18/11/1988", res);

		res = novo.alteraEnfermeiro("19614","Nacionalidade", "Italia");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraEnfermeiro("19614");
		self.assertEqual("Jalapeno Kino%M%19614%Italia%26/07/1970%04/10/1999%02/11/1995", res);

		res = novo.alteraEnfermeiro("136311","DtNasc", "31/01/1971");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraEnfermeiro("136311");
		self.assertEqual("Maria do Bairro%F%136311%Brasil%31/01/1971%13/08/2005%07/11/1999", res);

		res = novo.alteraEnfermeiro("1566","DtAdmiss", "19/02/2002");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.alteraEnfermeiro("1566","DtAdmiss", "19/07/2015");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraEnfermeiro("1566");
		self.assertEqual("Alfarroba Cacau%F%1566%Portugal%07/02/1989%19/07/2015%22/12/2012", res);

		res = novo.alteraEnfermeiro("189673","DtFormatura", "30/03/2014");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.alteraEnfermeiro("189673","DtFormatura", "30/03/2010");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraEnfermeiro("189673");
		self.assertEqual("Bátima da Silva Sauro%F%189673%Brasil%12/02/1984%31/05/2013%30/03/2010", res);
