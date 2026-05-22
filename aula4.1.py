saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
print(saque <= limite)

print( saldo >= saque and saque <= limite)
# No operador and todas as expressoes precisam ser verdadeiras para o resultado ser verdadeiro
print(saldo >= saque or saque <= limite)
# No operador or apenas uma das expressoes precisa ser verdadeira para o resultado ser verdadeiro