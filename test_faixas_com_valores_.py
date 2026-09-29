from main import calcular_frete


def test_frete_na_primeira_faixa():
	assert calcular_frete(3) == 10.0


def test_frete_no_limite_de_5():
	assert calcular_frete(5) == 10.0


def test_frete_na_segunda_faixa():
	assert calcular_frete(7) == 20.0


def test_frete_no_limite_de_10():
	assert calcular_frete(10) == 20.0


def test_frete_na_terceira_faixa():
	assert calcular_frete(12) == 35.0
