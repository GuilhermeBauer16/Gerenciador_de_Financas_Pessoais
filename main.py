import  _sqlite3
import functions
banco = _sqlite3.connect("Gerenciador_Tarefas.db")
cursor = banco.cursor()

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
    if opcao == 1:
        functions.cabecalho('Receitas' , 40)
        receita = functions.receitas('Suas receitas.R$ ')
        