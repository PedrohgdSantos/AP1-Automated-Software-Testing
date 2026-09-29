import pytest

from main import aplicar_desconto


def test_desconto_valido():
	assert aplicar_desconto(100, 10) == 90


def test_desconto_de_zero_porcento():
	assert aplicar_desconto(100, 0) == 100


def test_desconto_de_cem_porcento():
	assert aplicar_desconto(100, 100) == 0


def test_desconto_invalido_lanca_value_error():
	with pytest.raises(ValueError):
		aplicar_desconto(100, 101)
