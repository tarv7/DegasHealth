import unittest
import implementacao.procedimento as proc
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('procedimentos')

class ProcedimentoTests(unittest.TestCase):
	def test_1procedimentoNovo(self):
		novo = proc.procedimento()

		res = novo.novoProcedimento("763236","Ponte de Safena","50000");
		self.assertEqual("Procedimento Incluido com Sucesso", res);

		res = novo.novoProcedimento("763236","Transplante Coração","90000");
		self.assertEqual("Código de Procedimento Ja Cadastrado", res);
		res = novo.novoProcedimento("377523","Ponte de Safena","90000");
		self.assertEqual("Descrição de Procedimento Ja Cadastrado", res);
		res = novo.novoProcedimento("377523","Transplante Coração","90000");
		self.assertEqual("Procedimento Incluido com Sucesso", res);

		res = novo.novoProcedimento("404482","Redução de Fratura","2000.0");
		self.assertEqual("Erro: valor de custo inválido", res);
		res = novo.novoProcedimento("404482","Redução de Fratura","R2000");
		self.assertEqual("Erro: valor de custo inválido", res);
		res = novo.novoProcedimento("404482","Redução de Fratura","R$2000");
		self.assertEqual("Procedimento Incluido com Sucesso", res);

		res = novo.novoProcedimento("894275","Amputação de Membro","$15000,0");
		self.assertEqual("Procedimento Incluido com Sucesso", res);

		res = novo.novoProcedimento("839530","Curativo","50");
		self.assertEqual("Procedimento Incluido com Sucesso", res);

		res = novo.novoProcedimento("200752","Nebulização","100");
		self.assertEqual("Procedimento Incluido com Sucesso", res);

		res = novo.novoProcedimento("886244","Cateterismo","10000");
		self.assertEqual("Procedimento Incluido com Sucesso", res);

		res = novo.encontraProcedimento("404482");
		self.assertEqual("404482%Redução de Fratura%2000", res);

		res = novo.encontraProcedimento("Cateterismo");
		self.assertEqual("886244%Cateterismo%10000", res);

		res = novo.encontraProcedimento("12345");
		self.assertEqual("Procedimento não cadastrado", res);

		res = novo.encontraProcedimento("Obturação");
		self.assertEqual("Procedimento não cadastrado", res);

		res = novo.alteraProcedimento("894275", "Valor", "12000");
		self.assertEqual("Procedimento alterado com sucesso", res);

		res = novo.alteraProcedimento("200752", "Descricao", "Respiração Auxiliada");
		self.assertEqual("Procedimento alterado com sucesso", res);

	def test_2procedimentoAposPersistencia(self):
		novo = proc.procedimento()
		res = novo.encontraProcedimento("404482");
		self.assertEqual("404482%Redução de Fratura%2000", res);

		res = novo.encontraProcedimento("Cateterismo");
		self.assertEqual("886244%Cateterismo%10000", res);

		res = novo.encontraProcedimento("12345");
		self.assertEqual("Procedimento não cadastrado", res);