#!/bin/sh
python3 -m unittest test_medicoNovo.py -v
python3 -m unittest test_enfermeiroNovo.py -v
python3 -m unittest test_auxiliarNovo.py -v
python3 -m unittest test_procedimentoNovo.py -v
python3 -m unittest test_especialidadeNovo.py -v
python3 -m unittest test_equipamentoNovo.py -v
python3 -m unittest test_materialNovo.py -v
