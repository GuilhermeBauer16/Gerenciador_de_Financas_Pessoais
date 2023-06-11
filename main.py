import  _sqlite3
import functions
from time import sleep
banco = _sqlite3.connect("Gerenciador_Tarefas.db")
cursor = banco.cursor()
fonte = ''
tipo = ''
cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name='geral' ")
tabela_existe = cursor.fetchone()
if not tabela_existe:

    cursor.execute("""CREATE TABLE geral(
    'id' integer primary key  autoincrement,
    'valor' real , 
    'mes' text ,
    'ano' integer , 
    'opcao' text ,
    'comentario' text , 
    'tipo' text)
    """)


def mostrar():
    cursor.execute("SELECT id , valor , mes , ano ,opcao , comentario, tipo FROM geral ORDER BY tipo")
    functions.cabecalho('Gerenciamento de dados', 50)
    print(f'{str("N.O"):<5}{"R$":<10}{"Mês":<12}{"Ano":<12}{"Tipo":<12}{"Comentario":<10}{"Status":>25}')
    print('/=' * 50)
    for linha in cursor.fetchall():
        print(f'{str(linha[0]):<5}{linha[1]:<10}{linha[2]:<12}{str(linha[3]):<12}{linha[4]:<12}{linha[5]:<10}{linha[6]:>25}')


while True:
    functions.cabecalho('Gerenciador de finanças pessoais' , 50)
    print('''
    [1]receitas
    [2]dispesas
    [3]visualização de extrato bancario
    [4]filtrar por ano ou mês
    [5]deletar
    [6]editar 
    [7]sair
    ''')
    print('/=' * 50)
    opcao = functions.conversor_numero('Sua opção: ',int)
    if opcao == 1 or opcao == 2:
        if opcao == 1:  
            tipo = 'Receita'
            fonte = functions.receita()
            
        elif opcao == 2 :
            tipo = "Dispesa"
            fonte = functions.dispesa()

        functions.cabecalho(f'{tipo}' , 50)
        receita = functions.receitas(f'Sua {tipo}.R$ ')
        mes = str(input('Imforme o mês por extenso: ')).upper()
        ano = functions.conversor_numero('Imforme o ano: ' , int)
        comentario = str(input('Comentario: '))
        cursor.execute("""INSERT INTO geral (valor , mes , ano ,opcao , comentario, tipo) 
                          VALUES(?,?,?,?,?,?)"""
                        ,(receita, mes, ano ,fonte ,comentario ,tipo))
        print('\033[32mAdicionado com sucesso!\033[m')
        banco.commit()

    elif opcao == 3:
        mostrar()

    elif opcao == 4:
        while True:
            mostrar()
            functions.cabecalho('Filtro ', 50)
            print("""
[1]Mês/Ano
[2]Ano
[3]Sair
""")    
            print("=/" * 50)
            op_filtro = functions.conversor_numero('Sua opção: ',int)
            print("=/" * 50)
            if op_filtro == 1:
                seu_mes = str(input('Imforme o mês: ')).upper()
                seu_ano = str(input('Imforme o ano: ')).upper()
                print("=/" * 50)
                cursor.execute("SELECT * FROM geral WHERE mes = ? AND ano= ?" ,( seu_mes,seu_ano,))
                resultado = cursor.fetchall()

                if resultado:
                        print(f'{str("N.O"):<5}{"R$":<10}{"Mês":<12}{"Ano":<12}{"Tipo":<12}{"Comentario":<10}{"Status":>25}')
                        print("=/" * 50)
                        for linha in resultado:
                            print(f'{str(linha[0]):<5}{linha[1]:<10}{linha[2]:<12}{str(linha[3]):<12}{linha[4]:<12}{linha[5]:<10}{linha[6]:>25}')
                else:
                    print("=/" * 50)
                    print('\033[31mNada foi encontrado!\033[m ')

                sleep(1)
            elif op_filtro == 2: 
                seu_ano = str(input('Imforme o ano: ')).upper()
                print("=/" * 50)
                cursor.execute("SELECT * FROM geral WHERE ano = ?" ,( seu_ano,))
                resultado = cursor.fetchall()
                
                if resultado:
                    print(f'{str("N.O"):<5}{"R$":<10}{"Mês":<12}{"Ano":<12}{"Tipo":<12}{"Comentario":<10}{"Status":>25}')
                    print('/=' * 50)
                    for linha in resultado:
                        print(f'{str(linha[0]):<5}{linha[1]:<10}{linha[2]:<12}{str(linha[3]):<12}{linha[4]:<12}{linha[5]:<10}{linha[6]:>25}')
                else:
                    print("=/" * 50)
                    print('\033[31mNada foi encontrado!\033[m ')

                sleep(1)
            elif op_filtro == 3:
                print('Voltando para o menu')
                sleep(1)
                break
            else:
                print('\033[31mPorfavor selecione uma opcão valida!\033[m')

    elif opcao == 5:
        mostrar()
        cursor.execute("SELECT id FROM geral ")
        ids = [row[0] for row in cursor.fetchall()]# para selecionar os ids e guadar em uma lista.
        while True:
            print('/=' * 50)
            op_deleta = functions.conversor_numero('Imforme o número que deseja deletar[0 para voltar ao menu]: ')
            if op_deleta == 0:
                print('voltando ao menu')
                break
            elif op_deleta in ids:
                try:
                    cursor.execute("DELETE FROM geral WHERE id= ?" , (op_deleta,))
                    banco.commit()
                    print('\033[32mdeletado com sucesso\033[m')
                
                except:
                    print('\033[31merro ao deletar a tarefa\033[m')
            else:
                print('\033[31mPorfavor selecione uma opcão valida!\033[m')

    elif opcao == 6:

        while True:
            mostrar()
            print('=/' * 50)
            op_edita = functions.conversor_numero("Digite o numero da tabela que deseja editar[0 para voltar ao menu]: ")
            cursor.execute("SELECT * FROM geral WHERE id= ?" , (op_edita,))
            tabela = cursor.fetchone()
            if op_edita == 0:
                print('voltando ao menu')
                break

            if tabela: 

                functions.cabecalho('Edição', 50)
                print("""
[1]receita
[2]dispesa
""")  
                print('/=' * 50)
                opcao_receita = functions.conversor_numero('sua opção: ')
                if opcao_receita == 1:  
                    tipo = 'Receita'
                    fonte = functions.receita()

            
                elif opcao_receita == 2 :
                    tipo = "Dispesa"
                    fonte = functions.dispesa()

                
                functions.cabecalho(f'{tipo}' , 50)
                novo_receita = functions.receitas(f'Sua {tipo}.R$ ')
                novo_mes = str(input('Imforme o mês por extenso: ')).upper()
                novo_ano = functions.conversor_numero('Imforme o ano: ' , int)
                novo_comentario = str(input('Comentario: '))
                cursor.execute("""UPDATE  geral SET valor = ?, mes = ? , ano = ?
                ,opcao = ? , comentario = ?, tipo = ? WHERE id = ?  """,
                        (novo_receita, novo_mes, novo_ano ,fonte ,novo_comentario , tipo ,op_edita ))
                banco.commit()
                    
            else:
                print('=/' * 40)
                print('\033[31mPor favor selecione uma opção valida!\033[m')
                sleep(1)
        

    elif opcao == 7:
        print('Saindo...')
        sleep(1)
        break

banco.close()
