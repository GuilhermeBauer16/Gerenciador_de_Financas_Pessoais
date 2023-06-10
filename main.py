import  _sqlite3
import functions
from time import sleep
banco = _sqlite3.connect("Gerenciador_Tarefas.db")
cursor = banco.cursor()
fonte = ''
tipo = ''
cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name='geral' ")
tabela_existe = cursor.fetchone()


def mostrar():
    cursor.execute("SELECT id , valor , mes , ano ,opcao , comentario, tipo FROM geral ORDER BY tipo")
    functions.cabecalho('Gerenciamento de dados', 40)
    print(f'{str("N.O"):<5}{"R$":<10}{"Mês":<12}{"Ano":<12}{"Tipo":<12}{"Comentario":<10}{"Status":>25}')
    print('/=' * 40)
    for linha in cursor.fetchall():
        print(f'{str(linha[0]):<5}{linha[1]:<10}{linha[2]:<12}{str(linha[3]):<12}{linha[4]:<12}{linha[5]:<10}{linha[6]:>25}')


    for linha in cursor.fetchall():
        print(f'{str(linha[0]):<5}{linha[1]:<10}{linha[2]:<12}{str(linha[3]):<12}{linha[4]:<12}{linha[5]:<10}{linha[6]:>25}')
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



while True:
    functions.cabecalho('Gerenciador de finanças pessoais' , 40)
    print('''
    [1]receitas
    [2]dispesas
    [3]visualização de extrato bancario
    [4]filtro por categoria
    [5]deletar
    [6]editar 
    [7]sair
    ''')
    print('/=' * 40)
    opcao = functions.conversor_numero('Sua opção: ',int)
    if opcao == 1 or opcao == 2:
        if opcao == 1:  
            tipo = 'Receita'
            fonte = functions.receita()
            
        elif opcao == 2 :
            tipo = "Dispesa"
            fonte = functions.dispesa()

        functions.cabecalho(f'{tipo}' , 40)
        receita = functions.receitas(f'Sua {tipo}.R$ ')
        mes = str(input('Imforme o mes por extenso: ')).upper()
        ano = functions.conversor_numero('Imforme o ano: ' , int)
        comentario = str(input('Comentario: '))
        cursor.execute("""INSERT INTO geral (valor , mes , ano ,opcao , comentario, tipo) 
                          VALUES(?,?,?,?,?,?)"""
                        ,(receita, mes, ano ,fonte ,comentario ,tipo))
        banco.commit()

    elif opcao == 3:
        mostrar()

    elif opcao == 4:
        while True:
            functions.cabecalho('Filtro ')
            print("""
[1]Mês
[2]Ano
[3]Tipo
[4]Sair
""")    
            print("=/" * 40)
            op_filtro = functions.conversor_numero('Sua opção: ',int)
            if op_filtro == 1:
                seu_mes = str(input('Imforme o mes: ')).upper()
                cursor.execute("SELECT mes FROM geral WHERE mes = ?" ,( seu_mes,))
                resultado = cursor.fetchall()

                if resultado:
                    print(resultado)
                else:
                    print('Nada foi encontrado! ')
    elif opcao == 5:
        mostrar()
        cursor.execute("SELECT id FROM geral ")
        ids = [row[0] for row in cursor.fetchall()]# para selecionar os ids e guadar em uma lista.
        while True:

            op_deleta = functions.conversor_numero('Imforme o número que deseja deletar[0 para voltar ao menu]: ')
            if op_deleta == 0:
                break
            elif op_deleta in ids:
                try:
                    cursor.execute("DELETE FROM geral WHERE id= ?" , (op_deleta,))
                    banco.commit()
                    print('deletado com sucesso')
                
                except:
                    print('erro ao deletar a tarefa')
            else:
                print('Por favor digite uma opção valida')

    elif opcao == 6:

        while True:
            mostrar()
            print('=/' * 50)
            op_edita = functions.conversor_numero("Digite o numero da tabela que deseja editar[0 para voltar ao menu]: ")
            cursor.execute("SELECT * FROM geral WHERE id= ?" , (op_edita,))
            tabela = cursor.fetchone()
            if op_edita == 0:
                break

            if tabela: 

                functions.cabecalho('Edição', 40)
                print("""
[1]receita
[2]dispesa
""")  
                opcao_receita = functions.conversor_numero('sua opção: ')
                if opcao_receita == 1:  
                    tipo = 'Receita'
                    fonte = functions.receita()

            
                elif opcao_receita == 2 :
                    tipo = "Dispesa"
                    fonte = functions.dispesa()

                
                functions.cabecalho(f'{tipo}' , 40)
                novo_receita = functions.receitas(f'Sua {tipo}.R$ ')
                novo_mes = str(input('Imforme o mes por extenso: ')).upper()
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