import unittest
import implementacao.auxiliar as aux
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('auxiliares')

class AuxiliarTests(unittest.TestCase):
	def test_1auxiliarNovo(self):
		novo = aux.auxiliar()

		res = novo.novoAuxiliar("Augusta Rua","M","297719","Brasil","24/02/1969","29/12/2016","28/06/2015");
		self.assertEqual("Auxiliar/Técnico inserido!", res);

		res = novo.novoAuxiliar("Bárbara%  Leonel","F","251329","Brasil","18/10/1971","22/01/1999","18/05/1990");
		self.assertEqual("ERRO! Caracter '%' Invalido!", res);

		res = novo.novoAuxiliar("Cêcharpe L#dligues","M","251329","Brasil","28/11/1961","22/01/1992","18/05/1988");
		self.assertEqual("ERRO! Caracter '#' Invalido!", res);

		res = novo.novoAuxiliar("Dalva Branquinha Alves","F","251329","Br@sil","24/06/1981","22/01/2012","18/05/2000");
		self.assertEqual("ERRO! Caracter '@' Invalido!", res);

		res = novo.novoAuxiliar("Elie%e  dos Ponteiros","F","251329","Br@sil","03/06/1991","22/06/2017","18/05/2017");
		self.assertEqual("ERRO! Caracter '%' Invalido!", res);

		res = novo.novoAuxiliar("Fabíola do C#menor","M","251329","Br@sil","28/11/1961","23/09/1991","28/08/1988");
		self.assertEqual("ERRO! Caracter '#' Invalido!", res);

		res = novo.novoAuxiliar("Galinda C@xaqt#","F","251329","Brasil","18/11/1962","22/01/1992","18/05/1988");
		self.assertEqual("ERRO! Caracter '@' Invalido!", res);

		res = novo.novoAuxiliar("Hermitío da Gruta Longe","M","251329","Brasil","28/11/1962","22/01/1992","18/05/1988");
		self.assertEqual("Auxiliar/Técnico inserido!", res);

		res = novo.novoAuxiliar("Ivan da Van Dutch","M","251329","Brasil","28/11/1961","22/01/1992","18/10/1988");
		self.assertEqual("ERRO! COREN Já existente!", res);

		res = novo.novoAuxiliar("Jileno da Lamina Cega","M","29614","Brasil","26/01/1970","04/04/1999","02/05/1995");
		self.assertEqual("Auxiliar/Técnico inserido!", res);

		res = novo.novoAuxiliar("Lucas Bolseiro","M","29614","Brasil","26/03/1970","04/02/1999","02/10/1995");
		self.assertEqual("ERRO! COREN Já existente!", res);

		res = novo.novoAuxiliar("Maria do Bairro","F","236311","Brasil","22/07/1976","13/08/2005","07/05/1999");
		self.assertEqual("Auxiliar/Técnico inserido!", res);

	def test_2auxiliarAposPersistencia(self):
		novo = aux.auxiliar()

		res = novo.novoAuxiliar("Naiara Cinquenta","F","21566","Tchéquia","07/10/1988","28/09/2016","22/06/2012");
		self.assertEqual("Auxiliar/Técnico inserido!", res);

		res = novo.novoAuxiliar("Olimpo Luz do Panteão Divino ","M","21566","Brasil","05/12/1989","28/03/2017","22/06/2012");
		self.assertEqual("ERRO! COREN Já existente!", res);

		res = novo.novoAuxiliar("Pablo Bardo da Sofrência Boêmio","M","289673","Brasil","12/10/1984","32/10/2013","05/01/2011"); 
		self.assertEqual("ERRO! Data Inválida!", res); 

		res = novo.novoAuxiliar("Quincas Borba","M","289673","Brasil","12/10/1983","32/10/2012","05/01/2011");
		self.assertEqual("ERRO! Data Inválida!", res);

		res = novo.novoAuxiliar("Rubens Paiva","M","289673","Brasil","12/02/1984","31/3/2011","05/07/2013");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.novoAuxiliar("Sábado de Sol Silva","M","289673","Brasil","12/08/1984","30/11/2013","05/01/2011");
		self.assertEqual("Auxiliar/Técnico inserido!", res);

		res = novo.encontraAuxiliar("Augusta Rua");
		self.assertEqual("Augusta Rua%M%297719%Brasil%24/02/1969%29/12/2016%28/06/2015", res);

		res = novo.encontraAuxiliar("251329");
		self.assertEqual("Hermitío da Gruta Longe%M%251329%Brasil%28/11/1962%22/01/1992%18/05/1988", res);

	def test_3auxiliarMaisApos(self):
		novo = aux.auxiliar()

		res = novo.alteraAuxiliar("297719","Nome", "Arsenio Pereira da Produção Eficaz");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraAuxiliar("297719");
		self.assertEqual("Arsenio Pereira da Produção Eficaz%M%297719%Brasil%24/02/1969%29/12/2016%28/06/2015", res);

		res = novo.alteraAuxiliar("251329","Sexo", "F");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraAuxiliar("251329");
		self.assertEqual("Hermitío da Gruta Longe%F%251329%Brasil%28/11/1962%22/01/1992%18/05/1988", res);

		res = novo.alteraAuxiliar("29614","Nacionalidade", "Argentina");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraAuxiliar("29614");
		self.assertEqual("Jileno da Lamina Cega%M%29614%Argentina%26/01/1970%04/04/1999%02/05/1995", res);

		res = novo.alteraAuxiliar("236311","DtNasc", "31/01/1971");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraAuxiliar("236311");
		self.assertEqual("Maria do Bairro%F%236311%Brasil%31/01/1971%13/08/2005%07/05/1999", res);

		res = novo.alteraAuxiliar("21566","DtAdmiss", "19/02/2002");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.alteraAuxiliar("21566","DtAdmiss", "19/07/2015");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraAuxiliar("21566");
		self.assertEqual("Naiara Cinquenta%F%21566%Tchéquia%07/10/1988%19/07/2015%22/06/2012", res);

		res = novo.alteraAuxiliar("289673","DtFormatura", "30/03/2014");
		self.assertEqual("ERRO! Inconsistencia de datas: Formatura posterior a admissão!", res);

		res = novo.alteraAuxiliar("289673","DtFormatura", "30/03/2010");
		self.assertEqual("Alteracao executada com sucesso!", res);
		res = novo.encontraAuxiliar("289673");
		self.assertEqual("Sábado de Sol Silva%M%289673%Brasil%12/08/1984%30/11/2013%30/03/2010", res);