import unittest
from implementacao.verificar_pangrama import verificar_pangrama

class VerificarPangramaTests(unittest.TestCase):
	def test_retorna_falso_quando_frase_nao_eh_pangrama(self):			
			frase_eh_pangrama = verificar_pangrama("frase")
			self.assertEqual(False, frase_eh_pangrama)
			frase_eh_pangrama = verificar_pangrama("Zebras caolhas de Java querem mandar fax para moça gigante de New York")
			self.assertEqual(True, frase_eh_pangrama)
			frase_eh_pangrama = verificar_pangrama("frsdfgdfgdfgdfase")
			self.assertEqual(False, frase_eh_pangrama)
			frase_eh_pangrama = verificar_pangrama("Zebras caolhas de Java querem mandar fax para moça gigante de New York")
			self.assertEqual(True, frase_eh_pangrama)
			frase_eh_pangrama = verificar_pangrama("frcvbvnvbase")
			self.assertEqual(False, frase_eh_pangrama)
			frase_eh_pangrama = verificar_pangrama("abcdefghijklmnopqrstuvwxyz")
			self.assertEqual(False, frase_eh_pangrama)
			