# Solicita a quantidade de alunos, monitores e convidados
alunos = int(input("Digite a quantidade de alunos: "))
monitores = int(input("Digite a quantidade de monitores: "))
convidados = int(input("Digite a quantidade de convidados: "))

# Calcula o total de participantes
total_participantes = alunos + monitores + convidados

# Verifica as condições e exibe a mensagem apropriada
if total_participantes <= 100 and convidados <= 20:
    print("O evento pode ocorrer conforme planejado.")
elif total_participantes > 100:
    print("O número de ingressos é insuficiente.")
else:
    print("O número de convidados é superior ao permitido.")
