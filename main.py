# Questão 1 — Casos de teste por faixa

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    return "Acima do peso"

# Questão 2 — Testando erro

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor

# Questão 3 — Faixas com valores de fronteira

def calcular_frete(peso):
    if peso <= 5:
        return 10.0
    if peso <= 10:
        return 20.0
    return 35.0

# Questão 4 — Retorno booleano

def senha_valida(senha):
    if len(senha) < 8:
        return False
    return any(c.isdigit() for c in senha)

# Questão 5 — Cálculo com validação

def aplicar_desconto(valor, desconto):
    if desconto < 0 or desconto > 100:
        raise ValueError("Desconto inválido")
    return valor - (valor * desconto / 100)

# Questão 6 — Lista de notas

def calcular_media(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")
    return sum(notas) / len(notas)