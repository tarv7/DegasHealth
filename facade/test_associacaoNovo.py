import unittest
import implementacao.associacao as ass
import implementacao.banco_de_dados.conexao as db

db.deletarTabela('associacoes')

class AssociacoesTests(unittest.TestCase):
	maxDiff = None

	def test_1associacaoNovo(self):
		novo = ass.associacao()

		res = novo.materialProcedimento("763236","2415")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("763236","5927")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("763236","8996")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("763236","1110")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)

		res = novo.equipamentoProcedimento("763236","912")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("763236","685")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("763236","206")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)

		res = novo.listMateriaisProcedimento("763236")
		self.assertEqual("Fio de Sutura%Stinter cardíaco%Antisseptico%Anestesia Geral", res)

		res = novo.listEquipamentosProcedimento("763236")
		self.assertEqual("Mesa de Cirurgia%Raio X%Ultrassom", res)


		res = novo.materialProcedimento("377523","2415")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("377523","3314")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("377523","9622")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("377523","5796")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("377523","4404")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("377523","8996")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("377523","1110")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)

		res = novo.equipamentoProcedimento("377523","912")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("377523","188")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("377523","685")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("377523","206")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("377523","845")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)


		res = novo.materialProcedimento("404482","1881")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)

		res = novo.equipamentoProcedimento("404482","885")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("404482","188")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("404482","358")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)


		res = novo.equipamentoProcedimento("894275","912")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("894275","188")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("894275","358")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)
		res = novo.equipamentoProcedimento("894275","685")
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res)

		res = novo.materialProcedimento("894275","2415")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("894275","3314")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("894275","9622")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("894275","8996")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)
		res = novo.materialProcedimento("894275","1110")
		self.assertEqual("Material Incluido com sucesso no procedimento", res)

	def test_2associacaoChecandoPersistencia(self):
		novo = ass.associacao()

		res = novo.listMateriaisProcedimento("377523");
		self.assertEqual("Fio de Sutura%Gaze%Esparadrapo%Parafuso de Platina%Placa de Platina%Antisseptico%Anestesia Geral", res);

		res = novo.listEquipamentosProcedimento("377523");
		self.assertEqual("Mesa de Cirurgia%Cadeira%Raio X%Ultrassom%Tomógrafo", res);

		res = novo.listMateriaisProcedimento("404482");
		self.assertEqual("Gesso", res);
		res = novo.listEquipamentosProcedimento("404482");
		self.assertEqual("Maca%Cadeira%Mesa de Trabalho", res);

		res = novo.listMateriaisProcedimento("894275");
		self.assertEqual("Fio de Sutura%Gaze%Esparadrapo%Antisseptico%Anestesia Geral", res);
		res = novo.listEquipamentosProcedimento("894275");
		self.assertEqual("Mesa de Cirurgia%Cadeira%Mesa de Trabalho%Raio X", res);


		res = novo.equipamentoProcedimento("839530","885"); # Curativo necessita do apoio de Maca
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res);
		res = novo.equipamentoProcedimento("839530","188"); # Curativo necessita do apoio de Cadeira
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res);
		res = novo.equipamentoProcedimento("839530","358"); # Curativo necessita do apoio de Mesa de Trabalho
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res);

		res = novo.materialProcedimento("839530","3314"); # Curativo consome Gaze
		self.assertEqual("Material Incluido com sucesso no procedimento", res);
		res = novo.materialProcedimento("839530","9622"); # Curativo consome Esparadrapo
		self.assertEqual("Material Incluido com sucesso no procedimento", res);
		res = novo.materialProcedimento("839530","8996"); # Curativo consome Antisseptico
		self.assertEqual("Material Incluido com sucesso no procedimento", res);
		res = novo.materialProcedimento("839530","1111"); # Curativo consome Anestesia Local
		self.assertEqual("Material Incluido com sucesso no procedimento", res);

		#	Curativo
		res = novo.listMateriaisProcedimento("839530");
		self.assertEqual("Gaze%Esparadrapo%Antisseptico%Anestesia Local", res);
		res = novo.listEquipamentosProcedimento("404482");
		self.assertEqual("Maca%Cadeira%Mesa de Trabalho", res);


		#Nebuliza��o
		res = novo.materialProcedimento("200752","7278"); # Nebuliza��o consome Broncodilatador
		self.assertEqual("Material Incluido com sucesso no procedimento", res);


		#	Nebuliza��o
		res = novo.listMateriaisProcedimento("200752");
		self.assertEqual("Broncodilatador", res);


		res = novo.equipamentoProcedimento("886244","912"); # Cateterismo necessita do apoio de Mesa de Cirurgia
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res);
		res = novo.equipamentoProcedimento("886244","188"); # Cateterismo necessita do apoio de Cadeira
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res);
		res = novo.equipamentoProcedimento("886244","685"); # Cateterismo necessita do apoio de Raio X
		self.assertEqual("Equipamento Incluido com sucesso no procedimento", res);


		res = novo.materialProcedimento("886244","8996"); # Cateterismo consome Antisseptico
		self.assertEqual("Material Incluido com sucesso no procedimento", res);
		res = novo.materialProcedimento("886244","1110"); # Cateterismo consome Anestesia Geral
		self.assertEqual("Material Incluido com sucesso no procedimento", res);
		res = novo.materialProcedimento("886244","5927"); # Cateterismo consome Stinter card�aco
		self.assertEqual("Material Incluido com sucesso no procedimento", res);
		self.assertEqual("Material Incluido com sucesso no procedimento", res)

	def test_3associacaoChecandoMais(self):
		novo = ass.associacao()

		#	Cateterismo
		res = novo.listEquipamentosProcedimento("886244");
		self.assertEqual("Mesa de Cirurgia%Cadeira%Raio X", res);
		res = novo.listMateriaisProcedimento("886244");
		self.assertEqual("Antisseptico%Anestesia Geral%Stinter cardíaco", res);