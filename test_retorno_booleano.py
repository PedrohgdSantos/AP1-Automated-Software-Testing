from main import senha_valida


def test_senha_valida():
	assert senha_valida("senha1234") is True


def test_senha_curta_demais():
	assert senha_valida("abc123") is False


def test_senha_sem_numero():
	assert senha_valida("senhaforte") is False


def test_senha_com_exatamente_oito_caracteres():
	assert senha_valida("senha123") is True
