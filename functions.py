def conversor_numero(msg , tipo = int):
    while True: 
        numero = input(msg)
        try:
            numero_covertido = tipo(numero)
            break
        except ValueError:
            print('Por favor imforme um numero!')

    return numero_covertido


def cabecalho(msg, quant= 40):
    quantia = quant * 2
    print('/=' * quant)
    print(f'{msg: ^{quantia}}')
    print('/=' * quant)


def receitas(msg):

    while True:
        'Suas receitas.R$ '
        receitas = input(msg)
        receitas = receitas.replace(',','.')
        try:
            float_receitas = float(receitas)
            break
            
        except ValueError:
            print('Por favor digite um valor.Exemplo: 100,00')    
            
    return float_receitas


def receita():
    from time import sleep
    fonte = ''
    while True:
        cabecalho(f'Tipo de receita', 40)
        print('''
[1]Salário
[2]Freelancer
[3]Outro 
                ''')
        sleep(1)
        print('/=' * 40)
        op_receita = conversor_numero('sua opção: ', int)
        print('/=' * 40)
        if op_receita == 1:
            fonte ='salario'
            break
        elif op_receita == 2:
            fonte = 'freelancer'
            break
        elif op_receita == 3:
            fonte = 'outro'
            break

        else:
            print('por favor imforme uma opção valida!')

    return fonte


def dispesa():
    from time import sleep
    fonte = ''
    while True:
        cabecalho(f'Tipo de Dispesa', 40)
        print('''
[1]Esenssial 
[2]Lazer 
[3]Financiameto
[4]Viagem
[5]Outro 
                ''')
        sleep(1)
        print('/=' * 40)
        op_receita = conversor_numero('sua opção: ', int)
        print('/=' * 40)
        if op_receita == 1:
            fonte ='Esenssial'
            break
        elif op_receita == 2:
            fonte = 'Lazer'
            break
        elif op_receita == 3:
            fonte = 'Financiameto'
            break
        elif op_receita == 4:
            fonte = 'Viagem'
            break
        elif op_receita == 5:
            fonte = 'outro'
            break

        else:
            print('por favor imforme uma opção valida!')

    return fonte

