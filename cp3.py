temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala = 1
max_qtd_criticos = -1
sala_critica = -1

for linha in temperaturas:

    soma = 0
    criticos = 0

    for numero in linha:

        soma = soma + numero

        if numero >= 33:
            criticos = criticos + 1

    media = soma / 4

    if criticos > max_qtd_criticos:
        max_qtd_criticos = criticos
        sala_critica = sala

    print(f"Sala {sala}")
    print(f"Média: {media}")
    print(f"Registros críticos: {criticos}")
    print()

    sala = sala + 1

print(f"Sala com maior risco: Sala {sala_critica}")