from time import sleep
print('\033[1;31m#' * 22)
print('## VALIDADOR DE CPF ##')
print('#' * 22)
sleep(1)
while True:
    cpf = input('\033[mDigite seu CPF \033[1;33m(apenas números)\033[m:\n-> ')
    while not cpf.isnumeric() or len(cpf) != 11:
        cpf = input('\033[1;31mERRO!\033[m\nCPF contém 11 dígitos!\n-> ')
    cpf_novo = cpf[:-2]  # Retirei os dois últimos números
    sequencia = cpf[0] * len(cpf)  # Verificando se CPF é o mesmo número repetido

    if sequencia == cpf:
        print('CPF é uma sequência de números')
        break
    multipli = 10
    multipli2 = 11
    valor_da_multipli = valor_da_multipli2 = soma1 = soma2 = 0

    for i in cpf_novo:
        if multipli >= 2:
            valor_da_multipli = int(i) * multipli
            soma1 += valor_da_multipli
            valor_da_multipli = 0
            multipli -= 1
    #  Encontrando o penúltimo dígito
    d1 = 11 - (soma1 % 11)
    if d1 > 9:
        d1 = 0
    cpf_novo += str(d1)

    for i in cpf_novo:
        if multipli2 >= 2:
            valor_da_multipli2 = int(i) * multipli2
            soma2 += valor_da_multipli2
            valor_da_multipli2 = 0
            multipli2 -= 1
    # Encontrando o último dígito
    d2 = 11 - (soma2 % 11)
    cpf_novo += str(d2)

    if cpf == cpf_novo:
        print('\033[1;94m#' * 23)
        print('## SEU CPF É VÁLIDO! ##')
        print('#' * 23)
        break
    else:
        print('\033[1;31m#' * 25)
        print('## SEU CPF É INVÁLIDO! ##')
        print('#' * 25)
        break
