acumulador = 0 
print('Bem Vindo a Lanchonete')
print('******************Cardápio*****************')
print('| Código |       Descrição       |  Valor |')
print('|  100   |    Cachorro Quente    |   9,00 |')
print('|  101   | Cachorro Quente Duplo |  11,00 |')
print('|  102   |         X-Egg         |  12,00 |')
print('|  103   |        X-Salada       |  13,00 |')
print('|  104   |         X-Bacon       |  14,00 |')
print('|  105   |         X-Tudo        |  17,00 |')
print('|  200   |   Refrigerante Lata   |   5,00 |')
print('|  201   |      Chá Gelado       |   4,00 |')
while True:  
    codigo = int(input('Entre com o código desejado:'))  
    if codigo == 100:
        print('Você pediu um Cachorro-Quente no valor de 9,00')
        acumulador = acumulador + 9.00
    elif codigo == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        acumulador = acumulador + 11.00
    elif codigo == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        acumulador = acumulador + 12.00
    elif codigo == 103:
        print('Você pediu um X-Salada no valor de 12,00')
        acumulador = acumulador + 13.00
    elif codigo == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        acumulador = acumulador + 14.00
    elif codigo == 105:
        print('Você pediu um X-Tudo no valor de 17,00')
        acumulador = acumulador + 17.00
    elif codigo == 200:
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        acumulador = acumulador + 5.00
    elif codigo == 201:
        print('Você pediu um Chá Gelado no valor de 4,00')
        acumulador = acumulador + 4.00
    else:
        print('Opção Inválida')
        continue
    resposta = input('Deseja pedir mais alguma coisa?\n''1 - Sim\n''0 - Não\n''>> ')
    if resposta == '1':
        continue
    else:
        print('O total a ser pago é: {}'.format(acumulador))
        break
