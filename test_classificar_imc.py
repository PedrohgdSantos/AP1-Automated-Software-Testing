import pytest
from main import classificar_imc


def test_imc_abaixo_do_peso():
    assert classificar_imc(18.4) == "Abaixo do peso"


def test_imc_no_limite_do_peso_normal():
    assert classificar_imc(18.5) == "Peso normal"


def test_imc_no_limite_superior_do_peso_normal():
    assert classificar_imc(24.9) == "Peso normal"


def test_imc_acima_do_peso_a_partir_do_limite():
    assert classificar_imc(25) == "Acima do peso"