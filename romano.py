def inteiro_para_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numero_romano = ''
    i = 0
    while numero > 0:
        for _ in range(numero // valores[i]):
            numero_romano += simbolos[i]
            numero -= valores[i]
        i += 1
    return numero_romano

def testar_inteiro_para_romano():
    assert inteiro_para_romano(1) == 'I'
    assert inteiro_para_romano(4) == 'IV'
    assert inteiro_para_romano(5) == 'V'
    assert inteiro_para_romano(9) == 'IX'
    assert inteiro_para_romano(10) == 'X'
    assert inteiro_para_romano(50) == 'L'
    assert inteiro_para_romano(100) == 'C'
    assert inteiro_para_romano(500) == 'D'
    assert inteiro_para_romano(1000) == 'M'
    assert inteiro_para_romano(3999) == 'MMMCMXCIX'
    assert inteiro_para_romano(14) == 'XIV'
    assert inteiro_para_romano(44) == 'XLIV'
    assert inteiro_para_romano(99) == 'XCIX'
    assert inteiro_para_romano(2023) == 'MMXXIII'
    print("Todos os testes passaram!")

# Executar testes
testar_inteiro_para_romano()

# Exemplos solicitados
print("Exemplo 1: 3 em algarismos romanos: ", inteiro_para_romano(3))
print("Exemplo 2: 14 em algarismos romanos: ", inteiro_para_romano(14))
print("Exemplo 3: 2024 em algarismos romanos: ", inteiro_para_romano(2024))