import pytest

from main import calcular_media


def test_media_de_notas_diferentes():
	assert calcular_media([7, 8, 9]) == 8


def test_media_de_notas_iguais():
	assert calcular_media([6, 6, 6]) == 6


def test_media_de_uma_unica_nota():
	assert calcular_media([9]) == 9


def test_lista_vazia_lanca_value_error():
	with pytest.raises(ValueError):
		calcular_media([])
