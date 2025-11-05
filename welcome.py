
import os

menu1=0
listalivros=[]
contadorlivros=0

def adicionar(): # Função para adicionar livros
    os.system("cls")
    global contadorlivros
    try:
        if contadorlivros>=100:
            print("Limite de livros introduzidos. Por favor elimine livros da lista antes de adicionar novos.")
            return
        titulo=input("Introduza o titulo do livro: ")
        autor=input("Introduza o autor do livro: ")
        ano=int(input("Introduza do ano de publição do livro: "))
        livro=f"{titulo} - {autor} - {str(ano)}"
        if livro in listalivros:
            print("Livro já foi introduzido na lista. Livro não adicionado. A voltar ao menu principal.") # Não aceita livros duplicados
            return
        else:
            listalivros.append(livro)
            contadorlivros+=1
    except ValueError:
        print("Introduzir apenas números no ano de publicação. Livro não adicionado. A voltar ao menu principal.") # Protecçao para inputs de integers
        
def pesquisar(): # Função para pesquisar livros
    os.system("cls")
    nao_encontrou=True # Boleano para validar se livro foi ou nao encontrado
    procura=input("Procurar livro por titulo ou autor: ")
    for i in range (len(listalivros)):
        if procura in listalivros[i]:
            nao_encontrou=False
            print(f"{i+1}: {listalivros[i]}") # i+1 porque lista começa no indice 0.
    if nao_encontrou:
        print("Livro não encontrado. A voltar ao menu principal")
            
def apagar(): # Função para apagar livros
    os.system("cls")
    try:
        eliminar=int(input("Excluir um livro a partir da sua posição no catálogo: "))
        if eliminar <= (len(listalivros)):
            del listalivros[eliminar-1] # O -1 tem de ser inserido porque precisa de apagar -1 consoante o valor introduzido porque lista começa no 0.
        else:
            print("Valor introduzido não encontrado em nenhum indice da lista.")
    except ValueError:
        print("Introduzir apenas números. A voltar ao menu principal.") # Apenas aceita numeros porque é integer.
    
def ordenar(): # Função para ordenar livros
    os.system("cls")
    while True:
        organiza=input("Deseja organizar livros alfabeticamente? :").upper() # Converte input em UPPER CASE. Valida 's' ou 'S'.
        if organiza=="S":
            listalivros.sort() # Função de organizar
            print("Livros organizados alfabeticamente. A voltar ao menu.")
            break
        elif organiza=="N":
            print("Livro não organizados. A voltar ao menu.")
            break
        else:
            print("Introduzir apenas 'S/N'.\n")

def listar(): # Função para listar livros
    os.system("cls")
    for i, apresentar in enumerate (listalivros):
        print(f"{i+1}: {apresentar}")
    
while True:
    menu1=input("\n******MENU1******\n\n1 - Adicionar livro:\n2 - Procurar por título ou autor:\n3 - Excluir livro:\n4 - Ordenar livros:\n5 - Listar livros\n6 - Sair do programa: ")
    match menu1:
        case '1':
            adicionar()
        case '2':
            pesquisar()
        case '3':
            apagar()
        case '4':
            ordenar()
        case '5':
            listar()
        case '6':
            print("A sair do programa.")
            break
        case _:
            print("Opção inválida, introduzir apenas 1 a 6.")