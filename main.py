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

    cursor.execute("CREATE TABLE geral ('valor' real , 'mes' text , 'ano' integer , 'opcao' text ,'comentario' text , 'tipo' text)")



while True:
    functions.cabecalho('Gerenciador de tarefas' , 40)
    print('''
    [1]receitas
    [2]dispesas
    [3]visualização de extrato bancario
    [4]filtro por categoria
    [5]deletar
    [6]editar 
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
        cursor.execute("INSERT INTO geral VALUES(?,?,?,?,?,?)",(receita, mes, ano ,fonte ,comentario ,tipo))
        banco.commit()

        