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