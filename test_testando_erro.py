import pytest

from main import sacar


def test_saque_valido():
	assert sacar(100, 40) == 60


def test_saque_invalido_lanca_value_error():
	with pytest.raises(ValueError):
		sacar(100, 120)
