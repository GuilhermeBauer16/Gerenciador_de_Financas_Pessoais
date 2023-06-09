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
    cursor.execute("SELECT rowid , valor , mes , ano ,opcao , comentario, tipo FROM geral ORDER BY tipo")
    functions.cabecalho('Gerenciamento de dados', 40)
    print(f'{str("N.O"):<5}{"R$":<10}{"Mês":<12}{"Ano":<12}{"Tipo":<12}{"Comentario":<10}{"Status":>25}')
    print('/=' * 40)
    for linha in cursor.fetchall():
        print(f'{str(linha[0]):<5}{linha[1]:<10}{linha[2]:<12}{str(linha[3]):<12}{linha[4]:<12}{linha[5]:<10}{linha[6]:>25}')


def filtro():
    categoria = functions.conversor_numero("Informe a categoria: " , int)
    cursor.execute("SELECT rowid , valor , mes , ano , comentario , tipo FROM geral WHERE tipo =?" , (categoria,))
    print(f'{str("N.O"):<5}{"R$":<10}{"Mês":<12}{"Ano":<12}{"Tipo":<12}{"Comentario":<10}{"Status":>25}')
    print('/=' * 40)


    for linha in cursor.fetchall():
        print(f'{str(linha[0]):<5}{linha[1]:<10}{linha[2]:<12}{str(linha[3]):<12}{linha[4]:<12}{linha[5]:<10}{linha[6]:>25}')
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

    elif opcao == 3:
        mostrar()

    elif opcao == 4:
        filtro()


banco.close()
        