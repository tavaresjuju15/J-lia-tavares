# Definindo as variáveis
total_idades = 36

# Vamos iterar sobre possíveis idades para o primeiro aluno
for idade1 in range(1, total_idades):
    # O terceiro aluno tem a mesma idade que o primeiro
    idade3 = idade1

    # Agora, vamos encontrar a idade do segundo aluno, sabendo que um deles tem o dobro da idade do outro
    idade2 = total_idades - idade1 - idade3

    # Verificando se a idade2 é o dobro de idade1 ou se idade1 é o dobro de idade2
    if idade2 == 2 * idade1 or idade1 == 2 * idade2:
        # Se encontramos uma combinação válida, imprimimos as idades
        print(f"Idade do primeiro aluno: {idade1}")
        print(f"Idade do segundo aluno: {idade2}")
        print(f"Idade do terceiro aluno: {idade3}")
        break  # Paramos o loop, pois encontramos uma solução
